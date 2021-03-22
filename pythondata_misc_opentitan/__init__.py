import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5517"
version_tuple = (0, 0, 5517)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5517")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5422"
data_version_tuple = (0, 0, 5422)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5422")
except ImportError:
    pass
data_git_hash = "12ad5412b2697830481f17a49c3f221095c34199"
data_git_describe = "v0.0-5422-g12ad5412b"
data_git_msg = """\
commit 12ad5412b2697830481f17a49c3f221095c34199
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 22 10:19:51 2021 -0700

    [fpv/otp_ctrl] fix assertion issue
    
    This PR fixes an assertion error in DV regression. In property, it
    already includes a one cycle delay. Using `=>` gives an extra cycle that
    causes the failure.
    
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
