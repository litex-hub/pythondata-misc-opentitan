import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8568"
version_tuple = (0, 0, 8568)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8568")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8456"
data_version_tuple = (0, 0, 8456)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8456")
except ImportError:
    pass
data_git_hash = "0d0f7aed6f4dbd1f00c229fc41ce0f999ac18de7"
data_git_describe = "v0.0-8456-g0d0f7aed6"
data_git_msg = """\
commit 0d0f7aed6f4dbd1f00c229fc41ce0f999ac18de7
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Oct 21 18:28:49 2021 +0000

    [spi_device] Add Upload TB
    
    This commit implements a TB runs simple upload function. It uploads a
    couple of commands and checks the content inside the SRAM.
    
    - Command only
    - Command and Address
    - Command and Payload
    - Command / Address / Payload
    
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
