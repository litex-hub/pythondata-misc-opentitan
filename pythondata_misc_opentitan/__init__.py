import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9523"
version_tuple = (0, 0, 9523)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9523")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9401"
data_version_tuple = (0, 0, 9401)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9401")
except ImportError:
    pass
data_git_hash = "f3b63da6c892ae3bf5526054623737f24eb53713"
data_git_describe = "v0.0-9401-gf3b63da6c"
data_git_msg = """\
commit f3b63da6c892ae3bf5526054623737f24eb53713
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sun Jan 9 13:14:26 2022 -0800

    [fpv/pinmux] V1 checklist
    
    This PR updates V1 checklist and status.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
