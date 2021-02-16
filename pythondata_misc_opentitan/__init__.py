import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post4999"
version_tuple = (0, 0, 4999)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post4999")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4908"
data_version_tuple = (0, 0, 4908)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4908")
except ImportError:
    pass
data_git_hash = "1a0a024c15070125447b61314351125c498cf6f8"
data_git_describe = "v0.0-4908-g1a0a024c1"
data_git_msg = """\
commit 1a0a024c15070125447b61314351125c498cf6f8
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Dec 17 12:06:23 2020 +0000

    [AON timer] Initial rtl commit
    
    This commit adds the basic timers, registers and CDC for the AON wakeup
    and watchdog timers.
    
    There is one functional change to the HJSON, which is to add a wakeup
    cause register. This register is written to zero by software to clear
    the wakeup request (similar to pinmux wakeup).
    
    CDC logic for register writes is currently not very sensible (a four
    entry async fifo for every register). There are TODOs covering this and
    it will be improved in subsequent updates.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
