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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _111ll11ll1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111ll1l1l1_opy_:
    def __init__(self, handler):
        self._111ll1l1ll_opy_ = {}
        self._111ll11l1l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._111ll1l1ll_opy_[bstack1l111l1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩጕ")] = Module._inject_setup_function_fixture
        self._111ll1l1ll_opy_[bstack1l111l1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ጖")] = Module._inject_setup_module_fixture
        self._111ll1l1ll_opy_[bstack1l111l1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ጗")] = Class._inject_setup_class_fixture
        self._111ll1l1ll_opy_[bstack1l111l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪጘ")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack111ll1l111_opy_(bstack1l111l1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ጙ"))
        Module._inject_setup_module_fixture = self.bstack111ll1l111_opy_(bstack1l111l1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጚ"))
        Class._inject_setup_class_fixture = self.bstack111ll1l111_opy_(bstack1l111l1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጛ"))
        Class._inject_setup_method_fixture = self.bstack111ll1l111_opy_(bstack1l111l1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧጜ"))
    def bstack111l1llll1_opy_(self, bstack111ll111l1_opy_, hook_type):
        meth = getattr(bstack111ll111l1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111ll11l1l_opy_[hook_type] = meth
            setattr(bstack111ll111l1_opy_, hook_type, self.bstack111l1lll1l_opy_(hook_type))
    def bstack111ll1l11l_opy_(self, instance, bstack111ll11111_opy_):
        if bstack111ll11111_opy_ == bstack1l111l1_opy_ (u"ࠢࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠥጝ"):
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤጞ"))
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨጟ"))
        if bstack111ll11111_opy_ == bstack1l111l1_opy_ (u"ࠥࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠦጠ"):
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠥጡ"))
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠢጢ"))
        if bstack111ll11111_opy_ == bstack1l111l1_opy_ (u"ࠨࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࠨጣ"):
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠧጤ"))
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠤጥ"))
        if bstack111ll11111_opy_ == bstack1l111l1_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠥጦ"):
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠤጧ"))
            self.bstack111l1llll1_opy_(instance.obj, bstack1l111l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩࠨጨ"))
    @staticmethod
    def bstack111ll11lll_opy_(hook_type, func, args):
        if hook_type in [bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫጩ"), bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨጪ")]:
            _111ll11ll1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111l1lll1l_opy_(self, hook_type):
        def bstack111ll111ll_opy_(arg=None):
            self.handler(hook_type, bstack1l111l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧጫ"))
            result = None
            exception = None
            try:
                self.bstack111ll11lll_opy_(hook_type, self._111ll11l1l_opy_[hook_type], (arg,))
                result = Result(result=bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨጬ"))
            except Exception as e:
                result = Result(result=bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩጭ"), exception=e)
                self.handler(hook_type, bstack1l111l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩጮ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l111l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪጯ"), result)
        def bstack111ll11l11_opy_(this, arg=None):
            self.handler(hook_type, bstack1l111l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬጰ"))
            result = None
            exception = None
            try:
                self.bstack111ll11lll_opy_(hook_type, self._111ll11l1l_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l111l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ጱ"))
            except Exception as e:
                result = Result(result=bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧጲ"), exception=e)
                self.handler(hook_type, bstack1l111l1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧጳ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l111l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨጴ"), result)
        if hook_type in [bstack1l111l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩጵ"), bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ጶ")]:
            return bstack111ll11l11_opy_
        return bstack111ll111ll_opy_
    def bstack111ll1l111_opy_(self, bstack111ll11111_opy_):
        def bstack111l1lllll_opy_(this, *args, **kwargs):
            self.bstack111ll1l11l_opy_(this, bstack111ll11111_opy_)
            self._111ll1l1ll_opy_[bstack111ll11111_opy_](this, *args, **kwargs)
        return bstack111l1lllll_opy_