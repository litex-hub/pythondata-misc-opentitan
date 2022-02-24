import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10525"
version_tuple = (0, 0, 10525)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10525")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10399"
data_version_tuple = (0, 0, 10399)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10399")
except ImportError:
    pass
data_git_hash = "0978ab3285b5a66ebe6166295f16b7668b99929c"
data_git_describe = "v0.0-10399-g0978ab328"
data_git_msg = """\
commit 0978ab3285b5a66ebe6166295f16b7668b99929c
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Feb 24 10:05:05 2022 -0800

    [util/dvsim] Fix confusing error message
    
    The error emitted when there are circular includes is confusing, making
    diagnosis more difficult.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
