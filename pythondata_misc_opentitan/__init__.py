import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5413"
version_tuple = (0, 0, 5413)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5413")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5318"
data_version_tuple = (0, 0, 5318)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5318")
except ImportError:
    pass
data_git_hash = "545a28d239e9b6bd3dddd74e4693bfea046c4672"
data_git_describe = "v0.0-5318-g545a28d23"
data_git_msg = """\
commit 545a28d239e9b6bd3dddd74e4693bfea046c4672
Author: Weicai Yang <weicai@google.com>
Date:   Fri Mar 12 14:45:51 2021 -0800

    [spi_device/dv] Fix regression timeout
    
    mem size is increased recently, made these changes to avoid timeout
    1. increase max timeout timer to 1.5s, 1s takes a bit over 1hr
    2. reduce num_trans in spi_device_fifo_underflow_overflow_vseq
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
