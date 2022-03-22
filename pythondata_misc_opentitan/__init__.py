import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11021"
version_tuple = (0, 0, 11021)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11021")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10895"
data_version_tuple = (0, 0, 10895)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10895")
except ImportError:
    pass
data_git_hash = "311983c3c842c21230acbe09da10703e14cc5bb8"
data_git_describe = "v0.0-10895-g311983c3c"
data_git_msg = """\
commit 311983c3c842c21230acbe09da10703e14cc5bb8
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Tue Mar 22 14:56:02 2022 +0000

    [sysrst_ctrl,dv] Randomize flash_wp_l_in for flash_wp_prot test
    
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
