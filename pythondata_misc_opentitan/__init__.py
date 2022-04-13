import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11543"
version_tuple = (0, 0, 11543)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11543")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11417"
data_version_tuple = (0, 0, 11417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11417")
except ImportError:
    pass
data_git_hash = "913a02d91a7c51fc4b8397cc73affbce0ca3ad23"
data_git_describe = "v0.0-11417-g913a02d91"
data_git_msg = """\
commit 913a02d91a7c51fc4b8397cc73affbce0ca3ad23
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Apr 12 14:40:44 2022 -0700

    [dv/chip] Fix regression build-seed failure
    
    This PR fixes regression top-level failure when using `--build-seed`
    option. This temp solution won't randomize OTP image until we found the
    issue.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
