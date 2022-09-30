import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14518"
version_tuple = (0, 0, 14518)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14518")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14376"
data_version_tuple = (0, 0, 14376)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14376")
except ImportError:
    pass
data_git_hash = "0bb2c9b9039f8aef4ddc632296e58bee340ef075"
data_git_describe = "v0.0-14376-g0bb2c9b903"
data_git_msg = """\
commit 0bb2c9b9039f8aef4ddc632296e58bee340ef075
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Sep 29 15:41:36 2022 +0100

    [otbn,dv] Disable V2S assertions for FI tests
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
