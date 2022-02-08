import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10122"
version_tuple = (0, 0, 10122)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10122")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9998"
data_version_tuple = (0, 0, 9998)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9998")
except ImportError:
    pass
data_git_hash = "58f5ad256abf6c6d69622e192028748beff687ad"
data_git_describe = "v0.0-9998-g58f5ad256"
data_git_msg = """\
commit 58f5ad256abf6c6d69622e192028748beff687ad
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Feb 7 15:30:11 2022 -0800

    [kmac/rtl,DV] Alignment on swapping alerts order
    
    This PR follows PR #10517 which swaps the order of fatal and recoverable
    alerts. With that PR, now alert[0] is recoverable alert and alert[1] is
    fatal alert.
    With this change, we would like to update the alert_test register as
    well, so now:
    alert_test field[0] corresponds to recov_operation_err
    alert_test field[1] corresponds to fatal_fault_err
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
