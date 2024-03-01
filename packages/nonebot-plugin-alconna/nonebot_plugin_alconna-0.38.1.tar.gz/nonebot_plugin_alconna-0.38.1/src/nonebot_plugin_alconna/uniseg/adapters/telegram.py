from pathlib import Path
from typing import TYPE_CHECKING, Any, Union, cast

from tarina import lang
from nonebot.adapters import Bot, Event, Message

from ..segment import At, File, Text, Audio, Emoji, Image, Reply, Video, Voice
from ..export import Target, SupportAdapter, MessageExporter, SerializeFailed, export

if TYPE_CHECKING:
    from nonebot.adapters.telegram.message import MessageSegment


class TelegramMessageExporter(MessageExporter["MessageSegment"]):
    def get_message_type(self):
        from nonebot.adapters.telegram.message import Message

        return Message

    @classmethod
    def get_adapter(cls) -> SupportAdapter:
        return SupportAdapter.telegram

    def get_target(self, event: Event, bot: Union[Bot, None] = None) -> Target:
        from nonebot.adapters.telegram.event import EventWithChat

        assert isinstance(event, EventWithChat)
        return Target(str(event.chat.id), platform=self.get_adapter(), self_id=bot.self_id if bot else None)

    def get_message_id(self, event: Event) -> str:
        from nonebot.adapters.telegram.event import MessageEvent

        assert isinstance(event, MessageEvent)
        return f"{event.message_id}"

    @export
    async def text(self, seg: Text, bot: Bot) -> "MessageSegment":
        from nonebot.adapters.telegram.message import Entity

        if not seg.style:
            return Entity.text(seg.text)
        else:
            return Entity(seg.style, {"text": seg.text})

    @export
    async def at(self, seg: At, bot: Bot) -> "MessageSegment":
        from nonebot.adapters.telegram.message import Entity

        return (
            Entity.mention(f"{seg.target} ")
            if seg.target.startswith("@")
            else Entity.text_link("用户 ", f"tg://user?id={seg.target}")
        )

    @export
    async def emoji(self, seg: Emoji, bot: Bot) -> "MessageSegment":
        from nonebot.adapters.telegram.message import Entity

        return Entity.custom_emoji(seg.name, seg.id)  # type: ignore

    @export
    async def media(self, seg: Union[Image, Voice, Video, Audio, File], bot: Bot) -> "MessageSegment":
        from nonebot.adapters.telegram.message import File as TgFile

        name = seg.__class__.__name__.lower()
        method = {
            "image": TgFile.photo,
            "voice": TgFile.voice,
            "video": TgFile.video,
            "audio": TgFile.audio,
            "file": TgFile.document,
        }[name]
        if seg.id or seg.url:
            return method(seg.id or seg.url)
        elif seg.path:
            return method(Path(seg.path).read_bytes())
        elif seg.raw:
            return method(seg.raw_bytes)
        else:
            raise SerializeFailed(lang.require("nbp-uniseg", "invalid_segment").format(type=name, seg=seg))

    @export
    async def reply(self, seg: Reply, bot: Bot) -> "MessageSegment":
        from nonebot.adapters.telegram.message import Reply as TgReply

        return TgReply.reply(int(seg.id))

    async def send_to(self, target: Union[Target, Event], bot: Bot, message: Message):
        from nonebot.adapters.telegram.bot import Bot as TgBot
        from nonebot.adapters.telegram.event import Event as TgEvent
        from nonebot.adapters.telegram.message import Message as TgMessage

        assert isinstance(bot, TgBot)
        assert isinstance(message, TgMessage)
        if isinstance(target, Event):
            assert isinstance(target, TgEvent)
            return await bot.send(event=target, message=message)
        return await bot.send_to(target.id, message)

    async def recall(self, mid: Any, bot: Bot, context: Union[Target, Event]):
        from nonebot.adapters.telegram.bot import Bot as TgBot
        from nonebot.adapters.telegram.model import Message as MessageModel

        assert isinstance(bot, TgBot)
        _mid: MessageModel = cast(MessageModel, mid)
        await bot.delete_message(chat_id=_mid.chat.id, message_id=_mid.message_id)

    async def edit(self, new: Message, mid: Any, bot: Bot, context: Union[Target, Event]):
        from nonebot.adapters.telegram.bot import Bot as TgBot
        from nonebot.adapters.telegram.model import Message as MessageModel

        assert isinstance(bot, TgBot)
        _mid: MessageModel = cast(MessageModel, mid)
        text = new.extract_plain_text()
        res = await bot.edit_message_text(text=text, chat_id=_mid.chat.id, message_id=_mid.message_id)
        if isinstance(res, MessageModel):
            return res

    def get_reply(self, mid: Any):
        from nonebot.adapters.telegram.model import Message as MessageModel

        _mid: MessageModel = cast(MessageModel, mid)
        return Reply(str(_mid.message_id))
