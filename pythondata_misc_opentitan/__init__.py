import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8144"
version_tuple = (0, 0, 8144)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8144")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8036"
data_version_tuple = (0, 0, 8036)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8036")
except ImportError:
    pass
data_git_hash = "037bfc2050f481b4d5e673d2cc008ceb3fc013e0"
data_git_describe = "v0.0-8036-g037bfc205"
data_git_msg = """\
commit 037bfc2050f481b4d5e673d2cc008ceb3fc013e0
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 5 10:13:58 2021 -0700

    [dv/full_chip] Create pwrmgr testutils
    
    There are many tests that need to trigger wakeups from different IPs,
    so this abstracts one of the common pwrmgr operation.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post108"
tool_version_tuple = (0, 0, 108)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post108")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
