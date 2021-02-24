import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5129"
version_tuple = (0, 0, 5129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5038"
data_version_tuple = (0, 0, 5038)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5038")
except ImportError:
    pass
data_git_hash = "8318ceab65ef9d4e8751fe0706314618e2b57a96"
data_git_describe = "v0.0-5038-g8318ceab6"
data_git_msg = """\
commit 8318ceab65ef9d4e8751fe0706314618e2b57a96
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Feb 24 12:39:55 2021 +0000

    [otbn] Add parameter defaults to otbn_trace_if
    
    Xcellium requires these.
    
    Fixes #5355
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
