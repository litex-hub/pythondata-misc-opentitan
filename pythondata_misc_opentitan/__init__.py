import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14977"
version_tuple = (0, 0, 14977)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14977")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14835"
data_version_tuple = (0, 0, 14835)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14835")
except ImportError:
    pass
data_git_hash = "bb833ef26260ba0c4148a62c3cc16cc1841c6a65"
data_git_describe = "v0.0-14835-gbb833ef262"
data_git_msg = """\
commit bb833ef26260ba0c4148a62c3cc16cc1841c6a65
Author: Michael Schaffner <msf@google.com>
Date:   Wed Oct 26 16:58:37 2022 -0700

    [test] List tests for chip_lc_test_locked testpoint
    
    Fixes #15763
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
