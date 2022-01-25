import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9779"
version_tuple = (0, 0, 9779)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9779")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9657"
data_version_tuple = (0, 0, 9657)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9657")
except ImportError:
    pass
data_git_hash = "60837b92dbc8edf6edfe56c1f2a4c964c3868971"
data_git_describe = "v0.0-9657-g60837b92d"
data_git_msg = """\
commit 60837b92dbc8edf6edfe56c1f2a4c964c3868971
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Dec 21 10:02:45 2021 +0000

    [sw,crypto] Setup for OTBN utilities.
    
    After copying the utilities from silicon_creator, adjust the build logic
    to include them and do some minor cleanup (e.g. fix headers, remove
    unused imports).
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
