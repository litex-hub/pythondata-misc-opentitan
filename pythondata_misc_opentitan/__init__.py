import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15122"
version_tuple = (0, 0, 15122)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15122")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14980"
data_version_tuple = (0, 0, 14980)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14980")
except ImportError:
    pass
data_git_hash = "971782fde76e9ae79cd4d4b44fadd770f94b6b82"
data_git_describe = "v0.0-14980-g971782fde7"
data_git_msg = """\
commit 971782fde76e9ae79cd4d4b44fadd770f94b6b82
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Oct 28 15:28:41 2022 -0700

    Update rustfmt rule
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
