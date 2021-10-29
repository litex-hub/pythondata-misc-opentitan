import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8511"
version_tuple = (0, 0, 8511)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8511")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8399"
data_version_tuple = (0, 0, 8399)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8399")
except ImportError:
    pass
data_git_hash = "475a6e16c8440d13e15935c505741f298a03b6cb"
data_git_describe = "v0.0-8399-g475a6e16c"
data_git_msg = """\
commit 475a6e16c8440d13e15935c505741f298a03b6cb
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Oct 27 12:31:39 2021 -0700

    [dv/full_chip] Add rstmgr utils to help reset tests
    
    Add pre_reset and post_reset functions to prepare and check the rstmgr state.
    Add code to deal with the rstmgr cpu_info functionality, similar to alert_info.
    Add unit tests for the cpu_inf functionality.
    Change a couple pwrmgr tests to use these utilities.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
