import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13179"
version_tuple = (0, 0, 13179)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13179")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13037"
data_version_tuple = (0, 0, 13037)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13037")
except ImportError:
    pass
data_git_hash = "e2fed9dfa9eca83d7544bc13741c1cd6904eb4e3"
data_git_describe = "v0.0-13037-ge2fed9dfa9"
data_git_msg = """\
commit e2fed9dfa9eca83d7544bc13741c1cd6904eb4e3
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Jul 18 19:35:56 2022 -0700

    [dif/entropy_src] add DIFs to get/clear/force alerts and errors
    
    This adds DIFs (and corresponding unit tests) to get/clear/force
    recoverable alerts and (nonrecoverable) errors.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
