import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9548"
version_tuple = (0, 0, 9548)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9548")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9426"
data_version_tuple = (0, 0, 9426)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9426")
except ImportError:
    pass
data_git_hash = "1e2e6b3469d36dd13cdd2d0a518c98c1c5a4de79"
data_git_describe = "v0.0-9426-g1e2e6b346"
data_git_msg = """\
commit 1e2e6b3469d36dd13cdd2d0a518c98c1c5a4de79
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jan 13 12:37:14 2022 -0800

    [dv/clkmgr] Add stress test
    
    Fix for forks missing isolation forks.
    Fix other minor issues caught by this test.
    Move CSR value tracking to clkmgr interface.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
