import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5768"
version_tuple = (0, 0, 5768)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5768")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5673"
data_version_tuple = (0, 0, 5673)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5673")
except ImportError:
    pass
data_git_hash = "e029a68b6e781d14b5f1e51068b803837c0c62cd"
data_git_describe = "v0.0-5673-ge029a68b6"
data_git_msg = """\
commit e029a68b6e781d14b5f1e51068b803837c0c62cd
Author: Michael Schaffner <msf@google.com>
Date:   Tue Apr 6 16:21:30 2021 -0700

    [sysrst_ctrl/top] Instantiate sysrst_ctrl in top_earlgrey
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
