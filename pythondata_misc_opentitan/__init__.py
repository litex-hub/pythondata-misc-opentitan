import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12936"
version_tuple = (0, 0, 12936)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12936")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12794"
data_version_tuple = (0, 0, 12794)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12794")
except ImportError:
    pass
data_git_hash = "74186fbc474d590b9599e5b37806cbfb4641bbe8"
data_git_describe = "v0.0-12794-g74186fbc47"
data_git_msg = """\
commit 74186fbc474d590b9599e5b37806cbfb4641bbe8
Author: Hugo McNally <hugo.mcnally@gmail.com>
Date:   Thu Jun 30 15:53:57 2022 +0100

    [dif, rv_core_ibex] More flexible addr translation
    
    General dif API changes for ibex's address translation with added
    features, such as ability to disable address translation once enabled.
    
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
