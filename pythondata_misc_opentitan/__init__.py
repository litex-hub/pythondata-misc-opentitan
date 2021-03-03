import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5213"
version_tuple = (0, 0, 5213)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5213")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5122"
data_version_tuple = (0, 0, 5122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5122")
except ImportError:
    pass
data_git_hash = "6cc5c164ba96d339f06cbcede0d17d2c96ce3c05"
data_git_describe = "v0.0-5122-g6cc5c164b"
data_git_msg = """\
commit 6cc5c164ba96d339f06cbcede0d17d2c96ce3c05
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 3 01:10:09 2021 -0800

    [dv] Add SV_FCOV_SVA back
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
