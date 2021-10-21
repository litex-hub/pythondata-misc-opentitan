import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8395"
version_tuple = (0, 0, 8395)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8395")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8283"
data_version_tuple = (0, 0, 8283)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8283")
except ImportError:
    pass
data_git_hash = "dab021e1b7932ae2b9f7ea0f1930807c24eb2cf2"
data_git_describe = "v0.0-8283-gdab021e1b"
data_git_msg = """\
commit dab021e1b7932ae2b9f7ea0f1930807c24eb2cf2
Author: Weicai Yang <weicai@google.com>
Date:   Wed Oct 20 17:12:45 2021 -0700

    [dv] Update kmac_app_monitor to remove glitch of ok_to_end
    
    The update doesn't change any functionality but this will remove 0 delay
    glich of ok_to_end
    Signed-off-by: Weicai Yang <weicai@google.com>

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
