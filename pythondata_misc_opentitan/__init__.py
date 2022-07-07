import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12952"
version_tuple = (0, 0, 12952)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12952")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12810"
data_version_tuple = (0, 0, 12810)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12810")
except ImportError:
    pass
data_git_hash = "e759d414f3f93af1bc9942d60cc40ed595ace56e"
data_git_describe = "v0.0-12810-ge759d414f3"
data_git_msg = """\
commit e759d414f3f93af1bc9942d60cc40ed595ace56e
Author: Miles Dai <milesdai@google.com>
Date:   Thu Jun 30 13:48:12 2022 -0400

    [ci] Move continueOnError flag for Bazel fetch step
    
    This is an attempt to try and trigger a warning on Github instead of a failure.
    
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
