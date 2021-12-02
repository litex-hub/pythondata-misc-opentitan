import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8963"
version_tuple = (0, 0, 8963)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8963")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8851"
data_version_tuple = (0, 0, 8851)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8851")
except ImportError:
    pass
data_git_hash = "ddd38eef81257a44436cc84458954f60c1313243"
data_git_describe = "v0.0-8851-gddd38eef8"
data_git_msg = """\
commit ddd38eef81257a44436cc84458954f60c1313243
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Dec 2 10:31:02 2021 -0500

    [sw/silicon_creator] Add lifecycle_state_name_get()
    
    Values of the life cycle states were updated in #9319. This change adds
    a utility function for getting human-readable state names using the new
    state values.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
