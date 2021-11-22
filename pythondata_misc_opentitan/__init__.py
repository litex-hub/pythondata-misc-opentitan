import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8820"
version_tuple = (0, 0, 8820)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8820")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8708"
data_version_tuple = (0, 0, 8708)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8708")
except ImportError:
    pass
data_git_hash = "4f66423b1910df210908adb23507055f27ec6eae"
data_git_describe = "v0.0-8708-g4f66423b1"
data_git_msg = """\
commit 4f66423b1910df210908adb23507055f27ec6eae
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Nov 18 18:03:12 2021 +0000

    [spi_device] Revise Block Diagram
    
    This commit updates the SPI_DEVICE HWIP block diagram.
    
    The IP has been updated to support Flash mode, Passthrough mode, and TPM
    mode. The block diagram hasn't been updated to represent the changes.
    
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
