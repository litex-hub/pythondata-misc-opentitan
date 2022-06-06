import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12539"
version_tuple = (0, 0, 12539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12397"
data_version_tuple = (0, 0, 12397)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12397")
except ImportError:
    pass
data_git_hash = "93c8f594a707b916dfac7f11bb83add3475295f5"
data_git_describe = "v0.0-12397-g93c8f594a"
data_git_msg = """\
commit 93c8f594a707b916dfac7f11bb83add3475295f5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jun 6 11:36:11 2022 -0700

    [dv/alert_handler] Add common sec_cm test for alert_handler
    
    Alert_handler does not have alerts, so sec_cm violation will directly
    fires escalations or causes a local alert.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
