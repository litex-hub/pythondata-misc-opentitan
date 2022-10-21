import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14867"
version_tuple = (0, 0, 14867)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14867")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14725"
data_version_tuple = (0, 0, 14725)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14725")
except ImportError:
    pass
data_git_hash = "aad7e8f8ed303374f9eff94ca75fae95f60f0fa9"
data_git_describe = "v0.0-14725-gaad7e8f8ed"
data_git_msg = """\
commit aad7e8f8ed303374f9eff94ca75fae95f60f0fa9
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 20 11:44:25 2022 -0700

    [doc/edn] Minor update on the EDN doc
    
    This PR updates two parts on EDN doc:
    1). Update the statement saying this version does not support alert
    2). Minor fix on a redundant word "only".
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
