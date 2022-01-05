import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9343"
version_tuple = (0, 0, 9343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9226"
data_version_tuple = (0, 0, 9226)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9226")
except ImportError:
    pass
data_git_hash = "2525a63545c489f42167bcfd1f563c5e083e757b"
data_git_describe = "v0.0-9226-g2525a6354"
data_git_msg = """\
commit 2525a63545c489f42167bcfd1f563c5e083e757b
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 4 18:56:10 2022 -0800

    [dv/pwrmgr] Add escalation reset
    
    Connect alert_esc_agent and cfg to environment.
    Use escalation interface in testbench.
    Remove useless ndm system reset inputs in pwrmgr_rstmgr SVA.
    Add timeout if a WFI doesn't occur when transitioning to low power
    for the sake of simplicity.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
