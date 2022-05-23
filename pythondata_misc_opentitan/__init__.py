import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12287"
version_tuple = (0, 0, 12287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12159"
data_version_tuple = (0, 0, 12159)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12159")
except ImportError:
    pass
data_git_hash = "256f09bd6cfc255df5636ec75230392536bdc2f7"
data_git_describe = "v0.0-12159-g256f09bd6"
data_git_msg = """\
commit 256f09bd6cfc255df5636ec75230392536bdc2f7
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon May 16 15:49:26 2022 -0700

    [dv/chip] LC_walkthrough test [PART3]
    
    Adding a transition to RMA state using the RMA token.
    This PR adds the following transitions:
    1). RAW -> TESTUNLOCK0 -> PROD -> RMA
    2). RAW -> TESTUNLOCK0 -> DEV -> RMA
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
