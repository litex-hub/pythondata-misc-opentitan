import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10868"
version_tuple = (0, 0, 10868)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10868")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10742"
data_version_tuple = (0, 0, 10742)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10742")
except ImportError:
    pass
data_git_hash = "91938337a5966c83a0c3826dd853aa329207a84e"
data_git_describe = "v0.0-10742-g91938337a"
data_git_msg = """\
commit 91938337a5966c83a0c3826dd853aa329207a84e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Mar 9 20:48:31 2022 -0800

    [dv/kmac] Update shadow reg
    
    As fix #11307 is merged, this PR updates and fixes a few corner cases in
    shadow reg.
    1). Clear shadowed reg update eror when `err_processed` is set.
    2). Disable a few assertions when storage error happened.
    
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
