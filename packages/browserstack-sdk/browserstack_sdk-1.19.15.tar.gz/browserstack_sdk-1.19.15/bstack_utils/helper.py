# coding: UTF-8
import sys
bstack1l1l11_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1ll1ll_opy_ = 7
def bstack1l111l1_opy_ (bstack1ll1lll_opy_):
    global bstack1lll1l1_opy_
    bstack1ll1ll1_opy_ = ord (bstack1ll1lll_opy_ [-1])
    bstack1111l1_opy_ = bstack1ll1lll_opy_ [:-1]
    bstack11l1ll_opy_ = bstack1ll1ll1_opy_ % len (bstack1111l1_opy_)
    bstack1l11l1l_opy_ = bstack1111l1_opy_ [:bstack11l1ll_opy_] + bstack1111l1_opy_ [bstack11l1ll_opy_:]
    if bstack1l1l11_opy_:
        bstack111ll11_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11l1_opy_ + bstack1ll1ll1_opy_) % bstack1ll1ll_opy_) for bstack11l1_opy_, char in enumerate (bstack1l11l1l_opy_)])
    else:
        bstack111ll11_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11l1_opy_ + bstack1ll1ll1_opy_) % bstack1ll1ll_opy_) for bstack11l1_opy_, char in enumerate (bstack1l11l1l_opy_)])
    return eval (bstack111ll11_opy_)
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack11l1l111l1_opy_, bstack11l1lll1l_opy_, bstack1111l1l11_opy_, bstack1l11l1ll_opy_
from bstack_utils.messages import bstack1l1111ll1_opy_, bstack1l1ll11111_opy_
from bstack_utils.proxy import bstack1l1ll1ll_opy_, bstack1l11l1ll1l_opy_
bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
def bstack11l1llll11_opy_(config):
    return config[bstack1l111l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᅻ")]
def bstack11ll11l1ll_opy_(config):
    return config[bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᅼ")]
def bstack1l1lll1lll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l11ll1l1_opy_(obj):
    values = []
    bstack111llll11l_opy_ = re.compile(bstack1l111l1_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᅽ"), re.I)
    for key in obj.keys():
        if bstack111llll11l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11l11lll11_opy_(config):
    tags = []
    tags.extend(bstack11l11ll1l1_opy_(os.environ))
    tags.extend(bstack11l11ll1l1_opy_(config))
    return tags
def bstack11l11l111l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111ll1lll1_opy_(bstack11l111llll_opy_):
    if not bstack11l111llll_opy_:
        return bstack1l111l1_opy_ (u"ࠬ࠭ᅾ")
    return bstack1l111l1_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᅿ").format(bstack11l111llll_opy_.name, bstack11l111llll_opy_.email)
def bstack11ll1l1111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11l111lll1_opy_ = repo.common_dir
        info = {
            bstack1l111l1_opy_ (u"ࠢࡴࡪࡤࠦᆀ"): repo.head.commit.hexsha,
            bstack1l111l1_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᆁ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l111l1_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᆂ"): repo.active_branch.name,
            bstack1l111l1_opy_ (u"ࠥࡸࡦ࡭ࠢᆃ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l111l1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᆄ"): bstack111ll1lll1_opy_(repo.head.commit.committer),
            bstack1l111l1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᆅ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l111l1_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᆆ"): bstack111ll1lll1_opy_(repo.head.commit.author),
            bstack1l111l1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᆇ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l111l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᆈ"): repo.head.commit.message,
            bstack1l111l1_opy_ (u"ࠤࡵࡳࡴࡺࠢᆉ"): repo.git.rev_parse(bstack1l111l1_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᆊ")),
            bstack1l111l1_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᆋ"): bstack11l111lll1_opy_,
            bstack1l111l1_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᆌ"): subprocess.check_output([bstack1l111l1_opy_ (u"ࠨࡧࡪࡶࠥᆍ"), bstack1l111l1_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᆎ"), bstack1l111l1_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᆏ")]).strip().decode(
                bstack1l111l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᆐ")),
            bstack1l111l1_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᆑ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l111l1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᆒ"): repo.git.rev_list(
                bstack1l111l1_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᆓ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l11l11l1_opy_ = []
        for remote in remotes:
            bstack111ll1ll11_opy_ = {
                bstack1l111l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆔ"): remote.name,
                bstack1l111l1_opy_ (u"ࠢࡶࡴ࡯ࠦᆕ"): remote.url,
            }
            bstack11l11l11l1_opy_.append(bstack111ll1ll11_opy_)
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᆖ"): bstack1l111l1_opy_ (u"ࠤࡪ࡭ࡹࠨᆗ"),
            **info,
            bstack1l111l1_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᆘ"): bstack11l11l11l1_opy_
        }
    except Exception as err:
        print(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᆙ").format(err))
        return {}
def bstack11111l11l_opy_():
    env = os.environ
    if (bstack1l111l1_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᆚ") in env and len(env[bstack1l111l1_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᆛ")]) > 0) or (
            bstack1l111l1_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᆜ") in env and len(env[bstack1l111l1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᆝ")]) > 0):
        return {
            bstack1l111l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆞ"): bstack1l111l1_opy_ (u"ࠥࡎࡪࡴ࡫ࡪࡰࡶࠦᆟ"),
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᆠ"): env.get(bstack1l111l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᆡ")),
            bstack1l111l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᆢ"): env.get(bstack1l111l1_opy_ (u"ࠢࡋࡑࡅࡣࡓࡇࡍࡆࠤᆣ")),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᆤ"): env.get(bstack1l111l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᆥ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠥࡇࡎࠨᆦ")) == bstack1l111l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᆧ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡈࡏࠢᆨ"))):
        return {
            bstack1l111l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆩ"): bstack1l111l1_opy_ (u"ࠢࡄ࡫ࡵࡧࡱ࡫ࡃࡊࠤᆪ"),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᆫ"): env.get(bstack1l111l1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᆬ")),
            bstack1l111l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᆭ"): env.get(bstack1l111l1_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡏࡕࡂࠣᆮ")),
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᆯ"): env.get(bstack1l111l1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠤᆰ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠢࡄࡋࠥᆱ")) == bstack1l111l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᆲ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࠤᆳ"))):
        return {
            bstack1l111l1_opy_ (u"ࠥࡲࡦࡳࡥࠣᆴ"): bstack1l111l1_opy_ (u"࡙ࠦࡸࡡࡷ࡫ࡶࠤࡈࡏࠢᆵ"),
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᆶ"): env.get(bstack1l111l1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤ࡝ࡅࡃࡡࡘࡖࡑࠨᆷ")),
            bstack1l111l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᆸ"): env.get(bstack1l111l1_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᆹ")),
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᆺ"): env.get(bstack1l111l1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᆻ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠦࡈࡏࠢᆼ")) == bstack1l111l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᆽ") and env.get(bstack1l111l1_opy_ (u"ࠨࡃࡊࡡࡑࡅࡒࡋࠢᆾ")) == bstack1l111l1_opy_ (u"ࠢࡤࡱࡧࡩࡸ࡮ࡩࡱࠤᆿ"):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇀ"): bstack1l111l1_opy_ (u"ࠤࡆࡳࡩ࡫ࡳࡩ࡫ࡳࠦᇁ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᇂ"): None,
            bstack1l111l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇃ"): None,
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᇄ"): None
        }
    if env.get(bstack1l111l1_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅࡖࡆࡔࡃࡉࠤᇅ")) and env.get(bstack1l111l1_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡇࡔࡓࡍࡊࡖࠥᇆ")):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇇ"): bstack1l111l1_opy_ (u"ࠤࡅ࡭ࡹࡨࡵࡤ࡭ࡨࡸࠧᇈ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᇉ"): env.get(bstack1l111l1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡈࡋࡗࡣࡍ࡚ࡔࡑࡡࡒࡖࡎࡍࡉࡏࠤᇊ")),
            bstack1l111l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᇋ"): None,
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇌ"): env.get(bstack1l111l1_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᇍ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠣࡅࡌࠦᇎ")) == bstack1l111l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᇏ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠥࡈࡗࡕࡎࡆࠤᇐ"))):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇑ"): bstack1l111l1_opy_ (u"ࠧࡊࡲࡰࡰࡨࠦᇒ"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇓ"): env.get(bstack1l111l1_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡒࡉࡏࡍࠥᇔ")),
            bstack1l111l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇕ"): None,
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇖ"): env.get(bstack1l111l1_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᇗ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠦࡈࡏࠢᇘ")) == bstack1l111l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᇙ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࠤᇚ"))):
        return {
            bstack1l111l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇛ"): bstack1l111l1_opy_ (u"ࠣࡕࡨࡱࡦࡶࡨࡰࡴࡨࠦᇜ"),
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇝ"): env.get(bstack1l111l1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡏࡓࡉࡄࡒࡎࡠࡁࡕࡋࡒࡒࡤ࡛ࡒࡍࠤᇞ")),
            bstack1l111l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇟ"): env.get(bstack1l111l1_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᇠ")),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇡ"): env.get(bstack1l111l1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠥᇢ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠣࡅࡌࠦᇣ")) == bstack1l111l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᇤ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠥࡋࡎ࡚ࡌࡂࡄࡢࡇࡎࠨᇥ"))):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇦ"): bstack1l111l1_opy_ (u"ࠧࡍࡩࡵࡎࡤࡦࠧᇧ"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇨ"): env.get(bstack1l111l1_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡖࡔࡏࠦᇩ")),
            bstack1l111l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇪ"): env.get(bstack1l111l1_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᇫ")),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᇬ"): env.get(bstack1l111l1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠢᇭ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠧࡉࡉࠣᇮ")) == bstack1l111l1_opy_ (u"ࠨࡴࡳࡷࡨࠦᇯ") and bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࠥᇰ"))):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇱ"): bstack1l111l1_opy_ (u"ࠤࡅࡹ࡮ࡲࡤ࡬࡫ࡷࡩࠧᇲ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᇳ"): env.get(bstack1l111l1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᇴ")),
            bstack1l111l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᇵ"): env.get(bstack1l111l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡏࡅࡇࡋࡌࠣᇶ")) or env.get(bstack1l111l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᇷ")),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇸ"): env.get(bstack1l111l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᇹ"))
        }
    if bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᇺ"))):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇻ"): bstack1l111l1_opy_ (u"ࠧ࡜ࡩࡴࡷࡤࡰ࡙ࠥࡴࡶࡦ࡬ࡳ࡚ࠥࡥࡢ࡯ࠣࡗࡪࡸࡶࡪࡥࡨࡷࠧᇼ"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇽ"): bstack1l111l1_opy_ (u"ࠢࡼࡿࡾࢁࠧᇾ").format(env.get(bstack1l111l1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᇿ")), env.get(bstack1l111l1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࡉࡅࠩሀ"))),
            bstack1l111l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሁ"): env.get(bstack1l111l1_opy_ (u"ࠦࡘ࡟ࡓࡕࡇࡐࡣࡉࡋࡆࡊࡐࡌࡘࡎࡕࡎࡊࡆࠥሂ")),
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሃ"): env.get(bstack1l111l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨሄ"))
        }
    if bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࠤህ"))):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨሆ"): bstack1l111l1_opy_ (u"ࠤࡄࡴࡵࡼࡥࡺࡱࡵࠦሇ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨለ"): bstack1l111l1_opy_ (u"ࠦࢀࢃ࠯ࡱࡴࡲ࡮ࡪࡩࡴ࠰ࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠥሉ").format(env.get(bstack1l111l1_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡖࡔࡏࠫሊ")), env.get(bstack1l111l1_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡃࡆࡇࡔ࡛ࡎࡕࡡࡑࡅࡒࡋࠧላ")), env.get(bstack1l111l1_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡓࡖࡔࡐࡅࡄࡖࡢࡗࡑ࡛ࡇࠨሌ")), env.get(bstack1l111l1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬል"))),
            bstack1l111l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦሎ"): env.get(bstack1l111l1_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢሏ")),
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሐ"): env.get(bstack1l111l1_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨሑ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠨࡁ࡛ࡗࡕࡉࡤࡎࡔࡕࡒࡢ࡙ࡘࡋࡒࡠࡃࡊࡉࡓ࡚ࠢሒ")) and env.get(bstack1l111l1_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤሓ")):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨሔ"): bstack1l111l1_opy_ (u"ࠤࡄࡾࡺࡸࡥࠡࡅࡌࠦሕ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨሖ"): bstack1l111l1_opy_ (u"ࠦࢀࢃࡻࡾ࠱ࡢࡦࡺ࡯࡬ࡥ࠱ࡵࡩࡸࡻ࡬ࡵࡵࡂࡦࡺ࡯࡬ࡥࡋࡧࡁࢀࢃࠢሗ").format(env.get(bstack1l111l1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨመ")), env.get(bstack1l111l1_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࠫሙ")), env.get(bstack1l111l1_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠧሚ"))),
            bstack1l111l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥማ"): env.get(bstack1l111l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤሜ")),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤም"): env.get(bstack1l111l1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦሞ"))
        }
    if any([env.get(bstack1l111l1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥሟ")), env.get(bstack1l111l1_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡕࡉࡘࡕࡌࡗࡇࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧሠ")), env.get(bstack1l111l1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦሡ"))]):
        return {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨሢ"): bstack1l111l1_opy_ (u"ࠤࡄ࡛ࡘࠦࡃࡰࡦࡨࡆࡺ࡯࡬ࡥࠤሣ"),
            bstack1l111l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨሤ"): env.get(bstack1l111l1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡑࡗࡅࡐࡎࡉ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥሥ")),
            bstack1l111l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢሦ"): env.get(bstack1l111l1_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦሧ")),
            bstack1l111l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨረ"): env.get(bstack1l111l1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨሩ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢሪ")):
        return {
            bstack1l111l1_opy_ (u"ࠥࡲࡦࡳࡥࠣራ"): bstack1l111l1_opy_ (u"ࠦࡇࡧ࡭ࡣࡱࡲࠦሬ"),
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣር"): env.get(bstack1l111l1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡗ࡫ࡳࡶ࡮ࡷࡷ࡚ࡸ࡬ࠣሮ")),
            bstack1l111l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤሯ"): env.get(bstack1l111l1_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡵ࡫ࡳࡷࡺࡊࡰࡤࡑࡥࡲ࡫ࠢሰ")),
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣሱ"): env.get(bstack1l111l1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣሲ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࠧሳ")) or env.get(bstack1l111l1_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢሴ")):
        return {
            bstack1l111l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦስ"): bstack1l111l1_opy_ (u"ࠢࡘࡧࡵࡧࡰ࡫ࡲࠣሶ"),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦሷ"): env.get(bstack1l111l1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨሸ")),
            bstack1l111l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሹ"): bstack1l111l1_opy_ (u"ࠦࡒࡧࡩ࡯ࠢࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠦሺ") if env.get(bstack1l111l1_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢሻ")) else None,
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧሼ"): env.get(bstack1l111l1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡉࡌࡘࡤࡉࡏࡎࡏࡌࡘࠧሽ"))
        }
    if any([env.get(bstack1l111l1_opy_ (u"ࠣࡉࡆࡔࡤࡖࡒࡐࡌࡈࡇ࡙ࠨሾ")), env.get(bstack1l111l1_opy_ (u"ࠤࡊࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥሿ")), env.get(bstack1l111l1_opy_ (u"ࠥࡋࡔࡕࡇࡍࡇࡢࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥቀ"))]):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤቁ"): bstack1l111l1_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡉ࡬ࡰࡷࡧࠦቂ"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤቃ"): None,
            bstack1l111l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤቄ"): env.get(bstack1l111l1_opy_ (u"ࠣࡒࡕࡓࡏࡋࡃࡕࡡࡌࡈࠧቅ")),
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቆ"): env.get(bstack1l111l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧቇ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋࠢቈ")):
        return {
            bstack1l111l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ቉"): bstack1l111l1_opy_ (u"ࠨࡓࡩ࡫ࡳࡴࡦࡨ࡬ࡦࠤቊ"),
            bstack1l111l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥቋ"): env.get(bstack1l111l1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢቌ")),
            bstack1l111l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቍ"): bstack1l111l1_opy_ (u"ࠥࡎࡴࡨࠠࠤࡽࢀࠦ቎").format(env.get(bstack1l111l1_opy_ (u"ࠫࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠧ቏"))) if env.get(bstack1l111l1_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠣቐ")) else None,
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧቑ"): env.get(bstack1l111l1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤቒ"))
        }
    if bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠣࡐࡈࡘࡑࡏࡆ࡚ࠤቓ"))):
        return {
            bstack1l111l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቔ"): bstack1l111l1_opy_ (u"ࠥࡒࡪࡺ࡬ࡪࡨࡼࠦቕ"),
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቖ"): env.get(bstack1l111l1_opy_ (u"ࠧࡊࡅࡑࡎࡒ࡝ࡤ࡛ࡒࡍࠤ቗")),
            bstack1l111l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቘ"): env.get(bstack1l111l1_opy_ (u"ࠢࡔࡋࡗࡉࡤࡔࡁࡎࡇࠥ቙")),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢቚ"): env.get(bstack1l111l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦቛ"))
        }
    if bstack1l1l1ll111_opy_(env.get(bstack1l111l1_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡅࡈ࡚ࡉࡐࡐࡖࠦቜ"))):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤቝ"): bstack1l111l1_opy_ (u"ࠧࡍࡩࡵࡊࡸࡦࠥࡇࡣࡵ࡫ࡲࡲࡸࠨ቞"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ቟"): bstack1l111l1_opy_ (u"ࠢࡼࡿ࠲ࡿࢂ࠵ࡡࡤࡶ࡬ࡳࡳࡹ࠯ࡳࡷࡱࡷ࠴ࢁࡽࠣበ").format(env.get(bstack1l111l1_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡕࡈࡖ࡛ࡋࡒࡠࡗࡕࡐࠬቡ")), env.get(bstack1l111l1_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕࡉࡕࡕࡓࡊࡖࡒࡖ࡞࠭ቢ")), env.get(bstack1l111l1_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠪባ"))),
            bstack1l111l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨቤ"): env.get(bstack1l111l1_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤ࡝ࡏࡓࡍࡉࡐࡔ࡝ࠢብ")),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧቦ"): env.get(bstack1l111l1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠢቧ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠣࡅࡌࠦቨ")) == bstack1l111l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢቩ") and env.get(bstack1l111l1_opy_ (u"࡚ࠥࡊࡘࡃࡆࡎࠥቪ")) == bstack1l111l1_opy_ (u"ࠦ࠶ࠨቫ"):
        return {
            bstack1l111l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥቬ"): bstack1l111l1_opy_ (u"ࠨࡖࡦࡴࡦࡩࡱࠨቭ"),
            bstack1l111l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥቮ"): bstack1l111l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡽࢀࠦቯ").format(env.get(bstack1l111l1_opy_ (u"࡙ࠩࡉࡗࡉࡅࡍࡡࡘࡖࡑ࠭ተ"))),
            bstack1l111l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቱ"): None,
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥቲ"): None,
        }
    if env.get(bstack1l111l1_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡗࡇࡕࡗࡎࡕࡎࠣታ")):
        return {
            bstack1l111l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦቴ"): bstack1l111l1_opy_ (u"ࠢࡕࡧࡤࡱࡨ࡯ࡴࡺࠤት"),
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦቶ"): None,
            bstack1l111l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቷ"): env.get(bstack1l111l1_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠦቸ")),
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥቹ"): env.get(bstack1l111l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦቺ"))
        }
    if any([env.get(bstack1l111l1_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࠤቻ")), env.get(bstack1l111l1_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡗࡒࠢቼ")), env.get(bstack1l111l1_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨች")), env.get(bstack1l111l1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡚ࡅࡂࡏࠥቾ"))]):
        return {
            bstack1l111l1_opy_ (u"ࠥࡲࡦࡳࡥࠣቿ"): bstack1l111l1_opy_ (u"ࠦࡈࡵ࡮ࡤࡱࡸࡶࡸ࡫ࠢኀ"),
            bstack1l111l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣኁ"): None,
            bstack1l111l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣኂ"): env.get(bstack1l111l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣኃ")) or None,
            bstack1l111l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢኄ"): env.get(bstack1l111l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦኅ"), 0)
        }
    if env.get(bstack1l111l1_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣኆ")):
        return {
            bstack1l111l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤኇ"): bstack1l111l1_opy_ (u"ࠧࡍ࡯ࡄࡆࠥኈ"),
            bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ኉"): None,
            bstack1l111l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤኊ"): env.get(bstack1l111l1_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨኋ")),
            bstack1l111l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣኌ"): env.get(bstack1l111l1_opy_ (u"ࠥࡋࡔࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡅࡒ࡙ࡓ࡚ࡅࡓࠤኍ"))
        }
    if env.get(bstack1l111l1_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ኎")):
        return {
            bstack1l111l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ኏"): bstack1l111l1_opy_ (u"ࠨࡃࡰࡦࡨࡊࡷ࡫ࡳࡩࠤነ"),
            bstack1l111l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥኑ"): env.get(bstack1l111l1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢኒ")),
            bstack1l111l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦና"): env.get(bstack1l111l1_opy_ (u"ࠥࡇࡋࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨኔ")),
            bstack1l111l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥን"): env.get(bstack1l111l1_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥኖ"))
        }
    return {bstack1l111l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧኗ"): None}
def get_host_info():
    return {
        bstack1l111l1_opy_ (u"ࠢࡩࡱࡶࡸࡳࡧ࡭ࡦࠤኘ"): platform.node(),
        bstack1l111l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥኙ"): platform.system(),
        bstack1l111l1_opy_ (u"ࠤࡷࡽࡵ࡫ࠢኚ"): platform.machine(),
        bstack1l111l1_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦኛ"): platform.version(),
        bstack1l111l1_opy_ (u"ࠦࡦࡸࡣࡩࠤኜ"): platform.architecture()[0]
    }
def bstack1l1111l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11l11l1lll_opy_():
    if bstack11111111_opy_.get_property(bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ኝ")):
        return bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬኞ")
    return bstack1l111l1_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩ࠭ኟ")
def bstack11l111111l_opy_(driver):
    info = {
        bstack1l111l1_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧአ"): driver.capabilities,
        bstack1l111l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ኡ"): driver.session_id,
        bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫኢ"): driver.capabilities.get(bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩኣ"), None),
        bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧኤ"): driver.capabilities.get(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧእ"), None),
        bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩኦ"): driver.capabilities.get(bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧኧ"), None),
    }
    if bstack11l11l1lll_opy_() == bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨከ"):
        info[bstack1l111l1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫኩ")] = bstack1l111l1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪኪ") if bstack1ll1llll11_opy_() else bstack1l111l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧካ")
    return info
