import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8656"
version_tuple = (0, 0, 8656)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8656")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8544"
data_version_tuple = (0, 0, 8544)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8544")
except ImportError:
    pass
data_git_hash = "edf6e915ba3b0f20d551754493b0f8426250833e"
data_git_describe = "v0.0-8544-gedf6e915b"
data_git_msg = """\
commit edf6e915ba3b0f20d551754493b0f8426250833e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 9 11:26:01 2021 -0800

    [dv/alert_handler] fix alert ping timeout seq regression error
    
    This PR fixes the timeout issue in nightly regression regarding
    alert_handler_ping_timeout_vseq.
    The issue is that we locked the ping_en register via regwen before
    enabling the ping_en csr.
    The solution is to move the order of regwen write task.
    
    This PR also sets the min number of alert_en to be NUM_ALERTS-4 to avoid
    this sequence running too long.
    
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
