import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10257"
version_tuple = (0, 0, 10257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10133"
data_version_tuple = (0, 0, 10133)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10133")
except ImportError:
    pass
data_git_hash = "c15bbbfd478af1e335c1fc30c58ce03ee8c9ef98"
data_git_describe = "v0.0-10133-gc15bbbfd4"
data_git_msg = """\
commit c15bbbfd478af1e335c1fc30c58ce03ee8c9ef98
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Feb 11 09:42:24 2022 -0800

    [rtl/rstmgr] Remove superfluous assertion
    
    It caused trouble in some corner cases, and adds little value.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
