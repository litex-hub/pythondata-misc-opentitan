import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14316"
version_tuple = (0, 0, 14316)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14316")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14174"
data_version_tuple = (0, 0, 14174)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14174")
except ImportError:
    pass
data_git_hash = "1f3a24718d33c975f12f902994c39d2497b8623e"
data_git_describe = "v0.0-14174-g1f3a24718d"
data_git_msg = """\
commit 1f3a24718d33c975f12f902994c39d2497b8623e
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Sep 15 18:08:20 2022 -0700

    [top/dv] update testplan for manufacturing
    
    - enhance existing tests
    - add new test points.
    
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
