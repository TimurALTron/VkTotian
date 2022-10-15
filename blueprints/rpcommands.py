import typing

from loguru import logger

import sqlManager


from typing import Tuple

from vkbottle.bot import Blueprint, Message
from vkbottle.dispatch.rules.base import CommandRule

bp = Blueprint()

# You can add auto_rules to blueprint labeler:
# bp.labeler.auto_rules.append()
# You can change config for blueprint labeler locally:
bp.labeler.vbml_ignore_case = True


@bp.on.message(CommandRule("ударить", ["!"], 1))
async def say_handler(message: Message, args: Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")

    if(int(sex[0].sex)==1):
        #Eсли девушка
        await message.answer(f"👊| @id{user[0].id} ({user[0].first_name}) ударила с разворота {args[0]}")
    else:
        await message.answer(f"👊| @id{user[0].id} ({user[0].first_name}) ударил с разворота {args[0]}")

@bp.on.message(CommandRule("обнять", ["!"],1))
async def to_embrace(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")

    if (int(sex[0].sex) == 1):
    # Eсли девушка
        if(args[0] == "всех"): await message.answer(f"🤗| @id{user[0].id} ({user[0].first_name}) обняла всех! @all")
        else:
            await message.answer(f"🤗| @id{user[0].id} ({user[0].first_name}) обняла {args[0]}")
    else:
        if (args[0] == "всех"):
            await message.answer(f"🤗| @id{user[0].id} ({user[0].first_name}) обнял всех! @all")
        else:
            await message.answer(f"🤗| @id{user[0].id} ({user[0].first_name}) обнял {args[0]}")


@bp.on.message(CommandRule("убить", ["!"], 1))
async def kill(message: Message, args: Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"💀| @id{user[0].id} ({user[0].first_name}) убила {args[0]}")
    else:
        await message.answer(f"💀| @id{user[0].id} ({user[0].first_name}) убил {args[0]}")


@bp.on.message( text=["!выебать <member>", "!трахнуть <member>"] )
async def viebat(message: Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"👉👌😚| @id{user[0].id} ({user[0].first_name}) принудила к интиму {member}")
    else:
        await message.answer(f"👉👌😚| @id{user[0].id} ({user[0].first_name}) принудил к интиму {member}")


@bp.on.message(CommandRule("изнасиловать", ["!"],1))
async def to_rape(message:Message,args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"👉👌👹| @id{user[0].id} ({user[0].first_name}) изнасиловала {args[0]}")
    else:
        await message.answer(f"👉👌👹| @id{user[0].id} ({user[0].first_name}) изнасиловал {args[0]}") \
 \
@bp.on.message(CommandRule("раздеть", ["!"],1))
async def undress(message:Message,args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"👙😳| @id{user[0].id} ({user[0].first_name}) раздела {args[0]}")
    else:
        await message.answer(f"👙😳| @id{user[0].id} ({user[0].first_name}) раздела {args[0]}")




@bp.on.message(CommandRule("угостить пивком", ["!"], 1))
async def to_give_pivo(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🍻| @id{user[0].id} ({user[0].first_name}) угостила пивком {args[0]}")
    else:
        await message.answer(f"🍻| @id{user[0].id} ({user[0].first_name}) угостил пивком {args[0]}")

@bp.on.message(text=["!отсосать <member>", "!минет <member>"] )
async def otsos(message:Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😳💋🙊| @id{user[0].id} ({user[0].first_name}) отсосала у  {member}")
    else:
        await message.answer(f"😳💋🙊| @id{user[0].id} ({user[0].first_name}) отсосал у  {member}")


@bp.on.message(text=["!отлизать <member>", "!куни <member>"] )
async def otliz(message:Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😳💋😼| @id{user[0].id} ({user[0].first_name}) отлизала  {member}")
    else:

        await message.answer(f"😳💋😼| @id{user[0].id} ({user[0].first_name}) отлизал  {member}")




@bp.on.message(CommandRule("кончить",["!"],1))
async def konchit(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😫💦| @id{user[0].id} ({user[0].first_name}) кончила на  {args[0]}")
    else:
        await message.answer(f"😫💦| @id{user[0].id} ({user[0].first_name}) кончил на  {args[0]}")


@bp.on.message(CommandRule("кастрировать",["!"],1))
async def kastritovat(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😫⚔| @id{user[0].id} ({user[0].first_name}) кастрировала  {args[0]}")
    else:

        await message.answer(f"😫⚔| @id{user[0].id} ({user[0].first_name}) кастрировал  {args[0]}")


@bp.on.message(CommandRule("отдаться",["!"],1))
async def otdatsya(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😫🧕| @id{user[0].id} ({user[0].first_name}) отдалась  {args[0]}")
    else:
        await message.answer(f"😫🧕| @id{user[0].id} ({user[0].first_name}) отдался  {args[0]}")


@bp.on.message(CommandRule("поцеловать",["!"],1))
async def kiss(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)

    await message.answer(f"😽🥰| @id{user[0].id} ({user[0].first_name}) поцеловал до смерти  {args[0]}")


@bp.on.message(text=["!лизнуть <member>", "!лизь <member>"] )
async def otliz(message:Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😳💋| @id{user[0].id} ({user[0].first_name}) лизнула паршивое тело {member}")
    else:

        await message.answer(f"😳💋| @id{user[0].id} ({user[0].first_name}) лизнул паршивое тело {member}")

@bp.on.message(text=["!укусить <member>", "!кусь <member>"] )
async def ukus(message:Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤬😫| @id{user[0].id} ({user[0].first_name}) укусила {member}")
    else:
        await message.answer(f"🤬😫| @id{user[0].id} ({user[0].first_name}) укусила {member}")

@bp.on.message(CommandRule("ущипнуть",["!"],1))
async def kiss(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😽⚔| @id{user[0].id} ({user[0].first_name}) ущипнула  {args[0]}")
    else:

        await message.answer(f"😽⚔| @id{user[0].id} ({user[0].first_name}) ущипнула  {args[0]}")

@bp.on.message(CommandRule("толкнуть",["!"],1))
async def tolknut(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"⚔| @id{user[0].id} ({user[0].first_name}) толкнула с обрыва  {args[0]}")
    else:
        await message.answer(f"⚔| @id{user[0].id} ({user[0].first_name}) толкнула с обрыва  {args[0]}")

@bp.on.message(CommandRule("погладить",["!"],1))
async def pogladit(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😽| @id{user[0].id} ({user[0].first_name}) погладила по тупой бошке {args[0]}")
    else:

        await message.answer(f"😽| @id{user[0].id} ({user[0].first_name}) погладила по тупой бошке {args[0]}")

@bp.on.message(CommandRule("похвалить",["!"],1))
async def pohvalit(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😽🤗| @id{user[0].id} ({user[0].first_name}) похвалила {args[0]}")
    else:
        await message.answer(f"😽🤗| @id{user[0].id} ({user[0].first_name}) похвалила {args[0]}")

@bp.on.message(CommandRule("послать нахуй",["!"],1))
async def FUCKYOU(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤬🤬🤬| @id{user[0].id} ({user[0].first_name}) послала нахуй ебанутого {args[0]}")
    else:
        await message.answer(f"🤬🤬🤬| @id{user[0].id} ({user[0].first_name}) послала нахуй ебанутого {args[0]}")

@bp.on.message(CommandRule("оживить",["!"],1))
async def healme(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"👼❤| @id{user[0].id} ({user[0].first_name}) оживила покойного {args[0]}")
    else:
        await message.answer(f"👼❤| @id{user[0].id} ({user[0].first_name}) оживила покойного {args[0]}")

@bp.on.message(CommandRule("продать на органы", ["!"],1))
async def prodat_na_organy(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"☠❤| @id{user[0].id} ({user[0].first_name}) продала на органы {args[0]}")
    else:
        await message.answer(f"☠❤| @id{user[0].id} ({user[0].first_name}) продала на органы {args[0]}")


@bp.on.message(CommandRule("возбудить", ["!"],1))
async def vozbudit(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😬😏❤| @id{user[0].id} ({user[0].first_name}) возбудила {args[0]}")
    else:
        await message.answer(f"😬😏❤| @id{user[0].id} ({user[0].first_name}) возбудила {args[0]}")



@bp.on.message(CommandRule("прижать", ["!"],1))
async def prizhat(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😬😏❤| @id{user[0].id} ({user[0].first_name}) прижала к углу {args[0]}")
    else:
        await message.answer(f"😬😏❤| @id{user[0].id} ({user[0].first_name}) прижала к углу {args[0]}")

@bp.on.message(CommandRule("засосать", ["!"],1))
async def zasosat(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) засосала {args[0]}")
    else:
        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) засосала {args[0]}")



@bp.on.message(CommandRule("потрогать", ["!"],1))
async def potrogat(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) потрогала нежное тело {args[0]}")
    else:
        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) потрогала нежное тело {args[0]}")


@bp.on.message(CommandRule("шлепнуть", ["!"],1))
async def shlepnut(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) шлепнула по огромной заднице {args[0]}")
    else:
        await message.answer(f"😏❤| @id{user[0].id} ({user[0].first_name}) шлепнула по огромной заднице {args[0]}")


@bp.on.message(CommandRule("пригласить на чай", ["!"],1))
async def priglastiontea(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"☕😎| @id{user[0].id} ({user[0].first_name}) пригласила на чай {args[0]}")
    else:
        await message.answer(f"☕😎| @id{user[0].id} ({user[0].first_name}) пригласила на чай {args[0]}")




@bp.on.message(CommandRule("пожать руку", ["!"],1))
async def pozhatruku(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😎| @id{user[0].id} ({user[0].first_name}) пожала мокрые руки {args[0]}")
    else:
        await message.answer(f"😎| @id{user[0].id} ({user[0].first_name}) пожала мокрые руки {args[0]}")

@bp.on.message(CommandRule("дать пять", ["!"],1))
async def givefive(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😎| @id{user[0].id} ({user[0].first_name}) дала смачную пятерку {args[0]}")
    else:
        await message.answer(f"😎| @id{user[0].id} ({user[0].first_name}) дала смачную пятерку {args[0]}")

@bp.on.message(CommandRule("сжечь", ["!"],1))
async def szheg(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) сожгла в огромном пламени {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) сожгла в огромном пламени {args[0]}")

@bp.on.message(CommandRule("посадить на цепь", ["!"],1))
async def posaditoncep(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) приковала к цепи {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) приковала к цепи {args[0]}")

@bp.on.message(CommandRule("заразить", ["!"],1))
async def zarazit(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) заразила {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) заразила {args[0]}")

@bp.on.message(CommandRule("взглянуть", ["!"],1))
async def vzglyanut(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) взглянула на {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) взглянула на {args[0]}")



@bp.on.message(CommandRule("надеть кольцо", ["!"],1))
async def nadyetcolso(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) надела кольцо на  {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) надела кольцо на  {args[0]}")


@bp.on.message(text=["!усмирить <member>", "!успокоить <member>"] )
async def usmirit(message:Message, member=None):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"😫| @id{user[0].id} ({user[0].first_name}) усмирила и убила {member}")
    else:
        await message.answer(f"😫| @id{user[0].id} ({user[0].first_name}) усмирила и убила {member}")

@bp.on.message(CommandRule("кинуть на кровать", ["!"],1))
async def kinutonbed(message:Message, args:Tuple[str]):
    user = await bp.api.users.get(message.from_id)
    sex = await bp.api.users.get(message.from_id, fields="sex")
    if (int(sex[0].sex) == 1):
    # Eсли девушка

        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) кинула на кровать  {args[0]}")
    else:
        await message.answer(f"🤨| @id{user[0].id} ({user[0].first_name}) кинула на кровать  {getNickMember(args[0])}")



def getNickMember(id):

    nick = sqlManager.getNickMember(id)

    if nick[0] is None:
        textS = f"{id}"

        return textS

    textS = f"@id{nick[1]} ({nick[0]})"
    logger.info(f"{nick[0]}")
    return textS


















