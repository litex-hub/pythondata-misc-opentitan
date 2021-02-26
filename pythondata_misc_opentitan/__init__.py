import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5161"
version_tuple = (0, 0, 5161)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5161")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5070"
data_version_tuple = (0, 0, 5070)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5070")
except ImportError:
    pass
data_git_hash = "f11e29f066aa3601b1152aa5c35db23986619d63"
data_git_describe = "v0.0-5070-gf11e29f06"
data_git_msg = """\
commit f11e29f066aa3601b1152aa5c35db23986619d63
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Feb 11 09:04:35 2021 +0000

    [usbdev] Add ASSERT_KNOWN on outputs
    
    This is required for D1 signoff.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
