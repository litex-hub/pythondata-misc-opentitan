import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10394"
version_tuple = (0, 0, 10394)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10394")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10268"
data_version_tuple = (0, 0, 10268)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10268")
except ImportError:
    pass
data_git_hash = "c8b6231addeafba7cbccf3cef98800eae1042787"
data_git_describe = "v0.0-10268-gc8b6231ad"
data_git_msg = """\
commit c8b6231addeafba7cbccf3cef98800eae1042787
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 15 11:55:23 2022 +0100

    [aes] Convert Masking and SBoxImpl parameters to Sec parameters
    
    These two parameters are security critical and we should reduce the risk
    of accidentally setting non-default values for these for tapeouts.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
