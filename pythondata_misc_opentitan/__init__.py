import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10264"
version_tuple = (0, 0, 10264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10140"
data_version_tuple = (0, 0, 10140)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10140")
except ImportError:
    pass
data_git_hash = "5d8c0e8e44c5c0e853d25deef6ac7863a98cece7"
data_git_describe = "v0.0-10140-g5d8c0e8e4"
data_git_msg = """\
commit 5d8c0e8e44c5c0e853d25deef6ac7863a98cece7
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Feb 11 09:42:24 2022 -0800

    [rtl/rstmgr] Remove superfluous assertion
    
    It caused trouble in some corner cases, and adds little value.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
