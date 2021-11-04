import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8583"
version_tuple = (0, 0, 8583)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8583")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8471"
data_version_tuple = (0, 0, 8471)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8471")
except ImportError:
    pass
data_git_hash = "9036ea3133d98b8eac80473aa2460dbb7b83e8b0"
data_git_describe = "v0.0-8471-g9036ea313"
data_git_msg = """\
commit 9036ea3133d98b8eac80473aa2460dbb7b83e8b0
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Nov 4 14:08:53 2021 +0000

    [sw] Fix clkmgr smoketest
    
    The test aims to toggle all gateable and hintable clocks from disabled
    to enabled and back or vice versa. The state being checked for the
    toggle wasn't updated so everything just got disabled.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
