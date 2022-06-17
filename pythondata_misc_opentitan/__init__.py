import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12733"
version_tuple = (0, 0, 12733)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12733")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12591"
data_version_tuple = (0, 0, 12591)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12591")
except ImportError:
    pass
data_git_hash = "3a4fa3a334a4f721de713086ffb271af67104781"
data_git_describe = "v0.0-12591-g3a4fa3a33"
data_git_msg = """\
commit 3a4fa3a334a4f721de713086ffb271af67104781
Author: Joshua Park <jeoong@google.com>
Date:   Thu Jun 9 15:08:14 2022 -0700

    [dv|pwrmgr] added pwrmgr_deep_sleep_all_reset_reqs and pwrmgr_normal_sleep_all_reset_reqs
    
    Signed-off-by: Joshua Park <jeoong@google.com>

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
