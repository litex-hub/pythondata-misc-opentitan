import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12886"
version_tuple = (0, 0, 12886)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12886")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12744"
data_version_tuple = (0, 0, 12744)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12744")
except ImportError:
    pass
data_git_hash = "1c8f1e426fb6a3df9c38cef5082896467b6340e3"
data_git_describe = "v0.0-12744-g1c8f1e426f"
data_git_msg = """\
commit 1c8f1e426fb6a3df9c38cef5082896467b6340e3
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jun 9 16:36:00 2022 -0700

    [dv/chip] Update chip-level LPG testplan
    
    This PR adds an enhancement to alert's LPG testplan.
    It adds to scenarios where rst/clk mgrs can turn off IP's clock or
    toggle reset.
    
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
