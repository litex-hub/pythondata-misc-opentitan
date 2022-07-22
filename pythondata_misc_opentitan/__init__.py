import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13244"
version_tuple = (0, 0, 13244)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13244")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13102"
data_version_tuple = (0, 0, 13102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13102")
except ImportError:
    pass
data_git_hash = "ac970dca4a99c488abd769d9ad4925293c49486d"
data_git_describe = "v0.0-13102-gac970dca4a"
data_git_msg = """\
commit ac970dca4a99c488abd769d9ad4925293c49486d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jul 21 16:06:35 2022 -0700

    [dv/chip] Update sw_nmi_irq testplan
    
    This PR modifies the testplan for chip_sw_nmi_irq
    
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
