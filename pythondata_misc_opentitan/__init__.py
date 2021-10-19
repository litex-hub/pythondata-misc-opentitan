import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8345"
version_tuple = (0, 0, 8345)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8345")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8233"
data_version_tuple = (0, 0, 8233)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8233")
except ImportError:
    pass
data_git_hash = "e2de5d92977826085545844d155c36d2259edbaa"
data_git_describe = "v0.0-8233-ge2de5d929"
data_git_msg = """\
commit e2de5d92977826085545844d155c36d2259edbaa
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Oct 15 14:44:32 2021 -0700

    [ spi_host rtl ] Prepare to move entire SPI_HOST IP the peripheral clock domain
    
    This is the first of two commits which aim to standardize the CDC strategy for SPI_HOST
    
    In this first commit:
    
    - An explicit tlul_async_fifo is created inside spi_host.sv. This FIFO will eventually move
      to the TLUL fabric or the register interface.  However putting it inside the IP for now
      allows for testing of changes to other blocks without changing the interface, which would
      disrupt DV testing.
    
    - The command_cdc has been removed in favor of a shallow synchronous FIFO in
      spi_host_command_queue.
    
    - spi_host_data_cdc with its async fifos have also been removed in favor
      of spi_host_data_fifos, in which the fifos are synchronous
    
    Pending until next commit:
    
    - Migration of TLUL fifo to some automated system (TLUL fabric? Regtool?)
    - Removal of "Core" clocks & resets
    - Change COMMAND register to hw_ext
    - DV Interface updates to change clocks
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
