import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10255"
version_tuple = (0, 0, 10255)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10255")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10131"
data_version_tuple = (0, 0, 10131)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10131")
except ImportError:
    pass
data_git_hash = "971bb82ed72a996d71236107e0932ac184cd9749"
data_git_describe = "v0.0-10131-g971bb82ed"
data_git_msg = """\
commit 971bb82ed72a996d71236107e0932ac184cd9749
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Feb 10 10:17:17 2022 -0500

    [sw/silicon_creator] Directly use UART in shutdown_report_error()
    
    This change adds `shutdown_print()` that replaces usages of
    `log_printf()` in `shutdown_report_error()`.  `shutdown_report_error()`
    is also updated such that UART TX fifo is reset and TX is enabled before
    transmission. As a result, shutdown module no longer depends on the log
    library.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
