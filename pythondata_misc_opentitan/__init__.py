import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14432"
version_tuple = (0, 0, 14432)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14432")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14290"
data_version_tuple = (0, 0, 14290)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14290")
except ImportError:
    pass
data_git_hash = "f2a41db4f41ef6fe666c47340c3dc47b3e7169bc"
data_git_describe = "v0.0-14290-gf2a41db4f4"
data_git_msg = """\
commit f2a41db4f41ef6fe666c47340c3dc47b3e7169bc
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Mon Sep 26 08:57:55 2022 +0000

    [otbn,dv] Initialize `insn_addr_cg`
    
    This covergroup had not been initialized prior to this commit, so calls
    to `sample()` would result in an error.  This likely caused the last two
    OTBN nightly regression runs to fail.
    
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
