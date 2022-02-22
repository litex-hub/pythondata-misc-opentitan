import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10461"
version_tuple = (0, 0, 10461)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10461")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10335"
data_version_tuple = (0, 0, 10335)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10335")
except ImportError:
    pass
data_git_hash = "5170831073729eb0874cf924fb324140084601e1"
data_git_describe = "v0.0-10335-g517083107"
data_git_msg = """\
commit 5170831073729eb0874cf924fb324140084601e1
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 18 12:49:33 2022 -0800

    [doc/kmac] Update kmac dv doc
    
    Two minor updates on kmac dv doc:
    1). update the link for testplan.
    2). update the functional coverage section to refer to testplan.
    
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
