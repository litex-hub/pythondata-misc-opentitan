import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8494"
version_tuple = (0, 0, 8494)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8494")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8382"
data_version_tuple = (0, 0, 8382)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8382")
except ImportError:
    pass
data_git_hash = "316e177f937ca202fc9a05f30e22831f288d9708"
data_git_describe = "v0.0-8382-g316e177f9"
data_git_msg = """\
commit 316e177f937ca202fc9a05f30e22831f288d9708
Author: Jon Flatley <jflat@google.com>
Date:   Wed Aug 4 14:00:24 2021 -0400

    [sw/silicon_creator] Add program/erase to flash_ctrl
    
    Adds program and erase functionality to the mask rom flash_ctrl driver.
    
    Signed-off-by: Jon Flatley <jflat@google.com>

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
