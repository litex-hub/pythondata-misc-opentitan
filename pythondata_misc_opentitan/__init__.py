import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12453"
version_tuple = (0, 0, 12453)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12453")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12311"
data_version_tuple = (0, 0, 12311)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12311")
except ImportError:
    pass
data_git_hash = "e659e11763cd19d3ff983e7203e451a38724921e"
data_git_describe = "v0.0-12311-ge659e1176"
data_git_msg = """\
commit e659e11763cd19d3ff983e7203e451a38724921e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue May 31 17:04:25 2022 -0400

    [sw/silicon_creator] Use macro instead of constant for rv_dm rom size
    
    Fixes #11092
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
