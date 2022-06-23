import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12804"
version_tuple = (0, 0, 12804)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12804")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12662"
data_version_tuple = (0, 0, 12662)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12662")
except ImportError:
    pass
data_git_hash = "c1e8b95ccd95ecdcac82ba5e20c63dd4ed3c5963"
data_git_describe = "v0.0-12662-gc1e8b95ccd"
data_git_msg = """\
commit c1e8b95ccd95ecdcac82ba5e20c63dd4ed3c5963
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri May 27 23:33:26 2022 +0100

    [otbn] Remove un-needed Verilator waiver
    
    This isn't needed now that we've refactored how error bits get passed
    around.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
