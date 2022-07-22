import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13246"
version_tuple = (0, 0, 13246)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13246")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13104"
data_version_tuple = (0, 0, 13104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13104")
except ImportError:
    pass
data_git_hash = "7bcfa8c4fa546dfb7fefd72902bb0c06143ba4fb"
data_git_describe = "v0.0-13104-g7bcfa8c4fa"
data_git_msg = """\
commit 7bcfa8c4fa546dfb7fefd72902bb0c06143ba4fb
Author: Drew Macrae <drewmacrae@google.com>
Date:   Fri Jul 15 15:34:38 2022 -0400

    [bazel] specify longer timeouts so verilated tests can run in batches
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
