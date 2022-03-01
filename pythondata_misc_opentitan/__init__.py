import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10622"
version_tuple = (0, 0, 10622)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10622")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10496"
data_version_tuple = (0, 0, 10496)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10496")
except ImportError:
    pass
data_git_hash = "739099ccbb05f6b2aaeee15b8acdb5cc3b798d2a"
data_git_describe = "v0.0-10496-g739099ccb"
data_git_msg = """\
commit 739099ccbb05f6b2aaeee15b8acdb5cc3b798d2a
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Feb 28 15:00:38 2022 -0800

    [flash_ctrl] Correct erase suspend interface behavior
    
    - fixes #11143
    
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
