import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12830"
version_tuple = (0, 0, 12830)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12830")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12688"
data_version_tuple = (0, 0, 12688)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12688")
except ImportError:
    pass
data_git_hash = "1b111f4e5060f3eb308f59761c85daebb373c01f"
data_git_describe = "v0.0-12688-g1b111f4e50"
data_git_msg = """\
commit 1b111f4e5060f3eb308f59761c85daebb373c01f
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Jun 23 18:44:08 2022 +0100

    [otbn,rtl] Connect insn addr mismatch to escalate
    
    Fixes #13323
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
