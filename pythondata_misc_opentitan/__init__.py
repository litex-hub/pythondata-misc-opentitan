import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10728"
version_tuple = (0, 0, 10728)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10728")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10602"
data_version_tuple = (0, 0, 10602)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10602")
except ImportError:
    pass
data_git_hash = "620a9d1b32a73d9c35f859e04eddc99d36cc04f9"
data_git_describe = "v0.0-10602-g620a9d1b3"
data_git_msg = """\
commit 620a9d1b32a73d9c35f859e04eddc99d36cc04f9
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 4 12:16:00 2022 -0800

    [conn/top] Add lc_escalate_en connectivity checks
    
    This PR finishes a TODO in #11208
    
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
