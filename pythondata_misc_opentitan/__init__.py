import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13021"
version_tuple = (0, 0, 13021)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13021")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12879"
data_version_tuple = (0, 0, 12879)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12879")
except ImportError:
    pass
data_git_hash = "7ee59a3b34a68b4fb59ca521c2b5c1b82842f570"
data_git_describe = "v0.0-12879-g7ee59a3b34"
data_git_msg = """\
commit 7ee59a3b34a68b4fb59ca521c2b5c1b82842f570
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jun 30 16:35:26 2022 -0700

    [dv/top] Add alert_handler_escalation test
    
    - this test goes through the full escalation path from a single
      alert.
    - the secret checking portion during escalation can be further
      enhanced.
    
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
