import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5774"
version_tuple = (0, 0, 5774)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5774")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5679"
data_version_tuple = (0, 0, 5679)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5679")
except ImportError:
    pass
data_git_hash = "9eb2a9c9fd5d8e8342b2a9da5d7e6470e2a26ebf"
data_git_describe = "v0.0-5679-g9eb2a9c9f"
data_git_msg = """\
commit 9eb2a9c9fd5d8e8342b2a9da5d7e6470e2a26ebf
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Sat Mar 20 15:53:30 2021 -0700

    [entropy_src/rtl] symbol-based repetition count health test
    
    An additional symobl-based repetition count health test is added.
    Changed the rep counter to initialize to 1, as NIST shows.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
