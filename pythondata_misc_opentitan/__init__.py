import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5804"
version_tuple = (0, 0, 5804)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5804")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5709"
data_version_tuple = (0, 0, 5709)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5709")
except ImportError:
    pass
data_git_hash = "6abe0ff0129c6e24ae170e2162869c9bd0c64902"
data_git_describe = "v0.0-5709-g6abe0ff01"
data_git_msg = """\
commit 6abe0ff0129c6e24ae170e2162869c9bd0c64902
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Apr 6 20:32:10 2021 +0200

    [kmac, sha3] Add separate Verilator lint waiver files, fix some warnings
    
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
