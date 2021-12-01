import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8934"
version_tuple = (0, 0, 8934)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8934")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8822"
data_version_tuple = (0, 0, 8822)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8822")
except ImportError:
    pass
data_git_hash = "6193adbcacd4b45e85c1f1a160004cc364b71558"
data_git_describe = "v0.0-8822-g6193adbca"
data_git_msg = """\
commit 6193adbcacd4b45e85c1f1a160004cc364b71558
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Nov 23 01:01:29 2021 +0000

    [spi_device] Connect watermark to interrupt source
    
    This commit connects the watermark event to the interrupt source.
    
    watermark event occurs in SCK domain. The logic registers the comb
    signal at SCK then pulse sync the signal into the bus clock domain
    (sck_).
    
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
