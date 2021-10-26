import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8463"
version_tuple = (0, 0, 8463)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8463")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8351"
data_version_tuple = (0, 0, 8351)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8351")
except ImportError:
    pass
data_git_hash = "c858b582d5aaa604afa2548ae0016adc321fc9c5"
data_git_describe = "v0.0-8351-gc858b582d"
data_git_msg = """\
commit c858b582d5aaa604afa2548ae0016adc321fc9c5
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Oct 23 01:35:25 2021 -0700

    [ spi_host, rtl ] AUTOGEN
    
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
