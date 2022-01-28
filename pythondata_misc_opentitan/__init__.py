import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9866"
version_tuple = (0, 0, 9866)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9866")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9742"
data_version_tuple = (0, 0, 9742)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9742")
except ImportError:
    pass
data_git_hash = "3b45a9f00dff5c04e7b40cf4aa1fbe257c5724bd"
data_git_describe = "v0.0-9742-g3b45a9f00"
data_git_msg = """\
commit 3b45a9f00dff5c04e7b40cf4aa1fbe257c5724bd
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Jan 27 13:07:48 2022 -0800

    [bazel] pwrmgr_testutils 2 keymgr_functest deps
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
