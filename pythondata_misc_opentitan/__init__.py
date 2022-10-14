import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14742"
version_tuple = (0, 0, 14742)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14742")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14600"
data_version_tuple = (0, 0, 14600)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14600")
except ImportError:
    pass
data_git_hash = "7ecb30fb49ff8951d97b88bb8b05d9d33a2932e6"
data_git_describe = "v0.0-14600-g7ecb30fb49"
data_git_msg = """\
commit 7ecb30fb49ff8951d97b88bb8b05d9d33a2932e6
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 13 16:41:37 2022 -0700

    [spi_device/dv] Exclude mbyte related FSM coverage
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
