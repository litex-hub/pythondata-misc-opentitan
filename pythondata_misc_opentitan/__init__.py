import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8757"
version_tuple = (0, 0, 8757)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8757")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8645"
data_version_tuple = (0, 0, 8645)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8645")
except ImportError:
    pass
data_git_hash = "8bf33eadba36c7b9b469c393f1089a9c701d9317"
data_git_describe = "v0.0-8645-g8bf33eadb"
data_git_msg = """\
commit 8bf33eadba36c7b9b469c393f1089a9c701d9317
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Nov 16 22:34:31 2021 +0000

    [spi_device] Mailbox intercept logic.
    
    Mailbox is processed in readcmd submodule. If the received address falls
    into the mailbox region, the logic raises the intercept signal to assume
    the SPI and return data internally regardless of spi Flash or
    Passthrough mode.
    
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
