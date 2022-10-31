import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15062"
version_tuple = (0, 0, 15062)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15062")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14920"
data_version_tuple = (0, 0, 14920)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14920")
except ImportError:
    pass
data_git_hash = "84018ef7fb67ea5d8c3427c904c6ea0768291eab"
data_git_describe = "v0.0-14920-g84018ef7fb"
data_git_msg = """\
commit 84018ef7fb67ea5d8c3427c904c6ea0768291eab
Author: Bilgiday Yuce <bilgiday@google.com>
Date:   Thu Oct 20 14:10:51 2022 +0200

    [alert_handler] Add alert_handler_lpg_reset_toggle_test
    
    Code to implement the chip_sw_alert_handler_reset_toggle_test described
    in #14130.
    
    /sw/device/tests/alert_handler_lpg_reset_toggle.c:
       - 2 test phases
          - Phase 0: Negative test (ping_timeout =2, FPGA-only)
          - Phase 1: Official test (ping_timeout=256, FPGA+DV)
    
    Signed-off-by: Bilgiday Yuce <bilgiday@google.com>

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
