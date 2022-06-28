import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12875"
version_tuple = (0, 0, 12875)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12875")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12733"
data_version_tuple = (0, 0, 12733)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12733")
except ImportError:
    pass
data_git_hash = "00d5622674f50d751d4aa0850e19d3149597db9c"
data_git_describe = "v0.0-12733-g00d5622674"
data_git_msg = """\
commit 00d5622674f50d751d4aa0850e19d3149597db9c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Jun 14 22:39:01 2022 +0200

    [topgen] Pass alias register paths into topgen for top RAL generation
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
