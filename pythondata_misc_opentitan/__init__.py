import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9958"
version_tuple = (0, 0, 9958)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9958")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9834"
data_version_tuple = (0, 0, 9834)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9834")
except ImportError:
    pass
data_git_hash = "5a668a31d2fe32769d317a3d90178dea76196447"
data_git_describe = "v0.0-9834-g5a668a31d"
data_git_msg = """\
commit 5a668a31d2fe32769d317a3d90178dea76196447
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Jan 31 14:52:22 2022 -0800

    [rv_dm dv] Remove old testbench components
    
    This commit removes the old testbench components that are up-to-date in
    the newly added testbench.
    
    There are still several defunct testbench pieces which will be removed
    subsequently, as progress towards V1 is made.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
