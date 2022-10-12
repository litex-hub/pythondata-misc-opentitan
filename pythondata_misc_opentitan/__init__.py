import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14701"
version_tuple = (0, 0, 14701)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14701")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14559"
data_version_tuple = (0, 0, 14559)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14559")
except ImportError:
    pass
data_git_hash = "a49528cf0b786dcacdd12df4eeebc4a0d4633d84"
data_git_describe = "v0.0-14559-ga49528cf0b"
data_git_msg = """\
commit a49528cf0b786dcacdd12df4eeebc4a0d4633d84
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Wed Oct 5 05:22:44 2022 -0700

    Added misssing sec test and udpated sec doc
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
