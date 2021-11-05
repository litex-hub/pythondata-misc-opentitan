import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8609"
version_tuple = (0, 0, 8609)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8609")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8497"
data_version_tuple = (0, 0, 8497)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8497")
except ImportError:
    pass
data_git_hash = "2c275eba7be688e9a3d9716b8b91d56e35ce1298"
data_git_describe = "v0.0-8497-g2c275eba7"
data_git_msg = """\
commit 2c275eba7be688e9a3d9716b8b91d56e35ce1298
Author: Michael Schaffner <msf@google.com>
Date:   Thu Nov 4 11:35:54 2021 -0700

    [syn/aes/otbn] Minor fixes to fix block level synthesis
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
