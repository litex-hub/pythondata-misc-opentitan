import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13183"
version_tuple = (0, 0, 13183)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13183")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13041"
data_version_tuple = (0, 0, 13041)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13041")
except ImportError:
    pass
data_git_hash = "23f837b7d09068a1d293a9dedbe86e29932b6e84"
data_git_describe = "v0.0-13041-g23f837b7d0"
data_git_msg = """\
commit 23f837b7d09068a1d293a9dedbe86e29932b6e84
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Jul 19 13:13:46 2022 -0700

    [dif/entropy_src] move to S2
    
    This updates the DIF checklists to move the SW to S2.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
