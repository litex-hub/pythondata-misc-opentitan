import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14524"
version_tuple = (0, 0, 14524)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14524")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14382"
data_version_tuple = (0, 0, 14382)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14382")
except ImportError:
    pass
data_git_hash = "2678e0a9d03b75e0529c84339f0585b4b852dc9e"
data_git_describe = "v0.0-14382-g2678e0a9d0"
data_git_msg = """\
commit 2678e0a9d03b75e0529c84339f0585b4b852dc9e
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Sep 26 15:38:22 2022 +0000

    [pwrmgr,dv] Add manual exclusion file.
    
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
