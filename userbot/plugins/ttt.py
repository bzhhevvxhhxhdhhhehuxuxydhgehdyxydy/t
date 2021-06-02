from . import B, idB
from userbot import catub
from ..core.managers import edit_or_reply as eor

plugin_category = "fun"

@catub.cat_cmd(
    pattern=idB['cmd'],
    command=(idB['cmd'], plugin_category),
    info={"header": "for test", "usage": "h"},
)
async def _(e):
    await eor(e, idB['rep'].formar(B))
