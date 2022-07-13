import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13062"
version_tuple = (0, 0, 13062)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13062")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12920"
data_version_tuple = (0, 0, 12920)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12920")
except ImportError:
    pass
data_git_hash = "170f37016ed77437f48b5648b89baa4a8ba1df2d"
data_git_describe = "v0.0-12920-g170f37016e"
data_git_msg = """\
commit 170f37016ed77437f48b5648b89baa4a8ba1df2d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jul 12 14:06:26 2022 -0700

    [dv/alert_handler] Remove regwen related cov
    
    Regwen cov is replaced by automated coverbins
    "regwen_val_when_new_value_written_cg" from dv_abse_reg_pkg.
    
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
