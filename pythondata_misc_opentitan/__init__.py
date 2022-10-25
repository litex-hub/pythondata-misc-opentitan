import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14941"
version_tuple = (0, 0, 14941)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14941")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14799"
data_version_tuple = (0, 0, 14799)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14799")
except ImportError:
    pass
data_git_hash = "4580a1765e7b5bd9a5f96c71f89e746e6c27c95d"
data_git_describe = "v0.0-14799-g4580a1765e"
data_git_msg = """\
commit 4580a1765e7b5bd9a5f96c71f89e746e6c27c95d
Author: Miles Dai <milesdai@google.com>
Date:   Thu Oct 20 17:27:01 2022 -0400

    [bazel] Allow opentitan_functest to accept custom bitstreams
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
