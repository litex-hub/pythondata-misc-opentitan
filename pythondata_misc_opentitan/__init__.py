import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10277"
version_tuple = (0, 0, 10277)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10277")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10151"
data_version_tuple = (0, 0, 10151)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10151")
except ImportError:
    pass
data_git_hash = "65ab4c15c77e98f228642e05cb6c6b509cb9bb5d"
data_git_describe = "v0.0-10151-g65ab4c15c"
data_git_msg = """\
commit 65ab4c15c77e98f228642e05cb6c6b509cb9bb5d
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Thu Jan 20 14:48:22 2022 +0000

    [mask_rom] Configure watchdog using OTP value
    
    Configure the watchdog timer using an OTP value when in the DEV,
    PROD and PROD_END lifecycle states. Otherwise disable it.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
