from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Type, cast

from nonebot.adapters import Bot as BaseBot
from nonebot.message import event_postprocessor
from nonebot_plugin_orm import get_session
from nonebot_plugin_session import Session, SessionLevel, extract_session
from nonebot_plugin_session_orm import get_session_persist_id
from typing_extensions import override

from ..config import plugin_config
from ..consts import SupportedAdapter, SupportedPlatform
from ..message import (
    MessageDeserializer,
    MessageSerializer,
    register_deserializer,
    register_serializer,
    serialize_message,
)
from ..model import MessageRecord
from ..utils import remove_timezone

try:
    from nonebot.adapters.satori import Bot, Message, MessageEvent
    from nonebot.adapters.satori.models import InnerMessage as SatoriMessage

    adapter = SupportedAdapter.satori

    @event_postprocessor
    async def record_recv_msg(bot: Bot, event: MessageEvent):
        session = extract_session(bot, event)
        session_persist_id = await get_session_persist_id(session)

        record = MessageRecord(
            session_persist_id=session_persist_id,
            time=remove_timezone(event.timestamp.astimezone(timezone.utc)),
            type=event.get_type(),
            message_id=event.message.id,
            message=serialize_message(adapter, event.get_message()),
            plain_text=event.get_plaintext(),
        )
        async with get_session() as db_session:
            db_session.add(record)
            await db_session.commit()

    if plugin_config.chatrecorder_record_send_msg:

        @Bot.on_called_api
        async def record_send_msg(
            bot: BaseBot,
            e: Optional[Exception],
            api: str,
            data: Dict[str, Any],
            result: Optional[Any],
        ):
            if not isinstance(bot, Bot):
                return
            if e or not result or not isinstance(result, list):
                return
            if api not in ["message_create"]:
                return
            for res in result:
                if not isinstance(res, SatoriMessage):
                    return
            result_messages = cast(List[SatoriMessage], result)

            result_message = result_messages[0]
            level = SessionLevel.LEVEL0
            if result_message.guild:
                level = SessionLevel.LEVEL3
            elif result_message.member:
                level = SessionLevel.LEVEL2
            elif result_message.user:
                level = SessionLevel.LEVEL1
            id1 = data["channel_id"] if level == SessionLevel.LEVEL1 else None
            id2 = result_message.channel.id if result_message.channel else None
            id3 = result_message.guild.id if result_message.guild else None

            platform = bot.platform
            if platform in ("onebot", "red", "chronocat"):
                platform = SupportedPlatform.qq
            elif platform in ("kook",):
                platform = SupportedPlatform.kaiheila
            elif platform not in list(SupportedPlatform):
                platform = SupportedPlatform.unknown

            session = Session(
                bot_id=bot.self_id,
                bot_type=bot.type,
                platform=platform,
                level=level,
                id1=id1,
                id2=id2,
                id3=id3,
            )
            session_persist_id = await get_session_persist_id(session)

            message_id = "_".join([msg.id for msg in result_messages])
            message = Message()
            for msg in result_messages:
                message += Message.from_satori_element(msg.content)
            message_time = (
                remove_timezone(result_message.created_at.astimezone(timezone.utc))
                if result_message.created_at
                else datetime.utcnow()
            )

            record = MessageRecord(
                session_persist_id=session_persist_id,
                time=message_time,
                type="message_sent",
                message_id=message_id,
                message=serialize_message(adapter, message),
                plain_text=message.extract_plain_text(),
            )
            async with get_session() as db_session:
                db_session.add(record)
                await db_session.commit()

    class Serializer(MessageSerializer[Message]):
        pass

    class Deserializer(MessageDeserializer[Message]):
        @classmethod
        @override
        def get_message_class(cls) -> Type[Message]:
            return Message

    register_serializer(adapter, Serializer)
    register_deserializer(adapter, Deserializer)

except ImportError:
    pass
