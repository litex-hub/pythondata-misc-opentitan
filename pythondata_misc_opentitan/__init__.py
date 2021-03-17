import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5421"
version_tuple = (0, 0, 5421)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5421")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5326"
data_version_tuple = (0, 0, 5326)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5326")
except ImportError:
    pass
data_git_hash = "b5c684b86340ac4502fd34d8b8554575669b174d"
data_git_describe = "v0.0-5326-gb5c684b86"
data_git_msg = """\
commit b5c684b86340ac4502fd34d8b8554575669b174d
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Mar 11 14:44:55 2021 -0800

    [dv/sram] lc_escalation test
    
    this PR adds the lifecycle escalation test as described by the testplan.
    
    in this test we randomly inject an escalation request, then expect that
    the SRAM ignore all following memory requests until a system reset is
    issued.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
