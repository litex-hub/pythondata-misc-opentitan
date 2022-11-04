import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15238"
version_tuple = (0, 0, 15238)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15238")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15096"
data_version_tuple = (0, 0, 15096)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15096")
except ImportError:
    pass
data_git_hash = "024279c574b6be805ed33286801e62a2ed16fa13"
data_git_describe = "v0.0-15096-g024279c574"
data_git_msg = """\
commit 024279c574b6be805ed33286801e62a2ed16fa13
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Nov 2 15:32:12 2022 -0400

    [bazel] Use GDB from Bazel instead of /tools
    
    Fixes #15935
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
