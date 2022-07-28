import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13300"
version_tuple = (0, 0, 13300)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13300")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13158"
data_version_tuple = (0, 0, 13158)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13158")
except ImportError:
    pass
data_git_hash = "b1f6dddfdf29165e8c5f62c1a630e8b88025db6d"
data_git_describe = "v0.0-13158-gb1f6dddfdf"
data_git_msg = """\
commit b1f6dddfdf29165e8c5f62c1a630e8b88025db6d
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jul 27 16:47:38 2022 -0700

    [dv/top] Correct test name in sim config
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
