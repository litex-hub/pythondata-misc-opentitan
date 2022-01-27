import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9828"
version_tuple = (0, 0, 9828)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9828")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9706"
data_version_tuple = (0, 0, 9706)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9706")
except ImportError:
    pass
data_git_hash = "a993c4b23d936609e91b1fbea6d8a3d4001d9bea"
data_git_describe = "v0.0-9706-ga993c4b23"
data_git_msg = """\
commit a993c4b23d936609e91b1fbea6d8a3d4001d9bea
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Jan 25 19:10:19 2022 +0100

    [aes] Fix AscentLint errors
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
