import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13166"
version_tuple = (0, 0, 13166)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13166")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13024"
data_version_tuple = (0, 0, 13024)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13024")
except ImportError:
    pass
data_git_hash = "017232d57497c317129acf017ab91eab02a35d30"
data_git_describe = "v0.0-13024-g017232d574"
data_git_msg = """\
commit 017232d57497c317129acf017ab91eab02a35d30
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Tue Jul 19 10:03:07 2022 +0200

    [otbn,dv] Fix reset during EDN request (again)
    
    This commit reapplies 40dea7f638 (#13294), which had been partially
    undone in 3c7192597e (part of #13391).
    
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
