import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5078"
version_tuple = (0, 0, 5078)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5078")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4987"
data_version_tuple = (0, 0, 4987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4987")
except ImportError:
    pass
data_git_hash = "dc81618900cf069065c2d62b9863f52ce3a30cc1"
data_git_describe = "v0.0-4987-gdc8161890"
data_git_msg = """\
commit dc81618900cf069065c2d62b9863f52ce3a30cc1
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Feb 19 15:39:27 2021 -0800

    [dv/hmac] Fix hmac vector parsing
    
    This PR fixes the regression failure on hmac NIST vector parsing. The
    hmac vector does not have `KeyLen` keyword, but still has `Key`. The
    current parsing logic will set the key to 0 in this case.
    
    Also hmac NIST vector does not need to reserve key input, but kmac
    vectors needs to. So this PR adds a flag for user to decide if they want
    the key to be reserved.
    
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
