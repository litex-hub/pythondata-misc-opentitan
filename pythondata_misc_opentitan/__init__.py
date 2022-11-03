import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15172"
version_tuple = (0, 0, 15172)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15172")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15030"
data_version_tuple = (0, 0, 15030)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15030")
except ImportError:
    pass
data_git_hash = "99a7afa825ffb01928517954295f00cd9e354a34"
data_git_describe = "v0.0-15030-g99a7afa825"
data_git_msg = """\
commit 99a7afa825ffb01928517954295f00cd9e354a34
Author: Dan McArdle <dmcardle@google.com>
Date:   Tue Nov 1 11:13:49 2022 -0400

    [doc] Document Bazel-managed OpenOCD dependency
    
    Rather than editing incoming links to install_openocd.md, this commit
    just edits install_openocd.md, which is kind of a cop out. Eventually,
    we should rename the file to indicate that installation isn't a step you
    need to worry about anymore.
    
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
