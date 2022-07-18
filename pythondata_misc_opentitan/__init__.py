import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13144"
version_tuple = (0, 0, 13144)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13144")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13002"
data_version_tuple = (0, 0, 13002)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13002")
except ImportError:
    pass
data_git_hash = "0e1501b858e28f5aff9f4ec570e6a30d6f166bce"
data_git_describe = "v0.0-13002-g0e1501b858"
data_git_msg = """\
commit 0e1501b858e28f5aff9f4ec570e6a30d6f166bce
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Jul 15 16:28:02 2022 -0700

    [dvsim] Add support for SW (bazel) build opts
    
    This commit adds native support to set additional bazel command args via
    `sw_build_opts`, which can be set in test specifications, `run_modes`,
    `build_modes` and regressions in the Hjson spec.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
