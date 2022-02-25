import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10556"
version_tuple = (0, 0, 10556)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10556")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10430"
data_version_tuple = (0, 0, 10430)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10430")
except ImportError:
    pass
data_git_hash = "7e5ab7acc603347b7926e3d5f1bdba2764bd68d9"
data_git_describe = "v0.0-10430-g7e5ab7acc"
data_git_msg = """\
commit 7e5ab7acc603347b7926e3d5f1bdba2764bd68d9
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Feb 23 17:24:51 2022 -0800

    [rstmgr] documentation updates based on d2s feedback
    
    - there is a separate readability feedback that will be done in a different PR.
    
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
