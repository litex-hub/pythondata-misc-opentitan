import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15283"
version_tuple = (0, 0, 15283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15141"
data_version_tuple = (0, 0, 15141)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15141")
except ImportError:
    pass
data_git_hash = "f3f2a41794c1cf2a143a941d5e52c1a5f5d248f4"
data_git_describe = "v0.0-15141-gf3f2a41794"
data_git_msg = """\
commit f3f2a41794c1cf2a143a941d5e52c1a5f5d248f4
Author: Fatih Balli <fatihballi@google.com>
Date:   Thu Nov 3 07:56:19 2022 -0700

    [chip-test, kmac] Check KMAC sideload
    
    Checks whether keymgr KMAC sideloading works correctly by comparing
    the result of a KMAC operation (which uses sideload hw key) with a test
    vector computed within dv.
    
    Signed-off-by: Fatih Balli <fatihballi@google.com>

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
