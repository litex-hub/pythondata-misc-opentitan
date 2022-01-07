import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9368"
version_tuple = (0, 0, 9368)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9368")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9251"
data_version_tuple = (0, 0, 9251)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9251")
except ImportError:
    pass
data_git_hash = "a870ebef5ed5cd119647f00ffc5a028a56d88785"
data_git_describe = "v0.0-9251-ga870ebef5"
data_git_msg = """\
commit a870ebef5ed5cd119647f00ffc5a028a56d88785
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 6 11:21:07 2022 -0800

    [fpv/pinmux] Add aon_wkup assertions
    
    This PR adds aon_wkup_o assertions and changes aon_clk rate to be slower
    than clk_i.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
