import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10783"
version_tuple = (0, 0, 10783)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10783")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10657"
data_version_tuple = (0, 0, 10657)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10657")
except ImportError:
    pass
data_git_hash = "7d681e5cfe327d0e348325faaadcaa9f9d1b472b"
data_git_describe = "v0.0-10657-g7d681e5cf"
data_git_msg = """\
commit 7d681e5cfe327d0e348325faaadcaa9f9d1b472b
Author: Alexander Williams <awill@google.com>
Date:   Mon Feb 14 07:56:08 2022 -0800

    [usbdev] Enable defaulting to NAK for OUT transactions
    
    Add a bit to change the behavior for OUT transactions to default to NAK
    without software intervention, for safe communication of responses to
    the host.
    Before this commit, the device could incorrectly communicate acceptance
    of a packet to the host if the firmware did not take action in time.
    Defaulting to NAK gives the firmware time, since this is a nonbinding
    condition--The device is merely saying, "Please try again later."
    
    Clear the rxenable_out bit in hardware when a packet is received. Update
    software code to match.
    
    This change could have deleterious effects on performance in some cases,
    but priority is given to safe handling of responses. For interfaces that
    may perform transactions when a buffer is available, do not set the
    set_nak_out bit for the corresponding endpoints.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
