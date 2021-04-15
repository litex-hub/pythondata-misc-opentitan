import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5870"
version_tuple = (0, 0, 5870)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5870")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5775"
data_version_tuple = (0, 0, 5775)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5775")
except ImportError:
    pass
data_git_hash = "32655b71b78659f94d07b2f06575cb23f58c89c0"
data_git_describe = "v0.0-5775-g32655b71b"
data_git_msg = """\
commit 32655b71b78659f94d07b2f06575cb23f58c89c0
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Apr 1 21:38:30 2021 -0700

    [ spi_host ] SPI_HOST Implementation
    
    Register Changes:
    
    - Simplified Command structure to speed, direction, length, and CSAAT
    - CSAAT moved out of CONFIGOPTS
    - COMMAND register no longer a multi-reg
    - Added a separate CSID register
    - Added two new types of errors for command checking
    - Removed Manual CS feature
    - Made RX and TX FIFO come through the same register
    - Simplified all reset registers into one SW_RST
    - Renamed "BUSYERR" field to CMDBUSY, and homogenized dashes of similar registers
    - Harmonized all FIFO related sizes and quantities to word-units and
      8 bit sizes
    - ByteOrder now defaults to 1 (Little-Endian)
    - Clarified operation of ByteOrder in description of !!DATA register
    
    Inital implementation included
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
