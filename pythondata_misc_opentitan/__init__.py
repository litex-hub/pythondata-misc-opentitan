import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10603"
version_tuple = (0, 0, 10603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10477"
data_version_tuple = (0, 0, 10477)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10477")
except ImportError:
    pass
data_git_hash = "8d91bec38a7606e6418785e9de718c9063f61242"
data_git_describe = "v0.0-10477-g8d91bec38"
data_git_msg = """\
commit 8d91bec38a7606e6418785e9de718c9063f61242
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 25 18:17:13 2022 -0800

    [fpv/sec] Add some workaround logic for $cast keyword
    
    Because FPV does not accept $cast keyword, this PR adds some workaround
    logic to bypass that.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
