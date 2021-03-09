import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5294"
version_tuple = (0, 0, 5294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5199"
data_version_tuple = (0, 0, 5199)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5199")
except ImportError:
    pass
data_git_hash = "6ddbb231d193128aa8738131b58ae367dbfe4ffd"
data_git_describe = "v0.0-5199-g6ddbb231d"
data_git_msg = """\
commit 6ddbb231d193128aa8738131b58ae367dbfe4ffd
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Mar 8 11:16:17 2021 -0800

    [otp_ctrl] Properly end cnsty/integ checks that found an error
    
    This changes the behavior of the buffered partition checker logic such
    that failing checks signal back to the LFSR timer that they have
    finished performing the check.
    
    That way, the LFSR timer can still continue running and triggering
    checks in other partitions, despite the faulty partition being in the
    terminal error state.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
