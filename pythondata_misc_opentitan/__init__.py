import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8214"
version_tuple = (0, 0, 8214)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8214")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8102"
data_version_tuple = (0, 0, 8102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8102")
except ImportError:
    pass
data_git_hash = "366c41832947783734e8026757903c7188e2d79a"
data_git_describe = "v0.0-8102-g366c41832"
data_git_msg = """\
commit 366c41832947783734e8026757903c7188e2d79a
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Fri Oct 8 09:37:21 2021 +0100

    [rstmgr] Add missing dependency on alert_handler_component
    
    `rstmgr.sv` uses `alert_pkg`. The package containing this file needs to
    be listed as dependency.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
