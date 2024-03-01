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
from uuid import uuid4
from bstack_utils.helper import bstack1lll11llll_opy_, bstack11l1111ll1_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llllll1lll_opy_
class bstack1l111lllll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11lllll1ll_opy_=None, framework=None, tags=[], scope=[], bstack1llll1l111l_opy_=None, bstack1llll1l1l11_opy_=True, bstack1llll11l11l_opy_=None, bstack1lll1ll1l1_opy_=None, result=None, duration=None, bstack1l111ll1ll_opy_=None, meta={}):
        self.bstack1l111ll1ll_opy_ = bstack1l111ll1ll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1llll1l1l11_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11lllll1ll_opy_ = bstack11lllll1ll_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1llll1l111l_opy_ = bstack1llll1l111l_opy_
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
        self.bstack1lll1ll1l1_opy_ = bstack1lll1ll1l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11llll1ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1llll11l1l1_opy_(self):
        bstack1llll11l1ll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ᒡ"): bstack1llll11l1ll_opy_,
            bstack1l111l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ᒢ"): bstack1llll11l1ll_opy_,
            bstack1l111l1_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪᒣ"): bstack1llll11l1ll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢᒤ") + key)
            setattr(self, key, val)
    def bstack1llll1l1lll_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᒥ"): self.name,
            bstack1l111l1_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᒦ"): {
                bstack1l111l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᒧ"): bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᒨ"),
                bstack1l111l1_opy_ (u"ࠫࡨࡵࡤࡦࠩᒩ"): self.code
            },
            bstack1l111l1_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᒪ"): self.scope,
            bstack1l111l1_opy_ (u"࠭ࡴࡢࡩࡶࠫᒫ"): self.tags,
            bstack1l111l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᒬ"): self.framework,
            bstack1l111l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᒭ"): self.bstack11lllll1ll_opy_
        }
    def bstack1llll1ll1l1_opy_(self):
        return {
         bstack1l111l1_opy_ (u"ࠩࡰࡩࡹࡧࠧᒮ"): self.meta
        }
    def bstack1llll1l1111_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭ᒯ"): {
                bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨᒰ"): self.bstack1llll1l111l_opy_
            }
        }
    def bstack1llll1l1ll1_opy_(self, bstack1llll11ll11_opy_, details):
        step = next(filter(lambda st: st[bstack1l111l1_opy_ (u"ࠬ࡯ࡤࠨᒱ")] == bstack1llll11ll11_opy_, self.meta[bstack1l111l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᒲ")]), None)
        step.update(details)
    def bstack1llll1l11ll_opy_(self, bstack1llll11ll11_opy_):
        step = next(filter(lambda st: st[bstack1l111l1_opy_ (u"ࠧࡪࡦࠪᒳ")] == bstack1llll11ll11_opy_, self.meta[bstack1l111l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᒴ")]), None)
        step.update({
            bstack1l111l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᒵ"): bstack1lll11llll_opy_()
        })
    def bstack1l11111l1l_opy_(self, bstack1llll11ll11_opy_, result, duration=None):
        bstack1llll11l11l_opy_ = bstack1lll11llll_opy_()
        if bstack1llll11ll11_opy_ is not None and self.meta.get(bstack1l111l1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᒶ")):
            step = next(filter(lambda st: st[bstack1l111l1_opy_ (u"ࠫ࡮ࡪࠧᒷ")] == bstack1llll11ll11_opy_, self.meta[bstack1l111l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᒸ")]), None)
            step.update({
                bstack1l111l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᒹ"): bstack1llll11l11l_opy_,
                bstack1l111l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩᒺ"): duration if duration else bstack11l1111ll1_opy_(step[bstack1l111l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᒻ")], bstack1llll11l11l_opy_),
                bstack1l111l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᒼ"): result.result,
                bstack1l111l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᒽ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1llll1l11l1_opy_):
        if self.meta.get(bstack1l111l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᒾ")):
            self.meta[bstack1l111l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᒿ")].append(bstack1llll1l11l1_opy_)
        else:
            self.meta[bstack1l111l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓀ")] = [ bstack1llll1l11l1_opy_ ]
    def bstack1llll11lll1_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᓁ"): self.bstack11llll1ll1_opy_(),
            **self.bstack1llll1l1lll_opy_(),
            **self.bstack1llll11l1l1_opy_(),
            **self.bstack1llll1ll1l1_opy_()
        }
    def bstack1llll1ll1ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᓂ"): self.bstack1llll11l11l_opy_,
            bstack1l111l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᓃ"): self.duration,
            bstack1l111l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᓄ"): self.result.result
        }
        if data[bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᓅ")] == bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᓆ"):
            data[bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᓇ")] = self.result.bstack11ll1l1l11_opy_()
            data[bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᓈ")] = [{bstack1l111l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᓉ"): self.result.bstack11l1111l11_opy_()}]
        return data
    def bstack1llll11llll_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᓊ"): self.bstack11llll1ll1_opy_(),
            **self.bstack1llll1l1lll_opy_(),
            **self.bstack1llll11l1l1_opy_(),
            **self.bstack1llll1ll1ll_opy_(),
            **self.bstack1llll1ll1l1_opy_()
        }
    def bstack11llll11l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l111l1_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫᓋ") in event:
            return self.bstack1llll11lll1_opy_()
        elif bstack1l111l1_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓌ") in event:
            return self.bstack1llll11llll_opy_()
    def bstack11llllll11_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1llll11l11l_opy_ = time if time else bstack1lll11llll_opy_()
        self.duration = duration if duration else bstack11l1111ll1_opy_(self.bstack11lllll1ll_opy_, self.bstack1llll11l11l_opy_)
        if result:
            self.result = result
class bstack1l111l1l11_opy_(bstack1l111lllll_opy_):
    def __init__(self, hooks=[], bstack1l1111llll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1111llll_opy_ = bstack1l1111llll_opy_
        super().__init__(*args, **kwargs, bstack1lll1ll1l1_opy_=bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࠪᓍ"))
    @classmethod
    def bstack1llll1ll111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l111l1_opy_ (u"࠭ࡩࡥࠩᓎ"): id(step),
                bstack1l111l1_opy_ (u"ࠧࡵࡧࡻࡸࠬᓏ"): step.name,
                bstack1l111l1_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩᓐ"): step.keyword,
            })
        return bstack1l111l1l11_opy_(
            **kwargs,
            meta={
                bstack1l111l1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪᓑ"): {
                    bstack1l111l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᓒ"): feature.name,
                    bstack1l111l1_opy_ (u"ࠫࡵࡧࡴࡩࠩᓓ"): feature.filename,
                    bstack1l111l1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪᓔ"): feature.description
                },
                bstack1l111l1_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨᓕ"): {
                    bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᓖ"): scenario.name
                },
                bstack1l111l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᓗ"): steps,
                bstack1l111l1_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫᓘ"): bstack1llllll1lll_opy_(test)
            }
        )
    def bstack1llll1ll11l_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᓙ"): self.hooks
        }
    def bstack1llll11ll1l_opy_(self):
        if self.bstack1l1111llll_opy_:
            return {
                bstack1l111l1_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪᓚ"): self.bstack1l1111llll_opy_
            }
        return {}
    def bstack1llll11llll_opy_(self):
        return {
            **super().bstack1llll11llll_opy_(),
            **self.bstack1llll1ll11l_opy_()
        }
    def bstack1llll11lll1_opy_(self):
        return {
            **super().bstack1llll11lll1_opy_(),
            **self.bstack1llll11ll1l_opy_()
        }
    def bstack11llllll11_opy_(self):
        return bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᓛ")
class bstack1l111111l1_opy_(bstack1l111lllll_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1lll1ll1l1_opy_=bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᓜ"))
    def bstack11llll111l_opy_(self):
        return self.hook_type
    def bstack1llll1l1l1l_opy_(self):
        return {
            bstack1l111l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᓝ"): self.hook_type
        }
    def bstack1llll11llll_opy_(self):
        return {
            **super().bstack1llll11llll_opy_(),
            **self.bstack1llll1l1l1l_opy_()
        }
    def bstack1llll11lll1_opy_(self):
        return {
            **super().bstack1llll11lll1_opy_(),
            **self.bstack1llll1l1l1l_opy_()
        }
    def bstack11llllll11_opy_(self):
        return bstack1l111l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪᓞ")