import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10803"
version_tuple = (0, 0, 10803)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10803")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10677"
data_version_tuple = (0, 0, 10677)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10677")
except ImportError:
    pass
data_git_hash = "5babc8f790ee9ccfeac94031526ab30a305b21f1"
data_git_describe = "v0.0-10677-g5babc8f79"
data_git_msg = """\
commit 5babc8f790ee9ccfeac94031526ab30a305b21f1
Author: Alexander Williams <awill@google.com>
Date:   Wed Mar 9 11:28:52 2022 -0800

    [usbdev] Remove USB reset qualification of low_power
    
    The low_power signal does not need to be held off by the USB reset
    status, so remove it. The AON module is activated and deactivated by
    signals coming from the USB IP, and internal state changes only need
    depend on the signal from the pwrmgr.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
