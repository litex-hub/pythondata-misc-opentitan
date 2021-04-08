import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5789"
version_tuple = (0, 0, 5789)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5789")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5694"
data_version_tuple = (0, 0, 5694)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5694")
except ImportError:
    pass
data_git_hash = "3ecdcc05d4980fc776e9000a7da5e723e0a977f8"
data_git_describe = "v0.0-5694-g3ecdcc05d"
data_git_msg = """\
commit 3ecdcc05d4980fc776e9000a7da5e723e0a977f8
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Apr 7 11:06:12 2021 -0700

    [dv/otp_ctrl] Add coverpoint for scb checks
    
    In otp_ctrl scb, there are cases where we might waive checks (due to
    background checks, etc). I added some coverpoint to only collect
    coverage after these checks are done.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
