import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5111"
version_tuple = (0, 0, 5111)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5111")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5020"
data_version_tuple = (0, 0, 5020)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5020")
except ImportError:
    pass
data_git_hash = "d861bea1215bb42d3b07984a9f4fb8a4b7c0a82c"
data_git_describe = "v0.0-5020-gd861bea12"
data_git_msg = """\
commit d861bea1215bb42d3b07984a9f4fb8a4b7c0a82c
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Feb 22 10:00:58 2021 -0800

    [dv/otp_ctrl] update testplan to fix the unmapped test
    
    This PR updates the test sequence names and description to match the
    name of the sequences and avoid unmapped tests in regression results.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
