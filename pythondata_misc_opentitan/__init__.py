import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5709"
version_tuple = (0, 0, 5709)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5709")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5614"
data_version_tuple = (0, 0, 5614)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5614")
except ImportError:
    pass
data_git_hash = "414f7a74d775b88c842e508c4e036ea539cd3355"
data_git_describe = "v0.0-5614-g414f7a74d"
data_git_msg = """\
commit 414f7a74d775b88c842e508c4e036ea539cd3355
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Apr 2 13:58:57 2021 -0700

    [dv/otp_ctrl] otp init failure test
    
    This PR adds a otp_init failure test. This test will cause otp init
    failure by creating init check errors. Scb is disabled in this test.
    
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
