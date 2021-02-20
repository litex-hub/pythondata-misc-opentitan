import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5079"
version_tuple = (0, 0, 5079)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5079")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4988"
data_version_tuple = (0, 0, 4988)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4988")
except ImportError:
    pass
data_git_hash = "802d472305d27808ae019a65a43525f1ab176556"
data_git_describe = "v0.0-4988-g802d47230"
data_git_msg = """\
commit 802d472305d27808ae019a65a43525f1ab176556
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Feb 19 16:55:36 2021 -0800

    [dv/alert_handler] fix regression error
    
    Two regression error fixes regarding alert_handler:
    1. Regwen switch from W1C to W0C, so writing 0 to the regwen will lock
    the lockable regs.
    2. Adding a reset when check escalation length, because reset is async
    and monitor counts on posedge while scb counts on negedge. If reset is
    in between the clock edge, there might be mismatch.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
