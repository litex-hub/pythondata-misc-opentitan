import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10062"
version_tuple = (0, 0, 10062)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10062")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9938"
data_version_tuple = (0, 0, 9938)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9938")
except ImportError:
    pass
data_git_hash = "752c40cf2eb7d0de3eb63026a4331565865ec4f7"
data_git_describe = "v0.0-9938-g752c40cf2"
data_git_msg = """\
commit 752c40cf2eb7d0de3eb63026a4331565865ec4f7
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Feb 3 16:11:51 2022 -0800

    [hmac] Clarify hmac module security capability
    
    - Fixes #10470
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
