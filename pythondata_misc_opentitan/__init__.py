import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9915"
version_tuple = (0, 0, 9915)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9915")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9791"
data_version_tuple = (0, 0, 9791)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9791")
except ImportError:
    pass
data_git_hash = "deca537cd8e7337c54451c68ceecd599f2c07a0e"
data_git_describe = "v0.0-9791-gdeca537cd"
data_git_msg = """\
commit deca537cd8e7337c54451c68ceecd599f2c07a0e
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jan 27 15:14:35 2022 -0800

    [dv/rstmgr] Check alert and cpu info in reset test
    
    Update testplan for the added checks in reset sequence.
    Fix pwrmgr_rstmgr SVA to ignore checks on pwrmgr rstreqs outputs
    based on a parameter.
    Fix rstmgr_sw_rst SVA, especially clocking being per the target
    peripheral.
    Fix max_outstanding_req for coverage.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
