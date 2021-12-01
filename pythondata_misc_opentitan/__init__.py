import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8939"
version_tuple = (0, 0, 8939)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8939")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8827"
data_version_tuple = (0, 0, 8827)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8827")
except ImportError:
    pass
data_git_hash = "62ecce1a869eba33d65b112bab37258328adda55"
data_git_describe = "v0.0-8827-g62ecce1a8"
data_git_msg = """\
commit 62ecce1a869eba33d65b112bab37258328adda55
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Nov 23 16:54:36 2021 +0000

    [spi_device] Connect Readbuf Flip interrupt
    
    This commit connects the readbuf flip event into the interrupt line.
    The flip event may be high for multiple SCK cycles. The logic converts
    the signal into single cycle pulse to use prim_pulse_sync.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
