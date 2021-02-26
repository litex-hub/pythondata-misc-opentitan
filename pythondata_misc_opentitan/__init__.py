import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5165"
version_tuple = (0, 0, 5165)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5165")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5074"
data_version_tuple = (0, 0, 5074)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5074")
except ImportError:
    pass
data_git_hash = "ff5a23bd27248e958ac2a48061d7406684daefb7"
data_git_describe = "v0.0-5074-gff5a23bd2"
data_git_msg = """\
commit ff5a23bd27248e958ac2a48061d7406684daefb7
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Feb 26 10:16:10 2021 -0800

    [fpv] TLUL_pkg compile error
    
    This PR fixes a small compile error due to enum casting in tlul_pkg.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
