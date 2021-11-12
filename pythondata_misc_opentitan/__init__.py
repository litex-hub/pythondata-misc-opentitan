import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8693"
version_tuple = (0, 0, 8693)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8693")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8581"
data_version_tuple = (0, 0, 8581)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8581")
except ImportError:
    pass
data_git_hash = "88563757235dfc552e6a4bd03551d0b5c6156b9c"
data_git_describe = "v0.0-8581-g885637572"
data_git_msg = """\
commit 88563757235dfc552e6a4bd03551d0b5c6156b9c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Nov 11 12:11:39 2021 -0800

    [dv/alert_handler] Fix crashdump with reset
    
    This PR fixes a race condition between crashdump change and reset.
    
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
