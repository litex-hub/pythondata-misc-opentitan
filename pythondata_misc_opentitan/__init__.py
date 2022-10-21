import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14884"
version_tuple = (0, 0, 14884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14742"
data_version_tuple = (0, 0, 14742)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14742")
except ImportError:
    pass
data_git_hash = "8b1c3bd1c8bf2d8194b4e966fc7de77ad55ee5fe"
data_git_describe = "v0.0-14742-g8b1c3bd1c8"
data_git_msg = """\
commit 8b1c3bd1c8bf2d8194b4e966fc7de77ad55ee5fe
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 20 15:31:39 2022 -0700

    [spi_device/dv] Add a test to verify memory parity error
    
    For #9613
    
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
