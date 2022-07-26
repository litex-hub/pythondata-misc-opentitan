import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13264"
version_tuple = (0, 0, 13264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13122"
data_version_tuple = (0, 0, 13122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13122")
except ImportError:
    pass
data_git_hash = "507e9b3a2310cfe5829ab82b9cafeb564e7bf0c8"
data_git_describe = "v0.0-13122-g507e9b3a23"
data_git_msg = """\
commit 507e9b3a2310cfe5829ab82b9cafeb564e7bf0c8
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Jul 25 11:43:02 2022 -0700

    [entropy_src/rtl] add sha3 error status bit
    
    A fatal status bit is added for the case where a sha3 module error occurs.
    Additionally, an error test code is added to force this status bit on.
    Fixes #13823.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
