import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14465"
version_tuple = (0, 0, 14465)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14465")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14323"
data_version_tuple = (0, 0, 14323)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14323")
except ImportError:
    pass
data_git_hash = "b358d54a6b796d6a70d9c59f1741e45e31ad0479"
data_git_describe = "v0.0-14323-gb358d54a6b"
data_git_msg = """\
commit b358d54a6b796d6a70d9c59f1741e45e31ad0479
Author: Cindy <chencindy@google.com>
Date:   Tue Sep 27 20:00:18 2022 +0000

    [fpv] fix random seed syntax error
    
    FPV does not support rand dist and FPV_INIT with a non-constant.
    So this PR fixes the syntax error by using the default LFSR seed.
    
    Signed-off-by: Cindy <chencindy@google.com>

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
