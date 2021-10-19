import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8343"
version_tuple = (0, 0, 8343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8231"
data_version_tuple = (0, 0, 8231)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8231")
except ImportError:
    pass
data_git_hash = "e6e9fb2de76e92aeed4673e13d2c87ab7d5a6abd"
data_git_describe = "v0.0-8231-ge6e9fb2de"
data_git_msg = """\
commit e6e9fb2de76e92aeed4673e13d2c87ab7d5a6abd
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 13 00:51:52 2021 +0000

    [rv_timer] Make interrupt names more descriptive.
    
    The RV timer can raise and IRQ for each timer within each hart. In the
    current configuration of the RV timer, we implement one timer and one
    hart, so the name of the (single) resulting IRQ signal is:
    `timer_expired_0_0`, where the `0_0` portion signifies hart-0, timer-0.
    
    This commit fixes #8681 by changing the IRQ name above to:
    `timer_expired_hart0_timer0`.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
