import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15342"
version_tuple = (0, 0, 15342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15200"
data_version_tuple = (0, 0, 15200)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15200")
except ImportError:
    pass
data_git_hash = "c2caa251d82030b456669e9c04afd5586a127743"
data_git_describe = "v0.0-15200-gc2caa251d8"
data_git_msg = """\
commit c2caa251d82030b456669e9c04afd5586a127743
Author: Johnathan Van Why <jrvanwhy@google.com>
Date:   Wed Nov 2 12:59:26 2022 -0700

    Add rom_e2e_watchdog_reconfig tests.
    
    These tests verify the ROM correctly configures the watchdog timer. Tests are run with OTP configurations that disable and enable the watchdog for each life cycle state.
    
    Signed-off-by: Johnathan Van Why <jrvanwhy@google.com>

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
