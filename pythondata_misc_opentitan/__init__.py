import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10526"
version_tuple = (0, 0, 10526)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10526")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10400"
data_version_tuple = (0, 0, 10400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10400")
except ImportError:
    pass
data_git_hash = "8484c811f5061be7da39093df19c887248c3927b"
data_git_describe = "v0.0-10400-g8484c811f"
data_git_msg = """\
commit 8484c811f5061be7da39093df19c887248c3927b
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 23 11:38:42 2022 -0800

    [fpv/pinmux] Update pinmux IOs
    
    This PR updates pinmux testbench IOs related to usb change.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
