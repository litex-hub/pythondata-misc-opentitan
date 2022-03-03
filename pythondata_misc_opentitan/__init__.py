import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10690"
version_tuple = (0, 0, 10690)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10690")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10564"
data_version_tuple = (0, 0, 10564)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10564")
except ImportError:
    pass
data_git_hash = "6b03a2f69bb053c331256b3bbff75d1d85a51a87"
data_git_describe = "v0.0-10564-g6b03a2f69"
data_git_msg = """\
commit 6b03a2f69bb053c331256b3bbff75d1d85a51a87
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Mar 2 19:53:33 2022 -0800

    [dif/pwm] Implement remaining DIFs
    
    This commit implements all remaining DIFs for the PWM IP, including all
    get/set enablement DIFs and lock(ing) DIFs. Additionally this commit
    updates the DIF checklist to reflect these changes.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
