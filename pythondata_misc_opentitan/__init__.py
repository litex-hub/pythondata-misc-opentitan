import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5883"
version_tuple = (0, 0, 5883)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5883")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5788"
data_version_tuple = (0, 0, 5788)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5788")
except ImportError:
    pass
data_git_hash = "69b1c4225ffefde014c8e45efd17802c1b6d426d"
data_git_describe = "v0.0-5788-g69b1c4225"
data_git_msg = """\
commit 69b1c4225ffefde014c8e45efd17802c1b6d426d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Wed Apr 14 12:29:34 2021 +0200

    [aes] Fix and realign LEC script for the different combinational S-Boxes
    
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
