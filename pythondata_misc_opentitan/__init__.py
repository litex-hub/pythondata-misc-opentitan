import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12482"
version_tuple = (0, 0, 12482)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12482")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12340"
data_version_tuple = (0, 0, 12340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12340")
except ImportError:
    pass
data_git_hash = "9046e66b30af96a1f630a6c5d5706f4c6c1f0ac1"
data_git_describe = "v0.0-12340-g9046e66b3"
data_git_msg = """\
commit 9046e66b30af96a1f630a6c5d5706f4c6c1f0ac1
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Jun 1 15:41:58 2022 -0700

    chore(cdc): SPI_DEVICE static signals.
    
    - read pointer sits in SYS_CLK: no CDC path violation
    - control_abort to fwmode is in the same clock domain.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
