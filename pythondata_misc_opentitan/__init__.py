import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8457"
version_tuple = (0, 0, 8457)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8457")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8345"
data_version_tuple = (0, 0, 8345)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8345")
except ImportError:
    pass
data_git_hash = "05924908e0905aeff28bee5afdc880d89b48a784"
data_git_describe = "v0.0-8345-g05924908e"
data_git_msg = """\
commit 05924908e0905aeff28bee5afdc880d89b48a784
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Oct 15 16:16:17 2021 -0700

    [opentitantool] Add hook for bootstrapping code on emulators
    
    When running an OpenTitan emulator, we might want to use OpenTitan
    tool to "flash" a new firmware image.  We would not want to do so by
    SPI transactions like the real chips, except when testing the read
    only bootloader code.  Instead, we want to reach into special support
    from the emulation system itself, to be able to replace the entire
    content of the emulated flash storage.
    
    This CL adds a generic method to the Transport trait for specialized
    operations like that.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>

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
