import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12414"
version_tuple = (0, 0, 12414)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12414")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12272"
data_version_tuple = (0, 0, 12272)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12272")
except ImportError:
    pass
data_git_hash = "00dd729d4f254732acb0fb47c545239551fd63b5"
data_git_describe = "v0.0-12272-g00dd729d4"
data_git_msg = """\
commit 00dd729d4f254732acb0fb47c545239551fd63b5
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri May 27 19:43:50 2022 +0000

    [clkmgr,dv] regression fix - shadow register error test
    
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
