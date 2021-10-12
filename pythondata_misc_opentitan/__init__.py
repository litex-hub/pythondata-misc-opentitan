import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8233"
version_tuple = (0, 0, 8233)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8233")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8121"
data_version_tuple = (0, 0, 8121)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8121")
except ImportError:
    pass
data_git_hash = "52dac1e6cf8aedc8f8df3b0fe948081cde1262a8"
data_git_describe = "v0.0-8121-g52dac1e6c"
data_git_msg = """\
commit 52dac1e6cf8aedc8f8df3b0fe948081cde1262a8
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Sep 21 08:11:22 2021 -0700

    [opentitantool] Primitive bootstrap implementation
    
    1. Implement the primitive bootstrap protocol used by the opentitan boot_rom.
    2. Add a bootstrap command to the opentitantool CLI.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
