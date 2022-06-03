import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12498"
version_tuple = (0, 0, 12498)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12498")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12356"
data_version_tuple = (0, 0, 12356)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12356")
except ImportError:
    pass
data_git_hash = "4f106efab24430ef45d4a7d98e0a1a6cf6991b66"
data_git_describe = "v0.0-12356-g4f106efab"
data_git_msg = """\
commit 4f106efab24430ef45d4a7d98e0a1a6cf6991b66
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue May 31 14:11:06 2022 -0700

    [reggen] Update licencing info for generated files
    
    Opensource council has approved licensing the generated output under
    both Apache and MIT licenses.
    
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
