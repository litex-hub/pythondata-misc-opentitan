import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5561"
version_tuple = (0, 0, 5561)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5561")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5466"
data_version_tuple = (0, 0, 5466)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5466")
except ImportError:
    pass
data_git_hash = "7df143402a6908521013b717e14f2041d00978e4"
data_git_describe = "v0.0-5466-g7df143402"
data_git_msg = """\
commit 7df143402a6908521013b717e14f2041d00978e4
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 23 17:05:38 2021 -0700

    [util] Fix some minor indent issues
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
