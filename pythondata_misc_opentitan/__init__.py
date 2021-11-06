import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8617"
version_tuple = (0, 0, 8617)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8617")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8505"
data_version_tuple = (0, 0, 8505)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8505")
except ImportError:
    pass
data_git_hash = "a6260f0f11647bc7895183e58da9c7d52705df20"
data_git_describe = "v0.0-8505-ga6260f0f1"
data_git_msg = """\
commit a6260f0f11647bc7895183e58da9c7d52705df20
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Nov 4 15:59:35 2021 -0700

    [doc] Add D2S and V2S milestones to documentation
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
