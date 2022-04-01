import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11274"
version_tuple = (0, 0, 11274)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11274")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11148"
data_version_tuple = (0, 0, 11148)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11148")
except ImportError:
    pass
data_git_hash = "c9f41377ba08715d659ae55266982965da61f67c"
data_git_describe = "v0.0-11148-gc9f41377b"
data_git_msg = """\
commit c9f41377ba08715d659ae55266982965da61f67c
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 31 11:26:50 2022 -0700

    [flash_ctrl] make the rma termination process clearer
    
    - make it clear that after rma completes the flash controller disables itself
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
