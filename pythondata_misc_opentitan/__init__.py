import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14393"
version_tuple = (0, 0, 14393)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14393")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14251"
data_version_tuple = (0, 0, 14251)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14251")
except ImportError:
    pass
data_git_hash = "42313dc0381e53a01e6b251d6596089b9898afbf"
data_git_describe = "v0.0-14251-g42313dc038"
data_git_msg = """\
commit 42313dc0381e53a01e6b251d6596089b9898afbf
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Sep 16 09:26:38 2022 +0100

    [otbn,dv] Turn off some assertions in FI tests
    
    This commit groups blanking assertions and DMEM assertions with
    DV_ASSERT_CTRL macro and turns them off in fault injection tests
    since it is not guaranteed to be able to blank in those cases.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
