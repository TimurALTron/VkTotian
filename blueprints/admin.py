from vkbottle.bot import Blueprint, Message, rules

bp = Blueprint("for admin commands")
bp.labeler.auto_rules = [rules.FromPeerRule(518090077)] # Допустим, вы являетесь Павлом Дуровым

@bp.on.message(command="halt")
async def halt(_):
    exit(0)
