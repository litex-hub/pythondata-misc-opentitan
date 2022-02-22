import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10466"
version_tuple = (0, 0, 10466)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10466")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10340"
data_version_tuple = (0, 0, 10340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10340")
except ImportError:
    pass
data_git_hash = "4fd50137f7dfac40a8c392c6069a2956d18f3c46"
data_git_describe = "v0.0-10340-g4fd50137f"
data_git_msg = """\
commit 4fd50137f7dfac40a8c392c6069a2956d18f3c46
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Fri Jan 7 12:13:58 2022 +0000

    [sysrst_ctrl,dv] Add flash write prot output test
    
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
