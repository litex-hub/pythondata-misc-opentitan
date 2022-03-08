import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10762"
version_tuple = (0, 0, 10762)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10762")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10636"
data_version_tuple = (0, 0, 10636)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10636")
except ImportError:
    pass
data_git_hash = "8fd175f44f327a0f815ef89ecbbca28e3da145b4"
data_git_describe = "v0.0-10636-g8fd175f44"
data_git_msg = """\
commit 8fd175f44f327a0f815ef89ecbbca28e3da145b4
Author: Weicai Yang <weicai@google.com>
Date:   Wed Feb 23 21:27:17 2022 -0800

    [dv] Update V2S checklist
    
    Add an item - SIM_COVERAGE_REVIEWED
    Also clean up some TODO
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
