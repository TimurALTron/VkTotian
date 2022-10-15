import sys
import sqlManager


from vkbottle import Bot, load_blueprints_from_package
from vkbottle.bot import Message
from loguru import logger


logger.remove()
logger.add(sys.stderr, level="INFO")

bot = Bot("vk1.a.dOIJU-YB2DOeThI2VvqIFmYxyRNTPa2Lamun3hH5OvlCCaBq1IDXvS1LVU3tdWtvymZC6L4hKUzuPaXZ9j5r8LFE0l3hAWFYySMMQFVMru6K0GmLVlndk2biOUuZcfEEnlZJUYIgLYeWpswUn4HC42XqcyrLPYFggxG6Xj6N4He7nt1w7keY_Ep0BWsH07N2")

for bp in load_blueprints_from_package("blueprints"):
    bp.load(bot)



bot.run_forever()