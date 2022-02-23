import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10494"
version_tuple = (0, 0, 10494)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10494")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10368"
data_version_tuple = (0, 0, 10368)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10368")
except ImportError:
    pass
data_git_hash = "db0bba351980251bc2775e5af8dacaf8b6085f09"
data_git_describe = "v0.0-10368-gdb0bba351"
data_git_msg = """\
commit db0bba351980251bc2775e5af8dacaf8b6085f09
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Sat Feb 19 14:45:46 2022 -0800

    [edn/rtl] fix bug on auto req mode cmd valid
    
    When a reworking of the main state machine was done, a
    bug was created on the CSRNG command valid signal.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
