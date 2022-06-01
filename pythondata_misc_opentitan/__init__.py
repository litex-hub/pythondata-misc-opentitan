import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12448"
version_tuple = (0, 0, 12448)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12448")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12306"
data_version_tuple = (0, 0, 12306)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12306")
except ImportError:
    pass
data_git_hash = "ef893b7d3199c187084a5001bba1296ff921a37c"
data_git_describe = "v0.0-12306-gef893b7d3"
data_git_msg = """\
commit ef893b7d3199c187084a5001bba1296ff921a37c
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue May 31 13:47:06 2022 -0700

    doc(prim): Specify ICEBOX for prim_packer
    
    prim_packer needs empty signal for HMAC to set the idle state correctly.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
