import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9446"
version_tuple = (0, 0, 9446)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9446")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9328"
data_version_tuple = (0, 0, 9328)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9328")
except ImportError:
    pass
data_git_hash = "d136b23018dbd2a4f10abec13b2fde30e91438b6"
data_git_describe = "v0.0-9328-gd136b2301"
data_git_msg = """\
commit d136b23018dbd2a4f10abec13b2fde30e91438b6
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Jan 11 10:57:29 2022 -0800

    [pinmux/doc] Update sleep mode terminology
    
    Fix #9905
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
