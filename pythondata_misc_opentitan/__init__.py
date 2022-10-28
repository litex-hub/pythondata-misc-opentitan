import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15019"
version_tuple = (0, 0, 15019)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15019")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14877"
data_version_tuple = (0, 0, 14877)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14877")
except ImportError:
    pass
data_git_hash = "64ea3bd268b0ad00e771aa65d735a3a89a7febcb"
data_git_describe = "v0.0-14877-g64ea3bd268"
data_git_msg = """\
commit 64ea3bd268b0ad00e771aa65d735a3a89a7febcb
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Sep 26 18:08:11 2022 +0200

    [top_englishbreakfast] Update dir list to delete before running topgen
    
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
