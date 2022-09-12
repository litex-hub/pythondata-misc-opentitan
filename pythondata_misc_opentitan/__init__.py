import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14139"
version_tuple = (0, 0, 14139)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14139")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13997"
data_version_tuple = (0, 0, 13997)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13997")
except ImportError:
    pass
data_git_hash = "a00ce54bf6341a296c0d3864008487e0b65e5787"
data_git_describe = "v0.0-13997-ga00ce54bf6"
data_git_msg = """\
commit a00ce54bf6341a296c0d3864008487e0b65e5787
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Sep 8 14:29:42 2022 -0700

    [dv/kmac] clean up void usage in predict function
    
    This PR cleans up using `void` for ral predict function, instead I
    should use `DV_CHECK`.
    
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
