import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15075"
version_tuple = (0, 0, 15075)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15075")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14933"
data_version_tuple = (0, 0, 14933)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14933")
except ImportError:
    pass
data_git_hash = "076b1d179a4d9fb6e1cc1bca0f7a9f37e30d3347"
data_git_describe = "v0.0-14933-g076b1d179a"
data_git_msg = """\
commit 076b1d179a4d9fb6e1cc1bca0f7a9f37e30d3347
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 27 13:48:05 2022 -0700

    [spi_device] Sign off V2S
    
    All review items in #15539 have been addressed.
    Only 1 sec_cm - bus integrity, so directly sign off the V2S
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
