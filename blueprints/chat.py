from typing import Tuple

from vkbottle.bot import Blueprint, Message
from vkbottle.dispatch.rules.base import CommandRule

import sqlManager

bp = Blueprint()

# You can add auto_rules to blueprint labeler:
# bp.labeler.auto_rules.append()
# You can change config for blueprint labeler locally:
bp.labeler.vbml_ignore_case = True


@bp.on.message(text=["курить", "покурить", "вкурить"])
async def smoke(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) прикурил малиборо 🚬")


@bp.on.message(text="пиво")
async def pivo(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) хлебнул пивко 🍺")


@bp.on.message(text="вино")
async def vino(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) выпил вино 🍷")


@bp.on.message(text="парить")
async def vape(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) выпарил 20кг никотина 🚬")


@bp.on.message(text="нарко")
async def narko(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) употребил наркоту 🤤")


@bp.on.message(text="соль")
async def salt(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) ебнул соль 🤤")


@bp.on.message(text="ежже")
async def egge(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) ПРОКРИЧАЛ ЕЖЖЕ НА ВСЮ БЕСЕДУ 🦔")


@bp.on.message(text="суицид")
async def suicide(message: Message):
    user = await bp.api.users.get(message.from_id)
    await message.answer(f"@id{user[0].id} ({user[0].first_name}) суициднулся ( NOT PROPOGANTNANDAD)  😡⚔️⚠️")


@bp.on.message(text="test")
async def suicide(message: Message):
    user = await bp.api.users.get(message.from_id)
    # await message.answer(f"@id{user[0].id} ({user[0].first_name}) суициднулся ( NOT PROPOGANTNANDAD)  😡⚔️⚠️")

    await sqlManager.updateUsers(user[0].id, "Tim" ,100)
