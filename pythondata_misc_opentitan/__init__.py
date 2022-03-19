import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10991"
version_tuple = (0, 0, 10991)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10991")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10865"
data_version_tuple = (0, 0, 10865)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10865")
except ImportError:
    pass
data_git_hash = "89ea59eb3e6062030b2aba841911b3a1311d0efb"
data_git_describe = "v0.0-10865-g89ea59eb3"
data_git_msg = """\
commit 89ea59eb3e6062030b2aba841911b3a1311d0efb
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Mar 18 00:54:15 2022 -0700

    [rv_dm dv] Set cover_reg_top cov criteria
    
    Add more safe hierarchies for coverage collection in non-functional
    common tests that use the cover_reg_top build.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
