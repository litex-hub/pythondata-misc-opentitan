import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9791"
version_tuple = (0, 0, 9791)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9791")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9669"
data_version_tuple = (0, 0, 9669)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9669")
except ImportError:
    pass
data_git_hash = "cc0f9024cb2aaad7a46b7ff3f6b4e7a24b5e79b6"
data_git_describe = "v0.0-9669-gcc0f9024c"
data_git_msg = """\
commit cc0f9024cb2aaad7a46b7ff3f6b4e7a24b5e79b6
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jan 24 20:59:43 2022 -0800

    [otp_ctrl] Amend documentation for VENDOR_TEST partition
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
