import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8331"
version_tuple = (0, 0, 8331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8219"
data_version_tuple = (0, 0, 8219)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8219")
except ImportError:
    pass
data_git_hash = "c9887c25978451831fe91bd0c00050dadceb4335"
data_git_describe = "v0.0-8219-gc9887c259"
data_git_msg = """\
commit c9887c25978451831fe91bd0c00050dadceb4335
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 18 12:35:37 2021 -0700

    [fpv] Add formal target to alert related FPV testbench
    
    This PR adds a formal target to the alert_handler related FPV testbench
    and their templates.
    
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
