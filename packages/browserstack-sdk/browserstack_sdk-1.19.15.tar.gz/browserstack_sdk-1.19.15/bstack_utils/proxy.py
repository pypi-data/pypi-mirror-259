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
import os
from urllib.parse import urlparse
from bstack_utils.messages import bstack111l11l1l1_opy_
def bstack1111111111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11111111ll_opy_(bstack1llllllllll_opy_, bstack1111111l11_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1llllllllll_opy_):
        with open(bstack1llllllllll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1111111111_opy_(bstack1llllllllll_opy_):
        pac = get_pac(url=bstack1llllllllll_opy_)
    else:
        raise Exception(bstack1l111l1_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨᐓ").format(bstack1llllllllll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l111l1_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥᐔ"), 80))
        bstack11111111l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11111111l1_opy_ = bstack1l111l1_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫᐕ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1111111l11_opy_, bstack11111111l1_opy_)
    return proxy_url
def bstack1l1ll1lll1_opy_(config):
    return bstack1l111l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᐖ") in config or bstack1l111l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᐗ") in config
def bstack1l11l1ll1l_opy_(config):
    if not bstack1l1ll1lll1_opy_(config):
        return
    if config.get(bstack1l111l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᐘ")):
        return config.get(bstack1l111l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᐙ"))
    if config.get(bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᐚ")):
        return config.get(bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᐛ"))
def bstack1l1ll1ll_opy_(config, bstack1111111l11_opy_):
    proxy = bstack1l11l1ll1l_opy_(config)
    proxies = {}
    if config.get(bstack1l111l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᐜ")) or config.get(bstack1l111l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᐝ")):
        if proxy.endswith(bstack1l111l1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪᐞ")):
            proxies = bstack11l1l1111_opy_(proxy, bstack1111111l11_opy_)
        else:
            proxies = {
                bstack1l111l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᐟ"): proxy
            }
    return proxies
def bstack11l1l1111_opy_(bstack1llllllllll_opy_, bstack1111111l11_opy_):
    proxies = {}
    global bstack1lllllllll1_opy_
    if bstack1l111l1_opy_ (u"ࠧࡑࡃࡆࡣࡕࡘࡏ࡙࡛ࠪᐠ") in globals():
        return bstack1lllllllll1_opy_
    try:
        proxy = bstack11111111ll_opy_(bstack1llllllllll_opy_, bstack1111111l11_opy_)
        if bstack1l111l1_opy_ (u"ࠣࡆࡌࡖࡊࡉࡔࠣᐡ") in proxy:
            proxies = {}
        elif bstack1l111l1_opy_ (u"ࠤࡋࡘ࡙ࡖࠢᐢ") in proxy or bstack1l111l1_opy_ (u"ࠥࡌ࡙࡚ࡐࡔࠤᐣ") in proxy or bstack1l111l1_opy_ (u"ࠦࡘࡕࡃࡌࡕࠥᐤ") in proxy:
            bstack111111111l_opy_ = proxy.split(bstack1l111l1_opy_ (u"ࠧࠦࠢᐥ"))
            if bstack1l111l1_opy_ (u"ࠨ࠺࠰࠱ࠥᐦ") in bstack1l111l1_opy_ (u"ࠢࠣᐧ").join(bstack111111111l_opy_[1:]):
                proxies = {
                    bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᐨ"): bstack1l111l1_opy_ (u"ࠤࠥᐩ").join(bstack111111111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l111l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᐪ"): str(bstack111111111l_opy_[0]).lower() + bstack1l111l1_opy_ (u"ࠦ࠿࠵࠯ࠣᐫ") + bstack1l111l1_opy_ (u"ࠧࠨᐬ").join(bstack111111111l_opy_[1:])
                }
        elif bstack1l111l1_opy_ (u"ࠨࡐࡓࡑ࡛࡝ࠧᐭ") in proxy:
            bstack111111111l_opy_ = proxy.split(bstack1l111l1_opy_ (u"ࠢࠡࠤᐮ"))
            if bstack1l111l1_opy_ (u"ࠣ࠼࠲࠳ࠧᐯ") in bstack1l111l1_opy_ (u"ࠤࠥᐰ").join(bstack111111111l_opy_[1:]):
                proxies = {
                    bstack1l111l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᐱ"): bstack1l111l1_opy_ (u"ࠦࠧᐲ").join(bstack111111111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l111l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᐳ"): bstack1l111l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᐴ") + bstack1l111l1_opy_ (u"ࠢࠣᐵ").join(bstack111111111l_opy_[1:])
                }
        else:
            proxies = {
                bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᐶ"): proxy
            }
    except Exception as e:
        print(bstack1l111l1_opy_ (u"ࠤࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨᐷ"), bstack111l11l1l1_opy_.format(bstack1llllllllll_opy_, str(e)))
    bstack1lllllllll1_opy_ = proxies
    return proxies