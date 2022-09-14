import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14203"
version_tuple = (0, 0, 14203)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14203")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14061"
data_version_tuple = (0, 0, 14061)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14061")
except ImportError:
    pass
data_git_hash = "18419550510bc8327550cfb9a49beacbb66c535b"
data_git_describe = "v0.0-14061-g1841955051"
data_git_msg = """\
commit 18419550510bc8327550cfb9a49beacbb66c535b
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Feb 19 17:19:53 2022 -0800

    [entropy_src/rtl] Standardize Ext. Health Test Interface
    
    In preparation for creating an agent for the external health test,
    this commit updates the extht interface to make it more consistent
    with the current implementation of the other health checks.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
