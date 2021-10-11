import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8202"
version_tuple = (0, 0, 8202)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8202")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8090"
data_version_tuple = (0, 0, 8090)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8090")
except ImportError:
    pass
data_git_hash = "5038993e18395fc472ae02c103aa74b8b0e220d2"
data_git_describe = "v0.0-8090-g5038993e1"
data_git_msg = """\
commit 5038993e18395fc472ae02c103aa74b8b0e220d2
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Sep 30 06:32:20 2021 -0700

    [opentitantool] Refactor IO options for commonality
    
    1. Place UART and SPI bus parameters into their own structs.  Add
    `create` functions which apply the requested parameters when creating
    the requested IO interface.
    2. Use the Params structs in the `console` and `spi` commands.
    
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
