import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11228"
version_tuple = (0, 0, 11228)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11228")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11102"
data_version_tuple = (0, 0, 11102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11102")
except ImportError:
    pass
data_git_hash = "d8eb7a2d29a2b105e81810da8781b1f588da8a49"
data_git_describe = "v0.0-11102-gd8eb7a2d2"
data_git_msg = """\
commit d8eb7a2d29a2b105e81810da8781b1f588da8a49
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Mar 30 14:09:26 2022 -0700

    [conn/clk] Update otbn clk connection
    
    OTBN EDN clk is updated to connect to `clk_main_secure` from clkmgr.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
