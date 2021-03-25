import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5590"
version_tuple = (0, 0, 5590)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5590")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5495"
data_version_tuple = (0, 0, 5495)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5495")
except ImportError:
    pass
data_git_hash = "be7f5a59dca20ad84db4d5b16e89268a9a46c005"
data_git_describe = "v0.0-5495-gbe7f5a59d"
data_git_msg = """\
commit be7f5a59dca20ad84db4d5b16e89268a9a46c005
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Mar 25 08:31:49 2021 -0700

    [kmac] Change App Intf to unpacked array
    
    This commit changes `app_i/o` to array port in kmac_app module.
    Its size is determined by `NumAppIntf` parameter in kmac_pkg.
    
    To arbitrate among the requests, fixed priority arbiter module is used.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
