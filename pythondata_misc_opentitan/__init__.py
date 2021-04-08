import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5788"
version_tuple = (0, 0, 5788)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5788")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5693"
data_version_tuple = (0, 0, 5693)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5693")
except ImportError:
    pass
data_git_hash = "c2a8fc9b1a06f70258e1de3a7facbfb0ca1e9536"
data_git_describe = "v0.0-5693-gc2a8fc9b1"
data_git_msg = """\
commit c2a8fc9b1a06f70258e1de3a7facbfb0ca1e9536
Author: Weicai Yang <weicai@google.com>
Date:   Tue Apr 6 17:37:34 2021 -0700

    [dv] Update `process_tl_access` args for all blocks
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
