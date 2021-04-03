import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5704"
version_tuple = (0, 0, 5704)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5704")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5609"
data_version_tuple = (0, 0, 5609)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5609")
except ImportError:
    pass
data_git_hash = "e0eefbce8f1639d5e2e265442bfcec466ef57369"
data_git_describe = "v0.0-5609-ge0eefbce8"
data_git_msg = """\
commit e0eefbce8f1639d5e2e265442bfcec466ef57369
Author: Weicai Yang <weicai@google.com>
Date:   Fri Apr 2 11:37:18 2021 -0700

    [keymgr/dv] Fix scb for LC disable
    
    update state to StInvalid for LC disable
    and align with design when LC disable occurs, no hw/sw input error will happen
    
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
