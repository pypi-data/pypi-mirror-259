from typing import Union

from nepattern.base import URL, INTEGER
from nepattern import MatchMode, BasePattern, UnionPattern
from nonebot.adapters.onebot.v12.message import MessageSegment

from nonebot_plugin_alconna.typings import SegmentPattern

Text = str
Mention = SegmentPattern("mention", MessageSegment, MessageSegment.mention)
MentionAll = SegmentPattern("mention_all", MessageSegment, MessageSegment.mention_all)
Image = SegmentPattern("image", MessageSegment, MessageSegment.image)
Audio = SegmentPattern("audio", MessageSegment, MessageSegment.audio)
Voice = SegmentPattern("voice", MessageSegment, MessageSegment.voice)
File = SegmentPattern("file", MessageSegment, MessageSegment.file)
Video = SegmentPattern("video", MessageSegment, MessageSegment.video)
Location = SegmentPattern("location", MessageSegment, MessageSegment.location)
Reply = SegmentPattern("reply", MessageSegment, MessageSegment.reply)

ImgOrUrl = (
    UnionPattern(
        [
            BasePattern(
                mode=MatchMode.TYPE_CONVERT,
                origin=str,
                converter=lambda _, x: x.data["url"],
                alias="img",
                addition_accepts=Image,
            ),
            URL,
        ]
    )
    @ "img_url"
)
"""
内置类型, 允许传入图片元素(Image)或者链接(URL)，返回链接
"""

MentionID = (
    UnionPattern[Union[str, MessageSegment]](
        [
            BasePattern(
                mode=MatchMode.TYPE_CONVERT,
                origin=int,
                alias="Mention",
                addition_accepts=Mention,
                converter=lambda _, x: int(x.data["user_id"]),
            ),
            BasePattern(
                r"@(\d+)",
                mode=MatchMode.REGEX_CONVERT,
                origin=int,
                alias="@xxx",
                accepts=str,
                converter=lambda _, x: int(x[1]),
            ),
            INTEGER,
        ]
    )
    @ "mention_id"
)
"""
内置类型，允许传入提醒元素(Mention)或者'@xxxx'式样的字符串或者数字, 返回数字
"""
