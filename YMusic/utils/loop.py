


loop = {}

async def get_loop(chat_id: int) -> int:
    lop = loop.get(chat_id)
    return 0 if not lop else lop


async def set_loop(chat_id: int, mode: int):
    loop[chat_id] = mode