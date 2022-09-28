import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14468"
version_tuple = (0, 0, 14468)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14468")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14326"
data_version_tuple = (0, 0, 14326)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14326")
except ImportError:
    pass
data_git_hash = "0a24890956704735cddc5ee104a04944aeb60d04"
data_git_describe = "v0.0-14326-g0a24890956"
data_git_msg = """\
commit 0a24890956704735cddc5ee104a04944aeb60d04
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Sep 27 04:56:11 2022 +0000

    [flash_ctrl,dv] regression fix
    
    DV clean up for regression failtures 9/23
    
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
