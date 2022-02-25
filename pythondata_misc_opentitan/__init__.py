import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10538"
version_tuple = (0, 0, 10538)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10538")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10412"
data_version_tuple = (0, 0, 10412)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10412")
except ImportError:
    pass
data_git_hash = "876015a60772359128bfb687b6e71abc99f12573"
data_git_describe = "v0.0-10412-g876015a60"
data_git_msg = """\
commit 876015a60772359128bfb687b6e71abc99f12573
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Feb 24 12:54:19 2022 -0800

    [sw/test_rom] Re-enable SW-gateable clocks after reset
    
    As #11081 points out, if a SW-gateable clock is gated, and the chip is
    only partially reset (i.e., reset is NOT a POR), peripherals that the
    test ROM uses (i.e., UART for logging and HMAC for bootstrap) could be
    rendered in-operable.
    
    This commit partially addresses #11081 (w.r.t. to the test ROM) by
    resetting all SW-gateable clocks to their default POR values.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
