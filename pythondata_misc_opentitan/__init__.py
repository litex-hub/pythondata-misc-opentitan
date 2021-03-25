import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5589"
version_tuple = (0, 0, 5589)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5589")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5494"
data_version_tuple = (0, 0, 5494)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5494")
except ImportError:
    pass
data_git_hash = "b9b6165d496eb31731bfea755f0e01b0876faffd"
data_git_describe = "v0.0-5494-gb9b6165d4"
data_git_msg = """\
commit b9b6165d496eb31731bfea755f0e01b0876faffd
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 25 08:40:09 2021 +0000

    [sram_ctrl,lint] Fix width of RndCnstSramLfsrPermDefault
    
    This is a 160-bit parameter, so we should use a 160-bit
    default (silencing a lint warning). This is grabbed from the random
    constant we've currently got in top_earlgrey.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
