import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9443"
version_tuple = (0, 0, 9443)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9443")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9325"
data_version_tuple = (0, 0, 9325)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9325")
except ImportError:
    pass
data_git_hash = "33e0d1e65b289c01f8c8edcfc0fa6bcfad114924"
data_git_describe = "v0.0-9325-g33e0d1e65"
data_git_msg = """\
commit 33e0d1e65b289c01f8c8edcfc0fa6bcfad114924
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Jan 7 13:56:41 2022 -0800

    [dif/alert_handler] Add alert configuration DIF.
    
    Previously, the only way to configure an alert within the alert handler
    was to build a rather large struct that would configure all alerts
    within a class. (Re)Configuring a single alert had the side of effect of
    reconfiguring the class too.
    
    This commit adds a DIF to configure a single alert, i.e., enable it, set
    its class, and lock it. This partially addresses #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
