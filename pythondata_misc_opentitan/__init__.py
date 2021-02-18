import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5039"
version_tuple = (0, 0, 5039)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5039")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4948"
data_version_tuple = (0, 0, 4948)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4948")
except ImportError:
    pass
data_git_hash = "a0717f8d2278367c6ee4e526836f1a92a1a3f327"
data_git_describe = "v0.0-4948-ga0717f8d2"
data_git_msg = """\
commit a0717f8d2278367c6ee4e526836f1a92a1a3f327
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Feb 17 15:22:22 2021 -0800

    [dv/otp] Fix regression regwen failure
    
    The nightly regression failure is due to recent change in `reset`
    function. When reset is issued at posedge of `rst_n`, previous otp_scb
    code causes a race condition. This PR moves the ral prediction after
    `reset` function to avoid the race condition.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
