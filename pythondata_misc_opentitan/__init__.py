import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10171"
version_tuple = (0, 0, 10171)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10171")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10047"
data_version_tuple = (0, 0, 10047)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10047")
except ImportError:
    pass
data_git_hash = "d23fb67c3859c4e900c204331d09a1119cd9b0de"
data_git_describe = "v0.0-10047-gd23fb67c3"
data_git_msg = """\
commit d23fb67c3859c4e900c204331d09a1119cd9b0de
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 8 15:38:37 2022 -0800

    [pwrmgr] Update default value
    
    - fixes #4694
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
