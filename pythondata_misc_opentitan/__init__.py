import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14554"
version_tuple = (0, 0, 14554)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14554")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14412"
data_version_tuple = (0, 0, 14412)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14412")
except ImportError:
    pass
data_git_hash = "71f19edb3fd7331291abd6c2bbe5c51557faba39"
data_git_describe = "v0.0-14412-g71f19edb3f"
data_git_msg = """\
commit 71f19edb3fd7331291abd6c2bbe5c51557faba39
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Oct 4 15:12:08 2022 -0700

    fix(spid): Latch FIFOADDR at correct time
    
    _Related Issue: https://github.com/lowRISC/opentitan/issues/15266_
    
    This PR fixes a bug for unaligned access in TPM read commands.
    
    fifoaddr is latched with the counter being `'h1F`. The counter, however,
    runs on SPI_CLK, while the latching logic is running on inverted SPI_CLK
    domain.
    
    As a result, the latching logic captures the fifo address at a cycle
    earlier with prematured address. So it always assume address[1] as
    address[0].
    
    This commit fixes the issue by:
    
    1. Convert `sck_fifoaddr_latch` into iSCK domain.
    2. To not shift the address one bit more, use `sck_cmdaddr_wdata_q`
       rather than `sck_cmdaddr_wdata_d`.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
