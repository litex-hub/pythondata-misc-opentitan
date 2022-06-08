import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12565"
version_tuple = (0, 0, 12565)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12565")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12423"
data_version_tuple = (0, 0, 12423)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12423")
except ImportError:
    pass
data_git_hash = "5f46a4281c9ed36c61f1505c663add9cd29e15c0"
data_git_describe = "v0.0-12423-g5f46a4281"
data_git_msg = """\
commit 5f46a4281c9ed36c61f1505c663add9cd29e15c0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jun 7 11:23:51 2022 -0700

    [fpv/alert_handler] Add sec_cm FPV testbench for alert_handler
    
    This PR adds a sec_cm FPV testbench for alert_handler.
    Because alert_handler does not trigger alert, it triggers escalation or
    local_alerts, so we need to declare a separate macro for it.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
