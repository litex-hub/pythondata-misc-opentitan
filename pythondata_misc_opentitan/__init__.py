import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12229"
version_tuple = (0, 0, 12229)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12229")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12101"
data_version_tuple = (0, 0, 12101)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12101")
except ImportError:
    pass
data_git_hash = "30f5670173119b5a449578e08a152d4f298ffac4"
data_git_describe = "v0.0-12101-g30f567017"
data_git_msg = """\
commit 30f5670173119b5a449578e08a152d4f298ffac4
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed May 18 15:11:11 2022 -0700

    [dv/chip] Update chip-level testplan
    
    1). Update some tests that have been implemented by other chip level
      tests.
    2). Fix some sequence name mismatches/typos.
    
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
