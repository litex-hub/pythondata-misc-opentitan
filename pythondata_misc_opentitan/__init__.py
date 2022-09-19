import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14288"
version_tuple = (0, 0, 14288)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14288")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14146"
data_version_tuple = (0, 0, 14146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14146")
except ImportError:
    pass
data_git_hash = "fdbd80ef827b93d73480764b13c97e2153fafbed"
data_git_describe = "v0.0-14146-gfdbd80ef82"
data_git_msg = """\
commit fdbd80ef827b93d73480764b13c97e2153fafbed
Author: Weicai Yang <weicai@google.com>
Date:   Fri Sep 16 22:30:49 2022 -0700

    [spi_device/dv] Update spi_agent interface
    
    1. Updated interface to take sio as inout ports
    2. Fixed an issue caused by recent update that SPI host assigns z when it's idle, while
    the sio[1] is assigned with a DUT output.
    3. This enables chip-level to test dual/quad mode on SPI device
    
    Also fixed failed test - chip_sw_spi_device_tx_rx
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
