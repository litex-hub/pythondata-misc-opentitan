import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12850"
version_tuple = (0, 0, 12850)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12850")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12708"
data_version_tuple = (0, 0, 12708)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12708")
except ImportError:
    pass
data_git_hash = "a7319457e049f55bd628badcd48630d339363eff"
data_git_describe = "v0.0-12708-ga7319457e0"
data_git_msg = """\
commit a7319457e049f55bd628badcd48630d339363eff
Author: Alexander Williams <awill@google.com>
Date:   Fri Jun 24 10:24:56 2022 -0700

    [usbdev] Fix OUT ZLP handling under FIFO errors
    
    Previously, zero-length packets could elicit an ACK response even when
    the AV FIFO is empty or the RX FIFO is full. In the OUT transaction
    state machine, the state of the FIFOs was only checked when data would
    be written to a buffer. However, in usbdev_usbif, the transaction would
    be rejected, so the host would incorrectly think its packet reached the
    device.
    
    Fix this up by having the state machine also check FIFO states upon
    reaching the decision point for a handshake phase. This will be the
    final gate that will reject ZLPs that can't get an entry for the RX
    FIFO.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
