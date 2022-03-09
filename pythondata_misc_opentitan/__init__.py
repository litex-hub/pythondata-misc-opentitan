import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10788"
version_tuple = (0, 0, 10788)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10788")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10662"
data_version_tuple = (0, 0, 10662)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10662")
except ImportError:
    pass
data_git_hash = "8ccce1c64a9cd0ce6039e33050ac1e8fad83bbb6"
data_git_describe = "v0.0-10662-g8ccce1c64"
data_git_msg = """\
commit 8ccce1c64a9cd0ce6039e33050ac1e8fad83bbb6
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 8 11:33:17 2022 -0800

    [dv/shadow_reg] Minor update on shadow_reg reset
    
    When we glitch reset in shadowed_regs, we predict error status before
    reset is issued, that might cause scb to clear the predicted value.
    So in this PR, we moved the error prediction after reset is finished.
    
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
