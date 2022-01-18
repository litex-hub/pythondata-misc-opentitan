import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9591"
version_tuple = (0, 0, 9591)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9591")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9469"
data_version_tuple = (0, 0, 9469)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9469")
except ImportError:
    pass
data_git_hash = "724b74102f2141cf6a3c71cf0ce35815e9ab8524"
data_git_describe = "v0.0-9469-g724b74102"
data_git_msg = """\
commit 724b74102f2141cf6a3c71cf0ce35815e9ab8524
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jan 14 15:46:41 2022 -0800

    [dv/jtag] Add a runtime switch `create_jtag_map`
    
    This PR adds a runtime switch `create_jtag_map` to reuse the code to
    clone a jtag_map from default_map.
    
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
