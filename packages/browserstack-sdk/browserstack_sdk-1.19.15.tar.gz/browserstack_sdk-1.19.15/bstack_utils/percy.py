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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1l1ll1l1l_opy_, bstack1ll1llll1_opy_
class bstack1l1l11111l_opy_:
  working_dir = os.getcwd()
  bstack1ll1llll11_opy_ = False
  config = {}
  binary_path = bstack1l111l1_opy_ (u"ࠬ࠭Ꭾ")
  bstack1111lll11l_opy_ = bstack1l111l1_opy_ (u"࠭ࠧᎯ")
  bstack1ll1l1111l_opy_ = False
  bstack1111llll11_opy_ = None
  bstack11111ll111_opy_ = {}
  bstack1111l1l11l_opy_ = 300
  bstack111l11111l_opy_ = False
  logger = None
  bstack1111l1lll1_opy_ = False
  bstack1111lll1l1_opy_ = bstack1l111l1_opy_ (u"ࠧࠨᎰ")
  bstack11111lllll_opy_ = {
    bstack1l111l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨᎱ") : 1,
    bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪᎲ") : 2,
    bstack1l111l1_opy_ (u"ࠪࡩࡩ࡭ࡥࠨᎳ") : 3,
    bstack1l111l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫᎴ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11111ll11l_opy_(self):
    bstack111l1111ll_opy_ = bstack1l111l1_opy_ (u"ࠬ࠭Ꮅ")
    bstack1111ll1111_opy_ = sys.platform
    bstack1111ll111l_opy_ = bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᎶ")
    if re.match(bstack1l111l1_opy_ (u"ࠢࡥࡣࡵࡻ࡮ࡴࡼ࡮ࡣࡦࠤࡴࡹࠢᎷ"), bstack1111ll1111_opy_) != None:
      bstack111l1111ll_opy_ = bstack11l1l11l11_opy_ + bstack1l111l1_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡱࡶࡼ࠳ࢀࡩࡱࠤᎸ")
      self.bstack1111lll1l1_opy_ = bstack1l111l1_opy_ (u"ࠩࡰࡥࡨ࠭Ꮉ")
    elif re.match(bstack1l111l1_opy_ (u"ࠥࡱࡸࡽࡩ࡯ࡾࡰࡷࡾࡹࡼ࡮࡫ࡱ࡫ࡼࢂࡣࡺࡩࡺ࡭ࡳࢂࡢࡤࡥࡺ࡭ࡳࢂࡷࡪࡰࡦࡩࢁ࡫࡭ࡤࡾࡺ࡭ࡳ࠹࠲ࠣᎺ"), bstack1111ll1111_opy_) != None:
      bstack111l1111ll_opy_ = bstack11l1l11l11_opy_ + bstack1l111l1_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡼ࡯࡮࠯ࡼ࡬ࡴࠧᎻ")
      bstack1111ll111l_opy_ = bstack1l111l1_opy_ (u"ࠧࡶࡥࡳࡥࡼ࠲ࡪࡾࡥࠣᎼ")
      self.bstack1111lll1l1_opy_ = bstack1l111l1_opy_ (u"࠭ࡷࡪࡰࠪᎽ")
    else:
      bstack111l1111ll_opy_ = bstack11l1l11l11_opy_ + bstack1l111l1_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭࡭࡫ࡱࡹࡽ࠴ࡺࡪࡲࠥᎾ")
      self.bstack1111lll1l1_opy_ = bstack1l111l1_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧᎿ")
    return bstack111l1111ll_opy_, bstack1111ll111l_opy_
  def bstack1111l1l111_opy_(self):
    try:
      bstack111l111111_opy_ = [os.path.join(expanduser(bstack1l111l1_opy_ (u"ࠤࢁࠦᏀ")), bstack1l111l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᏁ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111l111111_opy_:
        if(self.bstack1111l1ll1l_opy_(path)):
          return path
      raise bstack1l111l1_opy_ (u"࡚ࠦࡴࡡ࡭ࡤࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣᏂ")
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠰ࠤࢀࢃࠢᏃ").format(e))
  def bstack1111l1ll1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1111llllll_opy_(self, bstack111l1111ll_opy_, bstack1111ll111l_opy_):
    try:
      bstack111l11l111_opy_ = self.bstack1111l1l111_opy_()
      bstack111l111ll1_opy_ = os.path.join(bstack111l11l111_opy_, bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࢀࡩࡱࠩᏄ"))
      bstack1111ll1lll_opy_ = os.path.join(bstack111l11l111_opy_, bstack1111ll111l_opy_)
      if os.path.exists(bstack1111ll1lll_opy_):
        self.logger.info(bstack1l111l1_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡹ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤᏅ").format(bstack1111ll1lll_opy_))
        return bstack1111ll1lll_opy_
      if os.path.exists(bstack111l111ll1_opy_):
        self.logger.info(bstack1l111l1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡻ࡫ࡳࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡹࡳࢀࡩࡱࡲ࡬ࡲ࡬ࠨᏆ").format(bstack111l111ll1_opy_))
        return self.bstack1111l1ll11_opy_(bstack111l111ll1_opy_, bstack1111ll111l_opy_)
      self.logger.info(bstack1l111l1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰࠤࢀࢃࠢᏇ").format(bstack111l1111ll_opy_))
      response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠪࡋࡊ࡚ࠧᏈ"), bstack111l1111ll_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack111l111ll1_opy_, bstack1l111l1_opy_ (u"ࠫࡼࡨࠧᏉ")) as file:
          file.write(response.content)
        self.logger.info(bstack11111l1ll1_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡤ࡬ࡲࡦࡸࡹࡠࡼ࡬ࡴࡤࡶࡡࡵࡪࢀࠦᏊ"))
        return self.bstack1111l1ll11_opy_(bstack111l111ll1_opy_, bstack1111ll111l_opy_)
      else:
        raise(bstack11111l1ll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࡶࡸࡦࡺࡵࡴࡡࡦࡳࡩ࡫ࡽࠣᏋ"))
    except:
      self.logger.error(bstack1l111l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᏌ"))
  def bstack1111l1l1ll_opy_(self, bstack111l1111ll_opy_, bstack1111ll111l_opy_):
    try:
      bstack1111ll1lll_opy_ = self.bstack1111llllll_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_)
      bstack1111lll1ll_opy_ = self.bstack111l111l1l_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_, bstack1111ll1lll_opy_)
      return bstack1111ll1lll_opy_, bstack1111lll1ll_opy_
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧᏍ").format(e))
    return bstack1111ll1lll_opy_, False
  def bstack111l111l1l_opy_(self, bstack111l1111ll_opy_, bstack1111ll111l_opy_, bstack1111ll1lll_opy_, bstack11111l1lll_opy_ = 0):
    if bstack11111l1lll_opy_ > 1:
      return False
    if bstack1111ll1lll_opy_ == None or os.path.exists(bstack1111ll1lll_opy_) == False:
      self.logger.warn(bstack1l111l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᏎ"))
      bstack1111ll1lll_opy_ = self.bstack1111llllll_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_)
      self.bstack111l111l1l_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_, bstack1111ll1lll_opy_, bstack11111l1lll_opy_+1)
    bstack1111l111l1_opy_ = bstack1l111l1_opy_ (u"ࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾࡢ࠯ࡤ࡮࡬ࠤࡡࡪ࠮࡝ࡦ࠮࠲ࡡࡪࠫࠣᏏ")
    command = bstack1l111l1_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪᏐ").format(bstack1111ll1lll_opy_)
    bstack11111l1l1l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111l111l1_opy_, bstack11111l1l1l_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l111l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦᏑ"))
      bstack1111ll1lll_opy_ = self.bstack1111llllll_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_)
      self.bstack111l111l1l_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_, bstack1111ll1lll_opy_, bstack11111l1lll_opy_+1)
  def bstack1111l1ll11_opy_(self, bstack111l111ll1_opy_, bstack1111ll111l_opy_):
    try:
      working_dir = os.path.dirname(bstack111l111ll1_opy_)
      shutil.unpack_archive(bstack111l111ll1_opy_, working_dir)
      bstack1111ll1lll_opy_ = os.path.join(working_dir, bstack1111ll111l_opy_)
      os.chmod(bstack1111ll1lll_opy_, 0o755)
      return bstack1111ll1lll_opy_
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᏒ"))
  def bstack1111llll1l_opy_(self):
    try:
      percy = str(self.config.get(bstack1l111l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭Ꮣ"), bstack1l111l1_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢᏔ"))).lower()
      if percy != bstack1l111l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᏕ"):
        return False
      self.bstack1ll1l1111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᏖ").format(e))
  def bstack111l1111l1_opy_(self):
    try:
      bstack111l1111l1_opy_ = str(self.config.get(bstack1l111l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᏗ"), bstack1l111l1_opy_ (u"ࠧࡧࡵࡵࡱࠥᏘ"))).lower()
      return bstack111l1111l1_opy_
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹࠡࡥࡤࡴࡹࡻࡲࡦࠢࡰࡳࡩ࡫ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᏙ").format(e))
  def init(self, bstack1ll1llll11_opy_, config, logger):
    self.bstack1ll1llll11_opy_ = bstack1ll1llll11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111llll1l_opy_():
      return
    self.bstack11111ll111_opy_ = config.get(bstack1l111l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭Ꮪ"), {})
    self.bstack1111l11l1l_opy_ = config.get(bstack1l111l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᏛ"), bstack1l111l1_opy_ (u"ࠤࡤࡹࡹࡵࠢᏜ"))
    try:
      bstack111l1111ll_opy_, bstack1111ll111l_opy_ = self.bstack11111ll11l_opy_()
      bstack1111ll1lll_opy_, bstack1111lll1ll_opy_ = self.bstack1111l1l1ll_opy_(bstack111l1111ll_opy_, bstack1111ll111l_opy_)
      if bstack1111lll1ll_opy_:
        self.binary_path = bstack1111ll1lll_opy_
        thread = Thread(target=self.bstack1111l1111l_opy_)
        thread.start()
      else:
        self.bstack1111l1lll1_opy_ = True
        self.logger.error(bstack1l111l1_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡨࡲࡹࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡒࡨࡶࡨࡿࠢᏝ").format(bstack1111ll1lll_opy_))
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᏞ").format(e))
  def bstack11111l1l11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l111l1_opy_ (u"ࠬࡲ࡯ࡨࠩᏟ"), bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࡲ࡯ࡨࠩᏠ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l111l1_opy_ (u"ࠢࡑࡷࡶ࡬࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࡷࠥࡧࡴࠡࡽࢀࠦᏡ").format(logfile))
      self.bstack1111lll11l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࠤࡵࡧࡴࡩ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᏢ").format(e))
  def bstack1111l1111l_opy_(self):
    bstack11111lll11_opy_ = self.bstack111l111lll_opy_()
    if bstack11111lll11_opy_ == None:
      self.bstack1111l1lll1_opy_ = True
      self.logger.error(bstack1l111l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠧᏣ"))
      return False
    command_args = [bstack1l111l1_opy_ (u"ࠥࡥࡵࡶ࠺ࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠦᏤ") if self.bstack1ll1llll11_opy_ else bstack1l111l1_opy_ (u"ࠫࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠨᏥ")]
    bstack1111l11lll_opy_ = self.bstack1111l111ll_opy_()
    if bstack1111l11lll_opy_ != None:
      command_args.append(bstack1l111l1_opy_ (u"ࠧ࠳ࡣࠡࡽࢀࠦᏦ").format(bstack1111l11lll_opy_))
    env = os.environ.copy()
    env[bstack1l111l1_opy_ (u"ࠨࡐࡆࡔࡆ࡝ࡤ࡚ࡏࡌࡇࡑࠦᏧ")] = bstack11111lll11_opy_
    bstack1111lllll1_opy_ = [self.binary_path]
    self.bstack11111l1l11_opy_()
    self.bstack1111llll11_opy_ = self.bstack1111ll11ll_opy_(bstack1111lllll1_opy_ + command_args, env)
    self.logger.debug(bstack1l111l1_opy_ (u"ࠢࡔࡶࡤࡶࡹ࡯࡮ࡨࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠣᏨ"))
    bstack11111l1lll_opy_ = 0
    while self.bstack1111llll11_opy_.poll() == None:
      bstack1111l11ll1_opy_ = self.bstack1111ll1l1l_opy_()
      if bstack1111l11ll1_opy_:
        self.logger.debug(bstack1l111l1_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠦᏩ"))
        self.bstack111l11111l_opy_ = True
        return True
      bstack11111l1lll_opy_ += 1
      self.logger.debug(bstack1l111l1_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡔࡨࡸࡷࡿࠠ࠮ࠢࡾࢁࠧᏪ").format(bstack11111l1lll_opy_))
      time.sleep(2)
    self.logger.error(bstack1l111l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡋࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࠦࡡࡵࡶࡨࡱࡵࡺࡳࠣᏫ").format(bstack11111l1lll_opy_))
    self.bstack1111l1lll1_opy_ = True
    return False
  def bstack1111ll1l1l_opy_(self, bstack11111l1lll_opy_ = 0):
    try:
      if bstack11111l1lll_opy_ > 10:
        return False
      bstack111l111l11_opy_ = os.environ.get(bstack1l111l1_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡗࡊࡘࡖࡆࡔࡢࡅࡉࡊࡒࡆࡕࡖࠫᏬ"), bstack1l111l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡲ࡯ࡤࡣ࡯࡬ࡴࡹࡴ࠻࠷࠶࠷࠽࠭Ꮽ"))
      bstack1111ll1l11_opy_ = bstack111l111l11_opy_ + bstack11l1l111ll_opy_
      response = requests.get(bstack1111ll1l11_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack111l111lll_opy_(self):
    bstack1111l1llll_opy_ = bstack1l111l1_opy_ (u"࠭ࡡࡱࡲࠪᏮ") if self.bstack1ll1llll11_opy_ else bstack1l111l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᏯ")
    bstack111lll1l11_opy_ = bstack1l111l1_opy_ (u"ࠣࡣࡳ࡭࠴ࡧࡰࡱࡡࡳࡩࡷࡩࡹ࠰ࡩࡨࡸࡤࡶࡲࡰ࡬ࡨࡧࡹࡥࡴࡰ࡭ࡨࡲࡄࡴࡡ࡮ࡧࡀࡿࢂࠬࡴࡺࡲࡨࡁࢀࢃࠢᏰ").format(self.config[bstack1l111l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᏱ")], bstack1111l1llll_opy_)
    uri = bstack1l1ll1l1l_opy_(bstack111lll1l11_opy_)
    try:
      response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠪࡋࡊ࡚ࠧᏲ"), uri, {}, {bstack1l111l1_opy_ (u"ࠫࡦࡻࡴࡩࠩᏳ"): (self.config[bstack1l111l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᏴ")], self.config[bstack1l111l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᏵ")])})
      if response.status_code == 200:
        bstack1111l11111_opy_ = response.json()
        if bstack1l111l1_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨ᏶") in bstack1111l11111_opy_:
          return bstack1111l11111_opy_[bstack1l111l1_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢ᏷")]
        else:
          raise bstack1l111l1_opy_ (u"ࠩࡗࡳࡰ࡫࡮ࠡࡐࡲࡸࠥࡌ࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾࠩᏸ").format(bstack1111l11111_opy_)
      else:
        raise bstack1l111l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡶࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡳࡵࡣࡷࡹࡸࠦ࠭ࠡࡽࢀ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡃࡱࡧࡽࠥ࠳ࠠࡼࡿࠥᏹ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡵࡸ࡯࡫ࡧࡦࡸࠧᏺ").format(e))
  def bstack1111l111ll_opy_(self):
    bstack11111ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠧࡶࡥࡳࡥࡼࡇࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠣᏻ"))
    try:
      if bstack1l111l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᏼ") not in self.bstack11111ll111_opy_:
        self.bstack11111ll111_opy_[bstack1l111l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨᏽ")] = 2
      with open(bstack11111ll1ll_opy_, bstack1l111l1_opy_ (u"ࠨࡹࠪ᏾")) as fp:
        json.dump(self.bstack11111ll111_opy_, fp)
      return bstack11111ll1ll_opy_
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡩࡲࡦࡣࡷࡩࠥࡶࡥࡳࡥࡼࠤࡨࡵ࡮ࡧ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ᏿").format(e))
  def bstack1111ll11ll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111lll1l1_opy_ == bstack1l111l1_opy_ (u"ࠪࡻ࡮ࡴࠧ᐀"):
        bstack1111l11l11_opy_ = [bstack1l111l1_opy_ (u"ࠫࡨࡳࡤ࠯ࡧࡻࡩࠬᐁ"), bstack1l111l1_opy_ (u"ࠬ࠵ࡣࠨᐂ")]
        cmd = bstack1111l11l11_opy_ + cmd
      cmd = bstack1l111l1_opy_ (u"࠭ࠠࠨᐃ").join(cmd)
      self.logger.debug(bstack1l111l1_opy_ (u"ࠢࡓࡷࡱࡲ࡮ࡴࡧࠡࡽࢀࠦᐄ").format(cmd))
      with open(self.bstack1111lll11l_opy_, bstack1l111l1_opy_ (u"ࠣࡣࠥᐅ")) as bstack1111lll111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111lll111_opy_, text=True, stderr=bstack1111lll111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111l1lll1_opy_ = True
      self.logger.error(bstack1l111l1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠣࡻ࡮ࡺࡨࠡࡥࡰࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᐆ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack111l11111l_opy_:
        self.logger.info(bstack1l111l1_opy_ (u"ࠥࡗࡹࡵࡰࡱ࡫ࡱ࡫ࠥࡖࡥࡳࡥࡼࠦᐇ"))
        cmd = [self.binary_path, bstack1l111l1_opy_ (u"ࠦࡪࡾࡥࡤ࠼ࡶࡸࡴࡶࠢᐈ")]
        self.bstack1111ll11ll_opy_(cmd)
        self.bstack111l11111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡳࡵࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡩ࡯࡮࡯ࡤࡲࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧᐉ").format(cmd, e))
  def bstack1lll1llll_opy_(self):
    if not self.bstack1ll1l1111l_opy_:
      return
    try:
      bstack1111ll11l1_opy_ = 0
      while not self.bstack111l11111l_opy_ and bstack1111ll11l1_opy_ < self.bstack1111l1l11l_opy_:
        if self.bstack1111l1lll1_opy_:
          self.logger.info(bstack1l111l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤ࡫ࡧࡩ࡭ࡧࡧࠦᐊ"))
          return
        time.sleep(1)
        bstack1111ll11l1_opy_ += 1
      os.environ[bstack1l111l1_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡂࡆࡕࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒ࠭ᐋ")] = str(self.bstack1111ll1ll1_opy_())
      self.logger.info(bstack1l111l1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠤᐌ"))
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᐍ").format(e))
  def bstack1111ll1ll1_opy_(self):
    if self.bstack1ll1llll11_opy_:
      return
    try:
      bstack11111lll1l_opy_ = [platform[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᐎ")].lower() for platform in self.config.get(bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᐏ"), [])]
      bstack11111ll1l1_opy_ = sys.maxsize
      bstack1111l1l1l1_opy_ = bstack1l111l1_opy_ (u"ࠬ࠭ᐐ")
      for browser in bstack11111lll1l_opy_:
        if browser in self.bstack11111lllll_opy_:
          bstack11111llll1_opy_ = self.bstack11111lllll_opy_[browser]
        if bstack11111llll1_opy_ < bstack11111ll1l1_opy_:
          bstack11111ll1l1_opy_ = bstack11111llll1_opy_
          bstack1111l1l1l1_opy_ = browser
      return bstack1111l1l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡣࡧࡶࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᐑ").format(e))