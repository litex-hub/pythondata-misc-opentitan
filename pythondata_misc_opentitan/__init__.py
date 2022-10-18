import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14810"
version_tuple = (0, 0, 14810)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14810")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14668"
data_version_tuple = (0, 0, 14668)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14668")
except ImportError:
    pass
data_git_hash = "54fa34484ef4ac6cfcf1f054bb4f283e08a211b1"
data_git_describe = "v0.0-14668-g54fa34484e"
data_git_msg = """\
commit 54fa34484ef4ac6cfcf1f054bb4f283e08a211b1
Author: Weicai Yang <weicai@google.com>
Date:   Fri Oct 14 12:14:38 2022 -0700

    [spi_device/dv] Update CSR exclusions
    
    Removed some unnecessary exclusions
    
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
