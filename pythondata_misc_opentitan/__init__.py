import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5856"
version_tuple = (0, 0, 5856)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5856")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5761"
data_version_tuple = (0, 0, 5761)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5761")
except ImportError:
    pass
data_git_hash = "338f58bd34d81870ab0b63aff1fc087ab5607f3d"
data_git_describe = "v0.0-5761-g338f58bd3"
data_git_msg = """\
commit 338f58bd34d81870ab0b63aff1fc087ab5607f3d
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Sat Apr 10 05:22:45 2021 -0700

    [sha3/lint] added waivers for sha3 lint msgs
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
