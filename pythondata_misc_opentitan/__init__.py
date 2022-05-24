import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12299"
version_tuple = (0, 0, 12299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12171"
data_version_tuple = (0, 0, 12171)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12171")
except ImportError:
    pass
data_git_hash = "416467bc10f2da23b5da77b699ae25ba95930def"
data_git_describe = "v0.0-12171-g416467bc1"
data_git_msg = """\
commit 416467bc10f2da23b5da77b699ae25ba95930def
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon May 23 11:00:56 2022 -0700

    [lc_ctrl/doc] Minor doc corrections and clarifications
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
