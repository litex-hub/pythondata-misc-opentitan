import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14247"
version_tuple = (0, 0, 14247)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14247")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14105"
data_version_tuple = (0, 0, 14105)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14105")
except ImportError:
    pass
data_git_hash = "ad0efd0714daf9b33ca1e1750f71e6978d12f519"
data_git_describe = "v0.0-14105-gad0efd0714"
data_git_msg = """\
commit ad0efd0714daf9b33ca1e1750f71e6978d12f519
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 23:09:05 2022 -0700

    [python] pin package version numbers
    
    Having unpinned package versions reduces reproducibility and was causing
    unncessary Bazel airgapped image updates.
    
    This fixes #14939.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
