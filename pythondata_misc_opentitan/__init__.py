import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5170"
version_tuple = (0, 0, 5170)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5170")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5079"
data_version_tuple = (0, 0, 5079)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5079")
except ImportError:
    pass
data_git_hash = "144ca84e05878fb6b813bfe18c776c22eb287a3a"
data_git_describe = "v0.0-5079-g144ca84e0"
data_git_msg = """\
commit 144ca84e05878fb6b813bfe18c776c22eb287a3a
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Feb 26 15:46:43 2021 +0100

    [aes] Add life cycle escalation signal
    
    If the life cycle escalation signal is received, the main controller FSM
    of the AES unit locks up in the terminal error state. A reset is required.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
