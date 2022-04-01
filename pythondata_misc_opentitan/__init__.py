import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11281"
version_tuple = (0, 0, 11281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11155"
data_version_tuple = (0, 0, 11155)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11155")
except ImportError:
    pass
data_git_hash = "56f1dbd6b7e30054d29b0da672e560e00be9d6e2"
data_git_describe = "v0.0-11155-g56f1dbd6b"
data_git_msg = """\
commit 56f1dbd6b7e30054d29b0da672e560e00be9d6e2
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Mar 31 14:04:17 2022 -0700

    [spi_device] Change addr_latched as a pulse
    
    Problem:
    
        `addr_latched_i` in `spid_readsram` module is expected to be a pulse
        signal. The `spi_readcmd` module generates the signal as a level by
        comparing `addr_cnt_d` with all zero value.
    
        As a result, the `strb` register in `spid_readsram` follows the
        current address, which is increased by when a byte is sent to the
        host system. However, the `spid_readsram` logic pushes the data into
        the FIFO already. As the FIFO depth is 2, one more entry has been
        added to the FIFO, which results the host system sees the a byte has
        been shifted.
    
    Resolution:
    
        Revised the `addr_latched` logic to be a pulse. Either `addr_cnt_d`
        or `addr_latched` can be revised. I chose the latter. Latching the
        latched signal and generated a pulse.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
