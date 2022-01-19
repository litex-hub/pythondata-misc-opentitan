import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9628"
version_tuple = (0, 0, 9628)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9628")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9506"
data_version_tuple = (0, 0, 9506)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9506")
except ImportError:
    pass
data_git_hash = "cc147faf54de28d8958cc3d23f1925062e0a9c53"
data_git_describe = "v0.0-9506-gcc147faf5"
data_git_msg = """\
commit cc147faf54de28d8958cc3d23f1925062e0a9c53
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jan 13 17:41:23 2022 -0800

    [dif/alert_handler] Add ping timer enable DIF.
    
    The previous commit adds a DIF to configure the ping timer. This DIF can
    also be used to enable and lock the ping timer too. However, if a user
    wants to only configure the ping timer, and enable it later, they would
    have to write to the time out register again too.
    
    This commit adds another DIF that just enables (and locks, if requested)
    the ping timer. This enables more fine grain configuration of the alert
    handler's ping timer.
    
    This addresses a task in #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
