import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8264"
version_tuple = (0, 0, 8264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8152"
data_version_tuple = (0, 0, 8152)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8152")
except ImportError:
    pass
data_git_hash = "e10832013c8f4e4969732f4e96831c9e39c7b82c"
data_git_describe = "v0.0-8152-ge10832013"
data_git_msg = """\
commit e10832013c8f4e4969732f4e96831c9e39c7b82c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Oct 13 17:40:24 2021 -0700

    [chip/testplan] Add alert ping output
    
    This PR addes a testplan entry about alert handler ping timeout.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
