import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8325"
version_tuple = (0, 0, 8325)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8325")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8213"
data_version_tuple = (0, 0, 8213)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8213")
except ImportError:
    pass
data_git_hash = "e041a961b1e8c3f57b19bd84ca1c44af215b4591"
data_git_describe = "v0.0-8213-ge041a961b"
data_git_msg = """\
commit e041a961b1e8c3f57b19bd84ca1c44af215b4591
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 18 14:23:59 2021 -0700

    [fpv/lint] Add lint target to secded modules
    
    This PR adds secded modules to FPV lint so we can check them in CI.
    
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
