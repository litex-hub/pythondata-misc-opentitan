import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5150"
version_tuple = (0, 0, 5150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5059"
data_version_tuple = (0, 0, 5059)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5059")
except ImportError:
    pass
data_git_hash = "3ec2dae4cc0c4a4c4604c7ff84f83e2f7c98b8a5"
data_git_describe = "v0.0-5059-g3ec2dae4c"
data_git_msg = """\
commit 3ec2dae4cc0c4a4c4604c7ff84f83e2f7c98b8a5
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Feb 22 11:36:07 2021 -0800

    [dv/otp_ctrl] ECC uncorrectable error
    
    This PR adds suppor to trigger ECC uncorrectable error. Currently only
    allow 2 errors per word. Once the ECC is integrity in mem_bkdr_if, we
    can fully randomize the error.
    
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
