import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12674"
version_tuple = (0, 0, 12674)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12674")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12532"
data_version_tuple = (0, 0, 12532)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12532")
except ImportError:
    pass
data_git_hash = "eba99e7b938c28e375a4b195e39103f3b9b4b45d"
data_git_describe = "v0.0-12532-geba99e7b9"
data_git_msg = """\
commit eba99e7b938c28e375a4b195e39103f3b9b4b45d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jun 13 17:07:10 2022 +0200

    [clkmgr] Allow transactional clock groups with just 1 clock
    
    This allows removing HMAC on English Breakfast to free some more FPGA
    resources.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
