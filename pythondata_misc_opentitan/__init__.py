import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12621"
version_tuple = (0, 0, 12621)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12621")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12479"
data_version_tuple = (0, 0, 12479)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12479")
except ImportError:
    pass
data_git_hash = "662e9dfcfe263d675ae1139831a56938b0240d83"
data_git_describe = "v0.0-12479-g662e9dfcf"
data_git_msg = """\
commit 662e9dfcfe263d675ae1139831a56938b0240d83
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jun 8 23:22:56 2022 -0700

    [dv] Update xcelium coverage config file
    
    Excluded statement coverage for tlul_assert, only enabled assertion
    coverage.
    Signed-off-by: Weicai Yang <weicai@google.com>

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
