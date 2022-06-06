import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12517"
version_tuple = (0, 0, 12517)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12517")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12375"
data_version_tuple = (0, 0, 12375)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12375")
except ImportError:
    pass
data_git_hash = "ce4d65282bb2122c0ef25768e3b9fea55a9837e5"
data_git_describe = "v0.0-12375-gce4d65282"
data_git_msg = """\
commit ce4d65282bb2122c0ef25768e3b9fea55a9837e5
Author: Miles Dai <milesdai@google.com>
Date:   Fri Jun 3 17:36:52 2022 -0400

    [ci] Reduce the number of CW310 tests being run in CI
    
    The communication with the CW310 board in CI fails intermittently. This
    is happening more frequency after more tests were added during the Bazel
    transition. This commit is a temporary measure to reduce the frequency
    of these failures by running fewer tests (the same set that was
    previously being run by systemtest).
    
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
