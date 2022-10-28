import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15026"
version_tuple = (0, 0, 15026)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15026")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14884"
data_version_tuple = (0, 0, 14884)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14884")
except ImportError:
    pass
data_git_hash = "c081aeba37d1099adc29ebcd2525f9656e0f43cb"
data_git_describe = "v0.0-14884-gc081aeba37"
data_git_msg = """\
commit c081aeba37d1099adc29ebcd2525f9656e0f43cb
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Oct 28 11:32:02 2022 -0700

    [dv] remove unfinished tests from nightly dashboard
    
    Some ROM E2E tests that were not yet running in in DV were mistakenly
    added to the testplan "tests" reference field, which makes them show up
    incorrectly in the nightly dashboard.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
