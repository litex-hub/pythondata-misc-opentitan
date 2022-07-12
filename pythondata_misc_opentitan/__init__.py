import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13045"
version_tuple = (0, 0, 13045)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13045")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12903"
data_version_tuple = (0, 0, 12903)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12903")
except ImportError:
    pass
data_git_hash = "52f7da058f43ce5d976841f48091366788496862"
data_git_describe = "v0.0-12903-g52f7da058f"
data_git_msg = """\
commit 52f7da058f43ce5d976841f48091366788496862
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jun 30 17:38:14 2022 -0700

    [clkmgr/prim] Make frequency measurement disable more robust
    
    - handles part of #13489
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
