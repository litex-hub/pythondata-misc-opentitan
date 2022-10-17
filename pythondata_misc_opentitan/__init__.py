import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14782"
version_tuple = (0, 0, 14782)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14782")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14640"
data_version_tuple = (0, 0, 14640)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14640")
except ImportError:
    pass
data_git_hash = "8a6b83dbfd0fab3d725f66a509294be11352d9e0"
data_git_describe = "v0.0-14640-g8a6b83dbfd"
data_git_msg = """\
commit 8a6b83dbfd0fab3d725f66a509294be11352d9e0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 13 15:58:49 2022 -0700

    [dv/lc_ctrl] Update coverage exclusion file
    
    This PR updates lc_ctrl's coverage exclusion file:
    1). Removed the V2 only exclusion file
    2). Add exclusion file to exclude any non-idle state to InvalidSt.
      Because they are fully covered by FPV testbench.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
