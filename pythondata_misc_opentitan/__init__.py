import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8854"
version_tuple = (0, 0, 8854)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8854")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8742"
data_version_tuple = (0, 0, 8742)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8742")
except ImportError:
    pass
data_git_hash = "a76b48d46098bf07904fbc1f8cf47d2cd4160cdc"
data_git_describe = "v0.0-8742-ga76b48d46"
data_git_msg = """\
commit a76b48d46098bf07904fbc1f8cf47d2cd4160cdc
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Nov 23 14:41:44 2021 +0000

    [sw/silicon_creator] Minor cleanups to shutdown code.
    
    Follow up addressing comments on PR #8289.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
