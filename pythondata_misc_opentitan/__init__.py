import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11027"
version_tuple = (0, 0, 11027)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11027")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10901"
data_version_tuple = (0, 0, 10901)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10901")
except ImportError:
    pass
data_git_hash = "a3ace41618c68a6a481194b097f2a5ea913508bd"
data_git_describe = "v0.0-10901-ga3ace4161"
data_git_msg = """\
commit a3ace41618c68a6a481194b097f2a5ea913508bd
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Tue Dec 21 13:38:57 2021 +0000

    [sysrst_ctrl,dv] Add sysrst_ctrl edge detect test
    
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
