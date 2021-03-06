import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5272"
version_tuple = (0, 0, 5272)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5272")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5177"
data_version_tuple = (0, 0, 5177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5177")
except ImportError:
    pass
data_git_hash = "4047b0d0f29b2a22b2b8a96cbf1881bcd5b13990"
data_git_describe = "v0.0-5177-g4047b0d0f"
data_git_msg = """\
commit 4047b0d0f29b2a22b2b8a96cbf1881bcd5b13990
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Mar 2 16:57:54 2021 +0100

    [aes] Update design checklist to represent current state
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
