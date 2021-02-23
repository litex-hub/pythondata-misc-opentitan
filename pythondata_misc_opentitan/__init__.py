import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5123"
version_tuple = (0, 0, 5123)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5123")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5032"
data_version_tuple = (0, 0, 5032)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5032")
except ImportError:
    pass
data_git_hash = "4bc32ae8205ac08af16b7f89f2d02e2e8185cd4d"
data_git_describe = "v0.0-5032-g4bc32ae82"
data_git_msg = """\
commit 4bc32ae8205ac08af16b7f89f2d02e2e8185cd4d
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Feb 23 10:45:15 2021 -0800

    [otp_ctrl] Make error interrupts non-sticky
    
    Fix #5350
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
