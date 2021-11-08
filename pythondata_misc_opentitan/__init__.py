import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8633"
version_tuple = (0, 0, 8633)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8633")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8521"
data_version_tuple = (0, 0, 8521)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8521")
except ImportError:
    pass
data_git_hash = "125cbc61defa6566c625ea6794b8a7e8e3bb4bf9"
data_git_describe = "v0.0-8521-g125cbc61d"
data_git_msg = """\
commit 125cbc61defa6566c625ea6794b8a7e8e3bb4bf9
Author: Weicai Yang <weicai@google.com>
Date:   Fri Nov 5 14:42:21 2021 -0700

    [top/dv] Fix spi device failure
    
    When the interrupt keeps firing, PC can not go back to the main program,
    Changed to disable the interrupt in interrupt routine instead of in the
    main program
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
