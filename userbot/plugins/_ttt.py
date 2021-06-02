from . import B, idB
from userbot import catub
from ..core.managers import edit_or_reply as eor

@catub.cat_cmd(pattern=idB['cmd'])
async def _(e):
    await eor(e, idB['rep'].formar(B))
