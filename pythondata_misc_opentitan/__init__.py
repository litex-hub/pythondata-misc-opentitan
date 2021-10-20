import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8360"
version_tuple = (0, 0, 8360)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8360")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8248"
data_version_tuple = (0, 0, 8248)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8248")
except ImportError:
    pass
data_git_hash = "f0f3426ba5a49d728bb623e428130941028c88cb"
data_git_describe = "v0.0-8248-gf0f3426ba"
data_git_msg = """\
commit f0f3426ba5a49d728bb623e428130941028c88cb
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 20 00:22:51 2021 +0000

    [dif/rv_timer] Prepare for `dif_rv_timer_init()` autogen.
    
    The RV Timer `dif_rv_timer_init()` function contained reset logic that was
    inconsistent with other IP's DIF APIs. In order to auto-generate the
    `dif_<ip>_init()` function across all IPs (as stated in #8409), this reset
    logic must be separated into a separate DIF/DIF invocation.
    
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
