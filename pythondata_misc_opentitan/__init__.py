import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13093"
version_tuple = (0, 0, 13093)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13093")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12951"
data_version_tuple = (0, 0, 12951)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12951")
except ImportError:
    pass
data_git_hash = "5de589cd275f9c67b4cf02d80e2471b8f22de231"
data_git_describe = "v0.0-12951-g5de589cd27"
data_git_msg = """\
commit 5de589cd275f9c67b4cf02d80e2471b8f22de231
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jul 14 10:40:23 2022 -0700

    [dv/clkmgr] Fix sporadic stress test failures
    
    Make sure resets will consistently start clocks. The measurement timeout
    counter measure tests were leaving some clocks inactive.
    Fix some log and asserton typos that cause confusion.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
