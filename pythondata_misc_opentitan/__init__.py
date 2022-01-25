import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9774"
version_tuple = (0, 0, 9774)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9774")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9652"
data_version_tuple = (0, 0, 9652)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9652")
except ImportError:
    pass
data_git_hash = "cf5bcb704e25ff981c8471078a28ec9be19542a2"
data_git_describe = "v0.0-9652-gcf5bcb704"
data_git_msg = """\
commit cf5bcb704e25ff981c8471078a28ec9be19542a2
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Jan 21 14:55:38 2022 -0800

    [entropy_src/rtl] Clear stats only on enable
    
    All statistics clear when the main enable is turned off.
    This is not good for post-processing of health test effectiveness.
    Fix is clear all when enabling.
    Fixes #10227.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
