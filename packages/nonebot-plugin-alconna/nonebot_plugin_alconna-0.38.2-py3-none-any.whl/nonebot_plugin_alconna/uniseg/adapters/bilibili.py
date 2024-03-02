from typing import Union, cast

from nonebot.adapters import Bot, Event, Message, MessageSegment

from ..segment import Text
from ..export import Target, SupportAdapter, MessageExporter, export


class BilibiliMessageExporter(MessageExporter):
    def get_message_type(self):
        from nonebot.adapters.bilibili.message import Message  # type: ignore

        return Message

    @classmethod
    def get_adapter(cls) -> SupportAdapter:
        return SupportAdapter.bilibili

    def get_message_id(self, event: Event) -> str:
        from nonebot.adapters.bilibili.event import MessageEvent  # type: ignore

        assert isinstance(event, MessageEvent)
        return str(event.session_id)  # type: ignore

    @export
    async def text(self, seg: Text, bot: Bot) -> MessageSegment:
        msg = self.get_message_type()
        ms = msg.get_segment_class()  # type: ignore

        return ms.danmu(seg.text)

    async def send_to(self, target: Union[Target, Event], bot: Bot, message: Message):
        from nonebot.adapters.bilibili.adapter import Adapter  # type: ignore

        adapter: Adapter = cast(Adapter, bot.adapter)
        return await adapter.bili.send(str(message), bot.self_id)
