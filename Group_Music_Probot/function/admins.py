from typing import Dict, List
from Group_Music_Probot.config import admins


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> List[int]:
    return admins[chat_id] if chat_id in admins else []
