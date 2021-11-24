import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8858"
version_tuple = (0, 0, 8858)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8858")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8746"
data_version_tuple = (0, 0, 8746)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8746")
except ImportError:
    pass
data_git_hash = "6c83a36a39b09fd7cc87110cee0dd71c84b88f1e"
data_git_describe = "v0.0-8746-g6c83a36a3"
data_git_msg = """\
commit 6c83a36a39b09fd7cc87110cee0dd71c84b88f1e
Author: Weicai Yang <weicai@google.com>
Date:   Tue Nov 23 17:52:04 2021 -0800

    [sram/dv] Configure main sram Exec=1, ret sram Exec=0
    
    To align with #8973, only main sram supports instruction fetch
    
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
