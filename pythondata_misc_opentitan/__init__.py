import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11422"
version_tuple = (0, 0, 11422)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11422")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11296"
data_version_tuple = (0, 0, 11296)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11296")
except ImportError:
    pass
data_git_hash = "28fff3babc12cda189798d0b51706c0b73b123a0"
data_git_describe = "v0.0-11296-g28fff3bab"
data_git_msg = """\
commit 28fff3babc12cda189798d0b51706c0b73b123a0
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Wed Apr 6 14:28:55 2022 +0100

    [sysrst_ctrl,dv] Remove CSR excl for KEY_INTR_STATUS register
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

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
