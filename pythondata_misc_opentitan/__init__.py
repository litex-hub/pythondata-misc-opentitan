import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10555"
version_tuple = (0, 0, 10555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10429"
data_version_tuple = (0, 0, 10429)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10429")
except ImportError:
    pass
data_git_hash = "455ccc505c475b3c2b73aff8686359a1414076cc"
data_git_describe = "v0.0-10429-g455ccc505"
data_git_msg = """\
commit 455ccc505c475b3c2b73aff8686359a1414076cc
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 24 16:16:19 2022 -0800

    [fpv/rom_ctrl] Check connectivity for alerts in rom_ctrl
    
    This PR checks connectivity for sparse fsm alerts in rom_ctrl.
    This PR only brings up the script for rom_ctrl, but formal does not accept "$cast" function,
    so still need some work to make this property passing.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
