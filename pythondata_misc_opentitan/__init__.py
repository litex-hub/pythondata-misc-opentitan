import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14798"
version_tuple = (0, 0, 14798)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14798")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14656"
data_version_tuple = (0, 0, 14656)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14656")
except ImportError:
    pass
data_git_hash = "62c7b5000a6716a8fd6dd0d54c2bfc6bcd2ecc75"
data_git_describe = "v0.0-14656-g62c7b5000a"
data_git_msg = """\
commit 62c7b5000a6716a8fd6dd0d54c2bfc6bcd2ecc75
Author: Hugo McNally <hugo.mcnally@gmail.com>
Date:   Mon Oct 17 20:35:48 2022 +0100

    [test] Added single fault check to cpu info test.
    
    Signed-off-by: Hugo McNally <hugo.mcnally@gmail.com>

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
