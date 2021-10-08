import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8184"
version_tuple = (0, 0, 8184)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8184")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8072"
data_version_tuple = (0, 0, 8072)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8072")
except ImportError:
    pass
data_git_hash = "9c9742a8f4fa229fe12892068b83fdd56a1ff5f9"
data_git_describe = "v0.0-8072-g9c9742a8f"
data_git_msg = """\
commit 9c9742a8f4fa229fe12892068b83fdd56a1ff5f9
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Oct 1 07:36:29 2021 -0700

    [dv/clkmgr] Fix frequency measurement test
    
    Compute the correct expectation.
    Improve randomization for thresholds.
    On each test round set at most one clock measurement to fail so the
    shared alert expectation functionality can handle the test.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
