import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12935"
version_tuple = (0, 0, 12935)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12935")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12793"
data_version_tuple = (0, 0, 12793)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12793")
except ImportError:
    pass
data_git_hash = "6d81f51f41d809e7bb030cc36291338ea567e870"
data_git_describe = "v0.0-12793-g6d81f51f41"
data_git_msg = """\
commit 6d81f51f41d809e7bb030cc36291338ea567e870
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Jul 1 08:51:37 2022 -0400

    [bazel] Enable e2e_bootup_success test
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
