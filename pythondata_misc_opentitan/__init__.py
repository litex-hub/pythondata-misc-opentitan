import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8232"
version_tuple = (0, 0, 8232)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8232")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8120"
data_version_tuple = (0, 0, 8120)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8120")
except ImportError:
    pass
data_git_hash = "72535bce8c7ead635c8e90ab6911ae7681a4f6ea"
data_git_describe = "v0.0-8120-g72535bce8"
data_git_msg = """\
commit 72535bce8c7ead635c8e90ab6911ae7681a4f6ea
Author: Michael Schaffner <msf@google.com>
Date:   Mon Oct 11 12:10:02 2021 -0700

    [alert_handler/top] Lint fixes and lc_tx_t to mubi4_t conversions
    
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
