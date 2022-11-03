import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15210"
version_tuple = (0, 0, 15210)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15210")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15068"
data_version_tuple = (0, 0, 15068)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15068")
except ImportError:
    pass
data_git_hash = "f82627c017668f182a66b74d51b31ab52790cac5"
data_git_describe = "v0.0-15068-gf82627c017"
data_git_msg = """\
commit f82627c017668f182a66b74d51b31ab52790cac5
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Nov 3 12:04:13 2022 -0700

    [dv,flash_ctrl,escalation] Expect ISR should not run
    
    Check that when the flash_ctrl gets a fatal fault it should block flash
    accesses. The chip_sw_all_escalation_resets test was allowing ISR not to
    run when flash_ctrl faults occur, this change causes a failure if an ISR
    actually runs.
    
    Fixes #15971
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
