import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14905"
version_tuple = (0, 0, 14905)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14905")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14763"
data_version_tuple = (0, 0, 14763)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14763")
except ImportError:
    pass
data_git_hash = "4ad3f30781a95dff7e161bc0ed865e3972b2446b"
data_git_describe = "v0.0-14763-g4ad3f30781"
data_git_msg = """\
commit 4ad3f30781a95dff7e161bc0ed865e3972b2446b
Author: Miles Dai <milesdai@google.com>
Date:   Wed Oct 19 23:13:47 2022 -0400

    [bazel] Add support for pagination when querying the bitstream cache
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
