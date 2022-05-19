import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12241"
version_tuple = (0, 0, 12241)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12241")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12113"
data_version_tuple = (0, 0, 12113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12113")
except ImportError:
    pass
data_git_hash = "69766dd58d497e6bba429bb4110b45a66f7ce7ab"
data_git_describe = "v0.0-12113-g69766dd58"
data_git_msg = """\
commit 69766dd58d497e6bba429bb4110b45a66f7ce7ab
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Thu May 19 13:38:50 2022 +0100

    [sysrst_ctrl,dv] Fix the combo detect seq name in stress all test
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
