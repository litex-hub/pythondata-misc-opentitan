import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8412"
version_tuple = (0, 0, 8412)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8412")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8300"
data_version_tuple = (0, 0, 8300)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8300")
except ImportError:
    pass
data_git_hash = "fec1499e66dc6d513d24373305a4761042200f6c"
data_git_describe = "v0.0-8300-gfec1499e6"
data_git_msg = """\
commit fec1499e66dc6d513d24373305a4761042200f6c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 22 15:23:29 2021 +0100

    [rom_ctrl,dv] Fully disable the scoreboard for CSR tests
    
    We were previously seeing occasional failures in tests like
    rom_ctrl_csr_hw_reset. The problem is that the test does a few memory
    transactions and then ends. But rom_ctrl might not have finished its
    work!
    
    The scoreboard is "disabled" by setting en_scb = 0 in the base
    environment, but we don't actually disable it: everything is still
    connected up and running. Thus the scoreboard itself needs to know to
    drain and ignore all analysis fifos and not do any checking.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
