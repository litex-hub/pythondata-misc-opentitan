import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8908"
version_tuple = (0, 0, 8908)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8908")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8796"
data_version_tuple = (0, 0, 8796)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8796")
except ImportError:
    pass
data_git_hash = "86e2378caaf4d8f0363357d405d1c946f0f92e49"
data_git_describe = "v0.0-8796-g86e2378ca"
data_git_msg = """\
commit 86e2378caaf4d8f0363357d405d1c946f0f92e49
Author: Weicai Yang <weicai@google.com>
Date:   Wed Nov 24 17:11:45 2021 -0800

    [sram/dv] Fix mem data check
    
    1. Fixed data check in mem model didn't work
    2. Move updating exp mem write value after data phase is done, as the
    2nd address may finish before the data phase of the 1st item when it
    supports 2+ outstanding items
    3. Avoid frontdoor checking read value if the location hasn't been
    written (check against backdoor will be still applied)
    4. Add knob for seq to initialize the mem and do it during sram_ctrl_init
    
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
