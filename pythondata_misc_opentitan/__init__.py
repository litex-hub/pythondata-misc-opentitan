import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12869"
version_tuple = (0, 0, 12869)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12869")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12727"
data_version_tuple = (0, 0, 12727)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12727")
except ImportError:
    pass
data_git_hash = "ef7847ffe2c4afb52dbe20e5b0d53e41a058a9ff"
data_git_describe = "v0.0-12727-gef7847ffe2"
data_git_msg = """\
commit ef7847ffe2c4afb52dbe20e5b0d53e41a058a9ff
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Jun 27 19:49:03 2022 -0700

    [rv_dm dv] Fix compile warnings.
    
    Fix warnings related to ignored function returns.
    
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
