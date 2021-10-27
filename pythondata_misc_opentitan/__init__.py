import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8467"
version_tuple = (0, 0, 8467)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8467")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8355"
data_version_tuple = (0, 0, 8355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8355")
except ImportError:
    pass
data_git_hash = "51ffaeecec6fb0655bf51f9492b9754fe42707a5"
data_git_describe = "v0.0-8355-g51ffaeece"
data_git_msg = """\
commit 51ffaeecec6fb0655bf51f9492b9754fe42707a5
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Oct 26 01:52:28 2021 +0000

    [dif] Add alert autogen support to `make_new_dif.py`.
    
    This commit adds support for parsing alert information from an IP's
    HJSON to support autogenerating `dif_<ip>_alert_force()` DIFs in the
    future.
    
    This partially addresses the longer term goal in #8879 of
    auto-generating all alert test DIFs.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
