import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11135"
version_tuple = (0, 0, 11135)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11135")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11009"
data_version_tuple = (0, 0, 11009)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11009")
except ImportError:
    pass
data_git_hash = "420cedc9ba81374804dbc7fb8db274bb7e476bd5"
data_git_describe = "v0.0-11009-g420cedc9b"
data_git_msg = """\
commit 420cedc9ba81374804dbc7fb8db274bb7e476bd5
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Fri Mar 25 10:50:47 2022 +0000

    [test, aes] Remove the aes_lc_escalate from test plan
    
     The aes_lc_escalate chip level test neither make sense nor can be
     implemented by software, because the aes IP will only be  notified
     by the Alert Handler from the escalation phase 1, as the phase
     1 is drastic enough to block the IBEX to fetch instructions and
     the only way to recover from this state is a system reset.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
