import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9328"
version_tuple = (0, 0, 9328)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9328")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9211"
data_version_tuple = (0, 0, 9211)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9211")
except ImportError:
    pass
data_git_hash = "9336f6d03fe6154c7d621d962d5eb402eb1c0332"
data_git_describe = "v0.0-9211-g9336f6d03"
data_git_msg = """\
commit 9336f6d03fe6154c7d621d962d5eb402eb1c0332
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Dec 16 17:42:45 2021 +0000

    [spi_device] Add `addr_swap_en` to the swap condition
    
    While adding `payload_swap_en` field in CMD_INFO, I missed to add
    `addr_swap_en` to the swap enable condition. This commit revises to use
    the config in CMD_INFO.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
