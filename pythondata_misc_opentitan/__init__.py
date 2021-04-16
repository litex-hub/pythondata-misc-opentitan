import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5937"
version_tuple = (0, 0, 5937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5842"
data_version_tuple = (0, 0, 5842)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5842")
except ImportError:
    pass
data_git_hash = "45b996fbabb7c2a51e96825e9a78a9fdb4694e76"
data_git_describe = "v0.0-5842-g45b996fba"
data_git_msg = """\
commit 45b996fbabb7c2a51e96825e9a78a9fdb4694e76
Author: Felix Miller <felix.miller@gi-de.com>
Date:   Thu Apr 15 23:11:02 2021 +0200

    [otbn] add test for RSA verify with exp=3
    
    Adds a test for RSA signature verification including
    an appropriate test key.
    
    Signed-off-by: Felix Miller <felix.miller@gi-de.com>

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
