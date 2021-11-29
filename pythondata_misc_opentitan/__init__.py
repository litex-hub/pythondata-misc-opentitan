import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8878"
version_tuple = (0, 0, 8878)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8878")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8766"
data_version_tuple = (0, 0, 8766)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8766")
except ImportError:
    pass
data_git_hash = "3bd6cebda2598e080aae62a3a81e36a60d7ee932"
data_git_describe = "v0.0-8766-g3bd6cebda"
data_git_msg = """\
commit 3bd6cebda2598e080aae62a3a81e36a60d7ee932
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Oct 22 09:43:26 2021 -0700

    [ spi_host, doc ] Update documentation to include deltas from recent PRs
    
    - Removes all discussion of the core clock domain
    - Eliminates all discussion of CDC's
      - One exception remains the description on "Back-to-Back Commands".
        This section will be updated in a forthcoming PR.
    - New class of error event associated with various "impossible" TX FIFO write
      events (i.e., zero-byte writes, or other writes not associated with any known
      processor data type.)
    - General cleaned up discussion of error events.
    - Documents the split of the DATA memory window into separate TXDATA/RXDATA windows
    - Implementation section: documents the split of the FSM `cmd_end` signal
      into `last_read` and `last_write` signals
    
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
