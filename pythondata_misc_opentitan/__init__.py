import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10342"
version_tuple = (0, 0, 10342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10216"
data_version_tuple = (0, 0, 10216)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10216")
except ImportError:
    pass
data_git_hash = "f8cde5d2c5be085429c9f5bcb71e5f9f546aa08e"
data_git_describe = "v0.0-10216-gf8cde5d2c"
data_git_msg = """\
commit f8cde5d2c5be085429c9f5bcb71e5f9f546aa08e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Feb 3 21:03:37 2022 +0000

    [otbn, test] Add secure wipe to smoke test
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
