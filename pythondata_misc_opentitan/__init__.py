import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9884"
version_tuple = (0, 0, 9884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9760"
data_version_tuple = (0, 0, 9760)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9760")
except ImportError:
    pass
data_git_hash = "56993601686be6018a0784b963fd0a09b3e1e410"
data_git_describe = "v0.0-9760-g569936016"
data_git_msg = """\
commit 56993601686be6018a0784b963fd0a09b3e1e410
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 27 10:42:26 2022 -0800

    [dv/hmac] Enhance stress_all_with_rand_reset to reset at target timing
    
    Follow the suggestion from PR #10397, thanks Rupert for the feedback!
    Definitely help reduced a test.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
