import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10414"
version_tuple = (0, 0, 10414)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10414")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10288"
data_version_tuple = (0, 0, 10288)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10288")
except ImportError:
    pass
data_git_hash = "41594d6d76f2f2eeb639ae1b45f22f4f4a7587c0"
data_git_describe = "v0.0-10288-g41594d6d7"
data_git_msg = """\
commit 41594d6d76f2f2eeb639ae1b45f22f4f4a7587c0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 16 22:41:59 2022 -0800

    [dv/kmac] Drive entropy related CSRs
    
    This PR drives entropy related CSRs to refresh entropy.
    
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
