import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9402"
version_tuple = (0, 0, 9402)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9402")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9284"
data_version_tuple = (0, 0, 9284)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9284")
except ImportError:
    pass
data_git_hash = "1d09fe63935b80842a13096f52fd0a09a9f57bd2"
data_git_describe = "v0.0-9284-g1d09fe639"
data_git_msg = """\
commit 1d09fe63935b80842a13096f52fd0a09a9f57bd2
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jan 10 08:57:46 2022 -0800

    [pinmux/doc] Minor update
    
    This removes the "chicken" switch terminology from sram_ctrl docs,
    as it may be confusing.
    
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
