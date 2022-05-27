import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12386"
version_tuple = (0, 0, 12386)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12386")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12246"
data_version_tuple = (0, 0, 12246)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12246")
except ImportError:
    pass
data_git_hash = "19a31959ad5e60ad1deaf1cfa5087cc183d24948"
data_git_describe = "v0.0-12246-g19a31959a"
data_git_msg = """\
commit 19a31959ad5e60ad1deaf1cfa5087cc183d24948
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon May 23 23:49:24 2022 +0000

    [chip,rstmgr,dv] regression fix rstmgr_alert_info test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
