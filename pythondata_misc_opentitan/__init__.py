import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13343"
version_tuple = (0, 0, 13343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13201"
data_version_tuple = (0, 0, 13201)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13201")
except ImportError:
    pass
data_git_hash = "cf59384407ef7733f96a1717cb7bb0c79e77205a"
data_git_describe = "v0.0-13201-gcf59384407"
data_git_msg = """\
commit cf59384407ef7733f96a1717cb7bb0c79e77205a
Author: Michael Schaffner <msf@google.com>
Date:   Tue Jul 26 16:07:07 2022 -0700

    [otp_ctrl/doc] Document what can be re-parameterized after D3/V3
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
