import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11164"
version_tuple = (0, 0, 11164)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11164")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11038"
data_version_tuple = (0, 0, 11038)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11038")
except ImportError:
    pass
data_git_hash = "4805c5a1205a822a114fa8db100b066af46c7319"
data_git_describe = "v0.0-11038-g4805c5a12"
data_git_msg = """\
commit 4805c5a1205a822a114fa8db100b066af46c7319
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 25 11:29:16 2022 -0700

    [dv/chip] Fix csr_bit_bash failure
    
    This PR fixes csr_bit_bash failure due to random write illegal values
    that causes an assertion error. There is no RTL error so instead of
    excluding the registers, we will just disable the assertion.
    
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
