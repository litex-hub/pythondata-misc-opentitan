import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5632"
version_tuple = (0, 0, 5632)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5632")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5537"
data_version_tuple = (0, 0, 5537)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5537")
except ImportError:
    pass
data_git_hash = "d15513ae70572efa698d4c5113302b9f81af8be7"
data_git_describe = "v0.0-5537-gd15513ae7"
data_git_msg = """\
commit d15513ae70572efa698d4c5113302b9f81af8be7
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 15 11:54:37 2021 +0000

    [rv_dm] Sign off debug module into D1
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
