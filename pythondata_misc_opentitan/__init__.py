import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13199"
version_tuple = (0, 0, 13199)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13199")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13057"
data_version_tuple = (0, 0, 13057)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13057")
except ImportError:
    pass
data_git_hash = "7003d824ec9598c2b2ef537c8afaf4ae43526aed"
data_git_describe = "v0.0-13057-g7003d824ec"
data_git_msg = """\
commit 7003d824ec9598c2b2ef537c8afaf4ae43526aed
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Jul 15 15:14:31 2022 -0700

    [sw,sensor_ctrl] Create testutils function for ast_init_done
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
