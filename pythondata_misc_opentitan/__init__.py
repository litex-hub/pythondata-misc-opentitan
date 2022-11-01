import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15091"
version_tuple = (0, 0, 15091)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15091")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14949"
data_version_tuple = (0, 0, 14949)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14949")
except ImportError:
    pass
data_git_hash = "8aff88ccc12afd90179361987c611f07409e8410"
data_git_describe = "v0.0-14949-g8aff88ccc1"
data_git_msg = """\
commit 8aff88ccc12afd90179361987c611f07409e8410
Author: Miles Dai <milesdai@google.com>
Date:   Tue Nov 1 11:50:42 2022 -0400

    Revert "[edn] Tweak fifo clear logic"
    
    This reverts commit 3ad51c3b4fa9a10c865d9e9ea0b6b87266ebd392.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
