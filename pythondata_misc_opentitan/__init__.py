import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8535"
version_tuple = (0, 0, 8535)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8535")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8423"
data_version_tuple = (0, 0, 8423)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8423")
except ImportError:
    pass
data_git_hash = "6e82bc60d2ce21b21ca79612707f57f22499fc43"
data_git_describe = "v0.0-8423-g6e82bc60d"
data_git_msg = """\
commit 6e82bc60d2ce21b21ca79612707f57f22499fc43
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Oct 27 21:25:59 2021 +0100

    [doc] Document Continuous Integration System
    
    Fixes #8326
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
