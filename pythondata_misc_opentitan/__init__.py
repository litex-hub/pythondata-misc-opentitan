import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5264"
version_tuple = (0, 0, 5264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5169"
data_version_tuple = (0, 0, 5169)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5169")
except ImportError:
    pass
data_git_hash = "f77e60c36955b16daa20fccfc91589a1f21ecde9"
data_git_describe = "v0.0-5169-gf77e60c36"
data_git_msg = """\
commit f77e60c36955b16daa20fccfc91589a1f21ecde9
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Mar 5 10:44:42 2021 -0800

    [rtl/otp_ctrl] Report ECC correctable error in consistency check
    
    This PR adds some logic to report ECC correctable error in consistency
    check. Previous logic will silently fix the ecc correctable error
    without reporting it to status and error bit.
    
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
