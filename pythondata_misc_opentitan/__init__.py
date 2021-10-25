import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8440"
version_tuple = (0, 0, 8440)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8440")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8328"
data_version_tuple = (0, 0, 8328)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8328")
except ImportError:
    pass
data_git_hash = "116abc28855890a28010dc1a386dcbf270850083"
data_git_describe = "v0.0-8328-g116abc288"
data_git_msg = """\
commit 116abc28855890a28010dc1a386dcbf270850083
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Oct 22 13:44:43 2021 -0700

    [spi_host] shift in correct bit
    
    In Single mode, we should be shifting in sd_i[1] (nee MISO).
    
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
