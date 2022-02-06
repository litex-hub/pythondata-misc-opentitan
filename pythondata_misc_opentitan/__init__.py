import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10094"
version_tuple = (0, 0, 10094)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10094")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9970"
data_version_tuple = (0, 0, 9970)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9970")
except ImportError:
    pass
data_git_hash = "7ff8990d4eb390d268005e4a0aca3689fc84c503"
data_git_describe = "v0.0-9970-g7ff8990d4"
data_git_msg = """\
commit 7ff8990d4eb390d268005e4a0aca3689fc84c503
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 4 15:10:04 2022 -0800

    [fpv/script] Mark unreachable as failures
    
    Previously `unreachables` are marked as failure only in `cov_rate`.
    However, certain assertions can be unreachabled, and we should
    categorize that as failure.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
