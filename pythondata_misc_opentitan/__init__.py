import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5320"
version_tuple = (0, 0, 5320)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5320")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5225"
data_version_tuple = (0, 0, 5225)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5225")
except ImportError:
    pass
data_git_hash = "0fdf008758da0afbccad7b8d2a9772e3631d5d18"
data_git_describe = "v0.0-5225-g0fdf00875"
data_git_msg = """\
commit 0fdf008758da0afbccad7b8d2a9772e3631d5d18
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 9 16:39:48 2021 +0000

    [spi_host] Add missing connection to scanmode_i
    
    The module gained the port in dbd087ed00 but we forgot to add the flag
    in the hjson to get topgen to wire it up for us. This causes Verilator
    lint errors.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
