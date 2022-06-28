import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12871"
version_tuple = (0, 0, 12871)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12871")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12729"
data_version_tuple = (0, 0, 12729)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12729")
except ImportError:
    pass
data_git_hash = "2994d340d76787f3ee9cc96aa30a2469b23b63fe"
data_git_describe = "v0.0-12729-g2994d340d7"
data_git_msg = """\
commit 2994d340d76787f3ee9cc96aa30a2469b23b63fe
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Jun 24 15:20:40 2022 +0000

    [dv,top,pwrmgr] deep_sleep_all_wake_ups regression fix
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
