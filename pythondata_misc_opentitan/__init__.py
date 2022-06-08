import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12575"
version_tuple = (0, 0, 12575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12433"
data_version_tuple = (0, 0, 12433)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12433")
except ImportError:
    pass
data_git_hash = "6dd0874d4cb7185622aa1dd4112112fd7f56684e"
data_git_describe = "v0.0-12433-g6dd0874d4"
data_git_msg = """\
commit 6dd0874d4cb7185622aa1dd4112112fd7f56684e
Author: Joshua Park <jeoong@google.com>
Date:   Mon Jun 6 23:43:52 2022 -0700

    [dv/pwrmgr] renamed pwrmgr_deep_sleep_sysrst_reqs to pwrmgr_random_sleep_al_reset_reqs
    
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
