import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10657"
version_tuple = (0, 0, 10657)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10657")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10531"
data_version_tuple = (0, 0, 10531)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10531")
except ImportError:
    pass
data_git_hash = "cea29efc4334108479e2a9aa2ef81126763ef16b"
data_git_describe = "v0.0-10531-gcea29efc4"
data_git_msg = """\
commit cea29efc4334108479e2a9aa2ef81126763ef16b
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 1 16:41:28 2022 -0800

    [prim] Minor lint fixes for unused clocks / resets
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
