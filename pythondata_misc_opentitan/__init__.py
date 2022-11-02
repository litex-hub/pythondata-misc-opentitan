import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15139"
version_tuple = (0, 0, 15139)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15139")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14997"
data_version_tuple = (0, 0, 14997)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14997")
except ImportError:
    pass
data_git_hash = "3a7c11f8b3fbabd45ce31e9fd4ed1a2fb0b6eb86"
data_git_describe = "v0.0-14997-g3a7c11f8b3"
data_git_msg = """\
commit 3a7c11f8b3fbabd45ce31e9fd4ed1a2fb0b6eb86
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 1 23:19:42 2022 -0700

    [top/dv] Add missing queue constraint
    
    - fixes #15895
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