def bstack1ll1llll11_opy_():
    if bstack11111111_opy_.get_property(bstack1l111l1_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬኬ")):
        return True
    if bstack1l1l1ll111_opy_(os.environ.get(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨክ"), None)):
        return True
    return False
def bstack1ll1llll1_opy_(bstack111lllll1l_opy_, url, data, config):
    headers = config.get(bstack1l111l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩኮ"), None)
    proxies = bstack1l1ll1ll_opy_(config, url)
    auth = config.get(bstack1l111l1_opy_ (u"ࠩࡤࡹࡹ࡮ࠧኯ"), None)
    response = requests.request(
            bstack111lllll1l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l111l1l_opy_(bstack111l1llll_opy_, size):
    bstack1ll11l11_opy_ = []
    while len(bstack111l1llll_opy_) > size:
        bstack1ll1l11l_opy_ = bstack111l1llll_opy_[:size]
        bstack1ll11l11_opy_.append(bstack1ll1l11l_opy_)
        bstack111l1llll_opy_ = bstack111l1llll_opy_[size:]
    bstack1ll11l11_opy_.append(bstack111l1llll_opy_)
    return bstack1ll11l11_opy_
def bstack11l111l11l_opy_(message, bstack11l111l111_opy_=False):
    os.write(1, bytes(message, bstack1l111l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩኰ")))
    os.write(1, bytes(bstack1l111l1_opy_ (u"ࠫࡡࡴࠧ኱"), bstack1l111l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫኲ")))
    if bstack11l111l111_opy_:
        with open(bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬኳ") + os.environ[bstack1l111l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ኴ")] + bstack1l111l1_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ኵ"), bstack1l111l1_opy_ (u"ࠩࡤࠫ኶")) as f:
            f.write(message + bstack1l111l1_opy_ (u"ࠪࡠࡳ࠭኷"))
def bstack11l11l1111_opy_():
    return os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧኸ")].lower() == bstack1l111l1_opy_ (u"ࠬࡺࡲࡶࡧࠪኹ")
def bstack1l1ll1l1l_opy_(bstack111lll1l11_opy_):
    return bstack1l111l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬኺ").format(bstack11l1l111l1_opy_, bstack111lll1l11_opy_)
def bstack1lll11llll_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"࡛ࠧࠩኻ")
def bstack11l1111ll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l111l1_opy_ (u"ࠨ࡜ࠪኼ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l111l1_opy_ (u"ࠩ࡝ࠫኽ")))).total_seconds() * 1000
def bstack11l11l1l1l_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack1l111l1_opy_ (u"ࠪ࡞ࠬኾ")
def bstack111llll1l1_opy_(bstack11l11lllll_opy_):
    date_format = bstack1l111l1_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩ኿")
    bstack11l111l1l1_opy_ = datetime.datetime.strptime(bstack11l11lllll_opy_, date_format)
    return bstack11l111l1l1_opy_.isoformat() + bstack1l111l1_opy_ (u"ࠬࡠࠧዀ")
def bstack11l11l1ll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭዁")
    else:
        return bstack1l111l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧዂ")
def bstack1l1l1ll111_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l111l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ዃ")
def bstack111lll1111_opy_(val):
    return val.__str__().lower() == bstack1l111l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨዄ")
def bstack1l1111lll1_opy_(bstack111llll1ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111llll1ll_opy_ as e:
                print(bstack1l111l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥዅ").format(func.__name__, bstack111llll1ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l111ll1l_opy_(bstack11l1111111_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11l1111111_opy_(cls, *args, **kwargs)
            except bstack111llll1ll_opy_ as e:
                print(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦ዆").format(bstack11l1111111_opy_.__name__, bstack111llll1ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l111ll1l_opy_
    else:
        return decorator
def bstack1ll1l1ll1l_opy_(bstack11lll11l1l_opy_):
    if bstack1l111l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ዇") in bstack11lll11l1l_opy_ and bstack111lll1111_opy_(bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪወ")]):
        return False
    if bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩዉ") in bstack11lll11l1l_opy_ and bstack111lll1111_opy_(bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪዊ")]):
        return False
    return True
def bstack1lll11l1l_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack11ll1l1l1_opy_(hub_url):
    if bstack1l1ll11lll_opy_() <= version.parse(bstack1l111l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩዋ")):
        if hub_url != bstack1l111l1_opy_ (u"ࠪࠫዌ"):
            return bstack1l111l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧው") + hub_url + bstack1l111l1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤዎ")
        return bstack1111l1l11_opy_
    if hub_url != bstack1l111l1_opy_ (u"࠭ࠧዏ"):
        return bstack1l111l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤዐ") + hub_url + bstack1l111l1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤዑ")
    return bstack1l11l1ll_opy_
def bstack111lllllll_opy_():
    return isinstance(os.getenv(bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨዒ")), str)
def bstack11ll1ll1l_opy_(url):
    return urlparse(url).hostname
def bstack11l1l1l1l_opy_(hostname):
    for bstack1ll11lll1l_opy_ in bstack11l1lll1l_opy_:
        regex = re.compile(bstack1ll11lll1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111lllll11_opy_(bstack11l111l1ll_opy_, file_name, logger):
    bstack11l111111_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠪࢂࠬዓ")), bstack11l111l1ll_opy_)
    try:
        if not os.path.exists(bstack11l111111_opy_):
            os.makedirs(bstack11l111111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠫࢃ࠭ዔ")), bstack11l111l1ll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l111l1_opy_ (u"ࠬࡽࠧዕ")):
                pass
            with open(file_path, bstack1l111l1_opy_ (u"ࠨࡷࠬࠤዖ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l1111ll1_opy_.format(str(e)))
def bstack11l11ll1ll_opy_(file_name, key, value, logger):
    file_path = bstack111lllll11_opy_(bstack1l111l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ዗"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l11ll1_opy_ = json.load(open(file_path, bstack1l111l1_opy_ (u"ࠨࡴࡥࠫዘ")))
        else:
            bstack111l11ll1_opy_ = {}
        bstack111l11ll1_opy_[key] = value
        with open(file_path, bstack1l111l1_opy_ (u"ࠤࡺ࠯ࠧዙ")) as outfile:
            json.dump(bstack111l11ll1_opy_, outfile)
def bstack11lllllll_opy_(file_name, logger):
    file_path = bstack111lllll11_opy_(bstack1l111l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪዚ"), file_name, logger)
    bstack111l11ll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l111l1_opy_ (u"ࠫࡷ࠭ዛ")) as bstack11ll1ll11_opy_:
            bstack111l11ll1_opy_ = json.load(bstack11ll1ll11_opy_)
    return bstack111l11ll1_opy_
def bstack1lll1lll11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫࠺ࠡࠩዜ") + file_path + bstack1l111l1_opy_ (u"࠭ࠠࠨዝ") + str(e))
def bstack1l1ll11lll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l111l1_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤዞ")
def bstack111l11l1_opy_(config):
    if bstack1l111l1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧዟ") in config:
        del (config[bstack1l111l1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨዠ")])
        return False
    if bstack1l1ll11lll_opy_() < version.parse(bstack1l111l1_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩዡ")):
        return False
    if bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪዢ")):
        return True
    if bstack1l111l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬዣ") in config and config[bstack1l111l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ዤ")] is False:
        return False
    else:
        return True
def bstack1111l1l1_opy_(args_list, bstack111ll1llll_opy_):
    index = -1
    for value in bstack111ll1llll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll1ll1l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll1ll1l_opy_ = bstack11lll1ll1l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l111l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧዥ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l111l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨዦ"), exception=exception)
    def bstack11ll1l1l11_opy_(self):
        if self.result != bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዧ"):
            return None
        if bstack1l111l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨየ") in self.exception_type:
            return bstack1l111l1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧዩ")
        return bstack1l111l1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨዪ")
    def bstack11l1111l11_opy_(self):
        if self.result != bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ያ"):
            return None
        if self.bstack11lll1ll1l_opy_:
            return self.bstack11lll1ll1l_opy_
        return bstack11l11l11ll_opy_(self.exception)
def bstack11l11l11ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11l111ll11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll1ll1l1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1l1l11l_opy_(config, logger):
    try:
        import playwright
        bstack11l11lll1l_opy_ = playwright.__file__
        bstack111lll1lll_opy_ = os.path.split(bstack11l11lll1l_opy_)
        bstack11l1111lll_opy_ = bstack111lll1lll_opy_[0] + bstack1l111l1_opy_ (u"ࠧ࠰ࡦࡵ࡭ࡻ࡫ࡲ࠰ࡲࡤࡧࡰࡧࡧࡦ࠱࡯࡭ࡧ࠵ࡣ࡭࡫࠲ࡧࡱ࡯࠮࡫ࡵࠪዬ")
        os.environ[bstack1l111l1_opy_ (u"ࠨࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜ࠫይ")] = bstack1l11l1ll1l_opy_(config)
        with open(bstack11l1111lll_opy_, bstack1l111l1_opy_ (u"ࠩࡵࠫዮ")) as f:
            bstack1l1ll1l111_opy_ = f.read()
            bstack11l1l11111_opy_ = bstack1l111l1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩዯ")
            bstack11l11ll11l_opy_ = bstack1l1ll1l111_opy_.find(bstack11l1l11111_opy_)
            if bstack11l11ll11l_opy_ == -1:
              process = subprocess.Popen(bstack1l111l1_opy_ (u"ࠦࡳࡶ࡭ࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠣደ"), shell=True, cwd=bstack111lll1lll_opy_[0])
              process.wait()
              bstack111llll111_opy_ = bstack1l111l1_opy_ (u"ࠬࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶࠥ࠿ࠬዱ")
              bstack111lll11ll_opy_ = bstack1l111l1_opy_ (u"ࠨࠢࠣࠢ࡟ࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴ࡝ࠤ࠾ࠤࡨࡵ࡮ࡴࡶࠣࡿࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠡࡿࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ࠩ࠼ࠢ࡬ࡪࠥ࠮ࡰࡳࡱࡦࡩࡸࡹ࠮ࡦࡰࡹ࠲ࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠩࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠬ࠮ࡁࠠࠣࠤࠥዲ")
              bstack11l11ll111_opy_ = bstack1l1ll1l111_opy_.replace(bstack111llll111_opy_, bstack111lll11ll_opy_)
              with open(bstack11l1111lll_opy_, bstack1l111l1_opy_ (u"ࠧࡸࠩዳ")) as f:
                f.write(bstack11l11ll111_opy_)
    except Exception as e:
        logger.error(bstack1l1ll11111_opy_.format(str(e)))
def bstack1l1l11llll_opy_():
  try:
    bstack11l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨዴ"))
    bstack11l11llll1_opy_ = []
    if os.path.exists(bstack11l1111l1l_opy_):
      with open(bstack11l1111l1l_opy_) as f:
        bstack11l11llll1_opy_ = json.load(f)
      os.remove(bstack11l1111l1l_opy_)
    return bstack11l11llll1_opy_
  except:
    pass
  return []
def bstack1lll11l111_opy_(bstack1llll11l11_opy_):
  try:
    bstack11l11llll1_opy_ = []
    bstack11l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩድ"))
    if os.path.exists(bstack11l1111l1l_opy_):
      with open(bstack11l1111l1l_opy_) as f:
        bstack11l11llll1_opy_ = json.load(f)
    bstack11l11llll1_opy_.append(bstack1llll11l11_opy_)
    with open(bstack11l1111l1l_opy_, bstack1l111l1_opy_ (u"ࠪࡻࠬዶ")) as f:
        json.dump(bstack11l11llll1_opy_, f)
  except:
    pass
def bstack1l1l111l1_opy_(logger, bstack111lll1ll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l111l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧዷ"), bstack1l111l1_opy_ (u"ࠬ࠭ዸ"))
    if test_name == bstack1l111l1_opy_ (u"࠭ࠧዹ"):
        test_name = threading.current_thread().__dict__.get(bstack1l111l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࡂࡥࡦࡢࡸࡪࡹࡴࡠࡰࡤࡱࡪ࠭ዺ"), bstack1l111l1_opy_ (u"ࠨࠩዻ"))
    bstack111lll11l1_opy_ = bstack1l111l1_opy_ (u"ࠩ࠯ࠤࠬዼ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111lll1ll1_opy_:
        bstack1l1l11l11l_opy_ = os.environ.get(bstack1l111l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪዽ"), bstack1l111l1_opy_ (u"ࠫ࠵࠭ዾ"))
        bstack1lllllllll_opy_ = {bstack1l111l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪዿ"): test_name, bstack1l111l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬጀ"): bstack111lll11l1_opy_, bstack1l111l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ጁ"): bstack1l1l11l11l_opy_}
        bstack11l11111ll_opy_ = []
        bstack111llllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧጂ"))
        if os.path.exists(bstack111llllll1_opy_):
            with open(bstack111llllll1_opy_) as f:
                bstack11l11111ll_opy_ = json.load(f)
        bstack11l11111ll_opy_.append(bstack1lllllllll_opy_)
        with open(bstack111llllll1_opy_, bstack1l111l1_opy_ (u"ࠩࡺࠫጃ")) as f:
            json.dump(bstack11l11111ll_opy_, f)
    else:
        bstack1lllllllll_opy_ = {bstack1l111l1_opy_ (u"ࠪࡲࡦࡳࡥࠨጄ"): test_name, bstack1l111l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪጅ"): bstack111lll11l1_opy_, bstack1l111l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫጆ"): str(multiprocessing.current_process().name)}
        if bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪጇ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lllllllll_opy_)
  except Exception as e:
      logger.warn(bstack1l111l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡳࡽࡹ࡫ࡳࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦገ").format(e))
def bstack111111111_opy_(error_message, test_name, index, logger):
  try:
    bstack111lll111l_opy_ = []
    bstack1lllllllll_opy_ = {bstack1l111l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ጉ"): test_name, bstack1l111l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨጊ"): error_message, bstack1l111l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩጋ"): index}
    bstack11l11l1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬጌ"))
    if os.path.exists(bstack11l11l1l11_opy_):
        with open(bstack11l11l1l11_opy_) as f:
            bstack111lll111l_opy_ = json.load(f)
    bstack111lll111l_opy_.append(bstack1lllllllll_opy_)
    with open(bstack11l11l1l11_opy_, bstack1l111l1_opy_ (u"ࠬࡽࠧግ")) as f:
        json.dump(bstack111lll111l_opy_, f)
  except Exception as e:
    logger.warn(bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤጎ").format(e))
def bstack1ll1lll1l_opy_(bstack1l11l1ll1_opy_, name, logger):
  try:
    bstack1lllllllll_opy_ = {bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬጏ"): name, bstack1l111l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧጐ"): bstack1l11l1ll1_opy_, bstack1l111l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ጑"): str(threading.current_thread()._name)}
    return bstack1lllllllll_opy_
  except Exception as e:
    logger.warn(bstack1l111l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡨࡥࡩࡣࡹࡩࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢጒ").format(e))
  return
def bstack11l11111l1_opy_():
    return platform.system() == bstack1l111l1_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺࡷࠬጓ")
def bstack1llll1lll1_opy_(bstack111lll1l1l_opy_, config, logger):
    bstack111ll1ll1l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111lll1l1l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡰࡹ࡫ࡲࠡࡥࡲࡲ࡫࡯ࡧࠡ࡭ࡨࡽࡸࠦࡢࡺࠢࡵࡩ࡬࡫ࡸࠡ࡯ࡤࡸࡨ࡮࠺ࠡࡽࢀࠦጔ").format(e))
    return bstack111ll1ll1l_opy_