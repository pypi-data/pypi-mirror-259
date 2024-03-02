from pathlib import Path
from typing import TYPE_CHECKING, Any, Union, cast

from tarina import lang
from nonebot.internal.driver import Request
from nonebot.adapters import Bot, Event, Message

from ..export import Target, SupportAdapter, MessageExporter, SerializeFailed, export
from ..segment import At, File, Text, AtAll, Audio, Emoji, Image, Reply, Video, Voice, Reference, CustomNode

if TYPE_CHECKING:
    from nonebot.adapters.red.message import MessageSegment


class RedMessageExporter(MessageExporter["MessageSegment"]):
    def get_message_type(self):
        from nonebot.adapters.red.message import Message

        return Message

    @classmethod
    def get_adapter(cls) -> SupportAdapter:
        return SupportAdapter.red

    def get_target(self, event: Event, bot: Union[Bot, None] = None) -> Target:
        from nonebot.adapters.red.api.model import ChatType
        from nonebot.adapters.red.api.model import Message as MessageModel

        assert isinstance(event, MessageModel)
        return Target(
            str(event.peerUin or event.peerUid),
            private=event.chatType == ChatType.FRIEND,
            platform=self.get_adapter(),
            self_id=bot.self_id if bot else None,
        )

    def get_message_id(self, event: Event) -> str:
        from nonebot.adapters.red.event import MessageEvent

        assert isinstance(event, MessageEvent)
        return f"{event.msgId}#{event.msgSeq}"

    @export
    async def text(self, seg: Text, bot: Bot) -> "MessageSegment":
        ms = self.segment_class
        return ms.text(seg.text)

    @export
    async def at(self, seg: At, bot: Bot) -> "MessageSegment":
        ms = self.segment_class

        return ms.at(seg.target)

    @export
    async def at_all(self, seg: AtAll, bot: Bot) -> "MessageSegment":
        ms = self.segment_class

        return ms.at_all()

    @export
    async def emoji(self, seg: Emoji, bot: Bot) -> "MessageSegment":
        ms = self.segment_class

        return ms.face(seg.id)

    @export
    async def media(self, seg: Union[Image, Video, File], bot: Bot) -> "MessageSegment":
        ms = self.segment_class

        name = seg.__class__.__name__.lower()
        method = {
            "image": ms.image,
            "video": ms.video,
            "file": ms.file,
        }[name]
        if seg.path:
            return method(Path(seg.path))
        elif seg.raw:
            return method(seg.raw_bytes)
        elif seg.url:
            resp = await bot.adapter.request(Request("GET", seg.url))
            return method(resp.content)  # type: ignore
        else:
            raise SerializeFailed(lang.require("nbp-uniseg", "invalid_segment").format(type=name, seg=seg))

    @export
    async def voice(self, seg: Union[Voice, Audio], bot: Bot) -> "MessageSegment":
        ms = self.segment_class

        name = seg.__class__.__name__.lower()
        if seg.path:
            return ms.voice(Path(seg.path), duration=seg.duration or 1)
        elif seg.raw:
            return ms.voice(seg.raw_bytes, duration=seg.duration or 1)
        elif seg.url:
            resp = await bot.adapter.request(Request("GET", seg.url))
            return ms.voice(resp.content, duration=seg.duration or 1)  # type: ignore
        else:
            raise SerializeFailed(lang.require("nbp-uniseg", "invalid_segment").format(type=name, seg=seg))

    @export
    async def reply(self, seg: Reply, bot: Bot) -> "MessageSegment":
        ms = self.segment_class
        if "#" in seg.id:
            _id, _seq = seg.id.split("#", 1)
            return ms.reply(_seq, _id)
        return ms.reply(seg.id)

    @export
    async def reference(self, seg: Reference, bot: Bot) -> "MessageSegment":
        from nonebot.adapters.red.message import ForwardNode

        ms = self.segment_class
        if not seg.content or not isinstance(seg.content, list):
            raise SerializeFailed(lang.require("nbp-uniseg", "invalid_segment").format(type="forward", seg=seg))
        nodes = []
        for node in seg.content:
            if not isinstance(node, CustomNode):
                raise SerializeFailed(lang.require("nbp-uniseg", "invalid_segment").format(type="forward", seg=seg))
            content = self.get_message_type()()
            if isinstance(node.content, str):
                content.extend(self.get_message_type()(node.content))
            elif isinstance(node.content, list):
                content.extend(await self.export(node.content, bot, True))  # type: ignore
            else:
                content.extend(node.content)
            nodes.append(ForwardNode(uin=node.uid, name=node.name, time=node.time, message=content))
        return ms.forward(nodes)

    async def send_to(self, target: Union[Target, Event], bot: Bot, message: Message):
        from nonebot.adapters.red.bot import Bot as RedBot

        assert isinstance(bot, RedBot)
        if TYPE_CHECKING:
            assert isinstance(message, self.get_message_type())

        if isinstance(target, Event):
            target = self.get_target(target, bot)

        if target.private:
            return await bot.send_friend_message(target=target.id, message=message)
        else:
            return await bot.send_group_message(target=target.id, message=message)

    async def recall(self, mid: Any, bot: Bot, context: Union[Target, Event]):
        from nonebot.adapters.red.bot import Bot as RedBot
        from nonebot.adapters.red.api.model import Message as MessageModel

        assert isinstance(bot, RedBot)
        _mid: MessageModel = cast(MessageModel, mid)
        await bot.recall_message(_mid.chatType, _mid.peerUin, _mid.msgId)
        return

    def get_reply(self, mid: Any):
        from nonebot.adapters.red.api.model import Message as MessageModel

        _mid: MessageModel = cast(MessageModel, mid)
        return Reply(f"{_mid.msgId}#{_mid.msgSeq}")
