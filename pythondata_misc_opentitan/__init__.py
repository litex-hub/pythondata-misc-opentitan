import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14972"
version_tuple = (0, 0, 14972)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14972")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14830"
data_version_tuple = (0, 0, 14830)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14830")
except ImportError:
    pass
data_git_hash = "ed90f5e1ee7826b27b89d846bce0a78961bb49e9"
data_git_describe = "v0.0-14830-ged90f5e1ee"
data_git_msg = """\
commit ed90f5e1ee7826b27b89d846bce0a78961bb49e9
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Oct 20 12:13:33 2022 +0100

    [dv, sram_ctl] Refactor the scramble_access test to use `CHECK_ARRAYS_NE`
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
