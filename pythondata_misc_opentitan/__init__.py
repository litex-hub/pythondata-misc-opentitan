import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5313"
version_tuple = (0, 0, 5313)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5313")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5218"
data_version_tuple = (0, 0, 5218)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5218")
except ImportError:
    pass
data_git_hash = "93daf962b2b90b42879ac0f6ea8b0a17a9a0cb50"
data_git_describe = "v0.0-5218-g93daf962b"
data_git_msg = """\
commit 93daf962b2b90b42879ac0f6ea8b0a17a9a0cb50
Author: Cindy Chen <chencindy@google.com>
Date:   Sun Mar 7 15:16:46 2021 -0800

    [dv/otp_ctrl] check timeout failure
    
    This PR supports one kind of check failure - the timeout failure.
    The timoeut failure is triggered by setting the timeout value to a small
    value. The timeout failure will send out a fatal alert and status
    timeout error bit will be set.
    
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
