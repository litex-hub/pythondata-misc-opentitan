import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8292"
version_tuple = (0, 0, 8292)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8292")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8180"
data_version_tuple = (0, 0, 8180)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8180")
except ImportError:
    pass
data_git_hash = "417e26e950fd095e81f9b330e4c4895f286176d8"
data_git_describe = "v0.0-8180-g417e26e95"
data_git_msg = """\
commit 417e26e950fd095e81f9b330e4c4895f286176d8
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Oct 4 17:52:55 2021 +0100

    [otbn, sw] Add software errors fatal mode testing to smoke test
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
