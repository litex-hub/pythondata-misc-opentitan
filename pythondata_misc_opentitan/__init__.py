import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8402"
version_tuple = (0, 0, 8402)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8402")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8290"
data_version_tuple = (0, 0, 8290)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8290")
except ImportError:
    pass
data_git_hash = "e956f7755eeb6fd12d04e6b8f0a40e25c47824ab"
data_git_describe = "v0.0-8290-ge956f7755"
data_git_msg = """\
commit e956f7755eeb6fd12d04e6b8f0a40e25c47824ab
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 21 17:19:52 2021 -0700

    [top/dv] Update testplan to add chip_sw_uart_rand_baudrate
    
    This will fix the unmapped test issue
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
