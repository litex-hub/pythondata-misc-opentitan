import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13276"
version_tuple = (0, 0, 13276)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13276")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13134"
data_version_tuple = (0, 0, 13134)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13134")
except ImportError:
    pass
data_git_hash = "19a8e33764bac07e0653d1d8720be7ffd0a02dd8"
data_git_describe = "v0.0-13134-g19a8e33764"
data_git_msg = """\
commit 19a8e33764bac07e0653d1d8720be7ffd0a02dd8
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Jul 26 10:12:44 2022 -0700

    [dvsim] remove unecessary `sw_build_dir` parameter
    
    In the previous commit, SW image string formats were update to be
    referred to by the Bazel label. Part of this update also involved
    copying Bazel-built SW images into the simulation `run_dir`, which
    removed the need to track the `sw_build_dir`. Therefore, this commit
    cleans up dvsim.py to remove this parameter.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
