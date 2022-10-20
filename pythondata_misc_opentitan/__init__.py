import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14848"
version_tuple = (0, 0, 14848)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14848")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14706"
data_version_tuple = (0, 0, 14706)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14706")
except ImportError:
    pass
data_git_hash = "9bbff6f01e352180891e7de2d35cffad07278133"
data_git_describe = "v0.0-14706-g9bbff6f01e"
data_git_msg = """\
commit 9bbff6f01e352180891e7de2d35cffad07278133
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 18 18:04:19 2022 -0700

    [dv,top-level] Fix all_escalation_resets test for flash_ctrl
    
    Capture the alert info dump to confirm the alert after the escalation reset.
    For flash_ctrl onlyh, ignore the check for ISRs having run, since flash
    accesses are blocked for flash_ctrl integrity errors.
    Provide a partial solution to #8945.
    Fixes a TODO in rstmgr_alert_info_test.c related to the creation of the
    C struct equivalent to the hardware bit stream for alert_info dump.
    Replaces some code that computes cycle counts from time durations by the
    corresponding code in alert_handler_testutils.
    
    Fixes #14899
    
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
