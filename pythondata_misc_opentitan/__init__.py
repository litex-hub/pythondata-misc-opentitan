import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9881"
version_tuple = (0, 0, 9881)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9881")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9757"
data_version_tuple = (0, 0, 9757)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9757")
except ImportError:
    pass
data_git_hash = "1ecb03098e51f1a940a76e9d6e9e4fdc5e9170ad"
data_git_describe = "v0.0-9757-g1ecb03098"
data_git_msg = """\
commit 1ecb03098e51f1a940a76e9d6e9e4fdc5e9170ad
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Jan 27 08:44:07 2022 -0800

    [edn/rtl] Fix for auto-mode
    
    A timing delay fix is needed to make both auto_req and boot_req
    modes work together.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
