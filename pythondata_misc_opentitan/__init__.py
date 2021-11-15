import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8716"
version_tuple = (0, 0, 8716)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8716")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8604"
data_version_tuple = (0, 0, 8604)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8604")
except ImportError:
    pass
data_git_hash = "1c5b13c2fb07dbb5956f771443a372c46f6f1ac5"
data_git_describe = "v0.0-8604-g1c5b13c2f"
data_git_msg = """\
commit 1c5b13c2fb07dbb5956f771443a372c46f6f1ac5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Nov 12 16:39:57 2021 -0800

    [dv/flash_ctrl] Add shadow_reg tests
    
    This PR adds the auto generated shadow reg tests for flash_ctrl.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
