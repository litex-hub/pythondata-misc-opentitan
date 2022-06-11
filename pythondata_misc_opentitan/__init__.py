import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12650"
version_tuple = (0, 0, 12650)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12650")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12508"
data_version_tuple = (0, 0, 12508)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12508")
except ImportError:
    pass
data_git_hash = "1d9f1032c7e30cb28c4c5b7c0a4ad0342a5200d7"
data_git_describe = "v0.0-12508-g1d9f1032c"
data_git_msg = """\
commit 1d9f1032c7e30cb28c4c5b7c0a4ad0342a5200d7
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Jun 10 14:06:19 2022 -0400

    [bazel] Sign ROM_EXT images
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
