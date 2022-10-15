import sqlite3

from loguru import logger

_DB = None
cursor = None
try:

    _DB = sqlite3.connect("Totian.db")
    cursor = _DB.cursor()
    logger.info(f"Database open.")
except:
    logger.error("Database not open.")


async def updateUsers(id,nick,money):
    logger.info("Updating users...")
    #Code...
    cursor.execute(""" SELECT id FROM users """)
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?)",(id,nick,money,None))
        _DB.commit()
        logger.info(f"Пользователь @id{id} добавлен в бд")
    else:
        logger.info("Такой пользовать уже есть")

def getNickMember(id):
    idT = str(id)
    normId = int(idT[3:-11])
    data = []
    cursor.execute("SELECT Nick FROM users WHERE id =? ", (normId,))

    rs = cursor.fetchone()
    if rs is None:
        data.append("")
        data.append(normId)
        return data
    else:


        data.append(rs[0])
        data.append(normId)
        return data


