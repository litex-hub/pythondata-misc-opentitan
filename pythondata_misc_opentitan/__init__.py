import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14532"
version_tuple = (0, 0, 14532)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14532")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14390"
data_version_tuple = (0, 0, 14390)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14390")
except ImportError:
    pass
data_git_hash = "cfe71b5140093f4a1aa95dce80b4d3b81d333de3"
data_git_describe = "v0.0-14390-gcfe71b5140"
data_git_msg = """\
commit cfe71b5140093f4a1aa95dce80b4d3b81d333de3
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Tue Sep 27 15:53:17 2022 +0000

    [doc] Update motivation and objectives of DIFs
    
    The current DIF reference manual (RM) text emphasizes error checking and
    robustness of DIFs quite heavily ("making it difficult, or impossible,
    to misuse [hardware]." and "providing example code to aid the
    implementation of reference firmware including end-consumer
    applications").  However, DIFs are called in test code, some of which
    deliberately misuses a hardware module, so error checking and robustness
    are not a primary objective for DIFs and could hinder their use for
    tests.
    
    This PR changes the wording of the DIF RM to de-emphasize error checking
    and robustness.  The revised text is aligned with the understanding of
    the Software WG at their meeting on 2022-09-27.  It also matches the
    description in `sw/device/lib/dif/_index.md` more closely.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
