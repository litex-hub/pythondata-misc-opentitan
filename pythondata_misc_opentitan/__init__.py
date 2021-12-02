import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8970"
version_tuple = (0, 0, 8970)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8970")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8858"
data_version_tuple = (0, 0, 8858)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8858")
except ImportError:
    pass
data_git_hash = "e752910da4375ee7b1d297a3e3833a70d6ccdb1b"
data_git_describe = "v0.0-8858-ge752910da"
data_git_msg = """\
commit e752910da4375ee7b1d297a3e3833a70d6ccdb1b
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Dec 1 17:23:34 2021 -0800

    [dv/alert_esc_agent] Add alert_esc lpg coverage
    
    Add coverage on alert and ping's lpg.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
