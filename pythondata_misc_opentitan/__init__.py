import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11105"
version_tuple = (0, 0, 11105)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11105")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10979"
data_version_tuple = (0, 0, 10979)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10979")
except ImportError:
    pass
data_git_hash = "acc825ff0cb0ee2344aede6fc05337ea7144c4f1"
data_git_describe = "v0.0-10979-gacc825ff0"
data_git_msg = """\
commit acc825ff0cb0ee2344aede6fc05337ea7144c4f1
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Mar 24 01:15:24 2022 -0700

    [dvsim] Treat `tests: ["N/A"]` as an ignored testpoint
    
    This came up in OTP ctrl review.
    With this commit, a testplan entry can be discarded by setting `tests: ["N/A"]`.
    This is useful for keeping the test entry, but not having it show up in the
    mapped simulation results / progress table.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
