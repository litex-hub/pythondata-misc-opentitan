import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5815"
version_tuple = (0, 0, 5815)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5815")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5720"
data_version_tuple = (0, 0, 5720)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5720")
except ImportError:
    pass
data_git_hash = "28047086d5d14a00c1feac17c5616fde871d0a31"
data_git_describe = "v0.0-5720-g28047086d"
data_git_msg = """\
commit 28047086d5d14a00c1feac17c5616fde871d0a31
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Apr 8 09:18:13 2021 -0700

    [ci] Remove dif_entropy_smoketest completely from CI
    
    - The test will be reintroduced when #5941 is ready
      and can produce reliable results.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
