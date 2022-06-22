import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12781"
version_tuple = (0, 0, 12781)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12781")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12639"
data_version_tuple = (0, 0, 12639)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12639")
except ImportError:
    pass
data_git_hash = "1013e5fa4481e4b4fad1eef1202e2d7006925c57"
data_git_describe = "v0.0-12639-g1013e5fa44"
data_git_msg = """\
commit 1013e5fa4481e4b4fad1eef1202e2d7006925c57
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Apr 4 18:37:17 2022 +0100

    [sw,crypto] Ed25519 point addition implementation.
    
    Implementation and a quick OTBN-simulator test for Ed25519 point
    addition using extended twisted Edwards coordinates (following RFC
    8032).
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
