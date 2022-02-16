import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10371"
version_tuple = (0, 0, 10371)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10371")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10245"
data_version_tuple = (0, 0, 10245)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10245")
except ImportError:
    pass
data_git_hash = "7ff7336b02695bb0961cfeb4e98b103ade4fe692"
data_git_describe = "v0.0-10245-g7ff7336b0"
data_git_msg = """\
commit 7ff7336b02695bb0961cfeb4e98b103ade4fe692
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Feb 15 10:02:16 2022 -0800

    [rv_dm dv] Drive DUT inputs to known values
    
    - Initialize the inputs to the DUT with some random values
    - Constrain the inputs in the common seqeunce with amenable values
    
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
