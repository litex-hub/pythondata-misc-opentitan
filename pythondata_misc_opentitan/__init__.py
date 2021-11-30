import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8884"
version_tuple = (0, 0, 8884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8772"
data_version_tuple = (0, 0, 8772)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8772")
except ImportError:
    pass
data_git_hash = "01234f94e2cf1ef42f3e2e79e940b4ae5b199ecc"
data_git_describe = "v0.0-8772-g01234f94e"
data_git_msg = """\
commit 01234f94e2cf1ef42f3e2e79e940b4ae5b199ecc
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Nov 19 13:25:57 2021 -0800

    [lc_ctrl] Make the life cycle state CSR multibit
    
    This repeats the 5bit life cycle enum and the 2bit
    provisioning state enum in order to make these CSRs
    multibit (they will span almost the entire 32bit).
    
    This change has been requested as part of ROM code hardening.
    
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
