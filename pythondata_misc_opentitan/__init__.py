import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9691"
version_tuple = (0, 0, 9691)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9691")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9569"
data_version_tuple = (0, 0, 9569)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9569")
except ImportError:
    pass
data_git_hash = "e408ebf4a40a36a59a79eb67878bcfa7193d7c25"
data_git_describe = "v0.0-9569-ge408ebf4a"
data_git_msg = """\
commit e408ebf4a40a36a59a79eb67878bcfa7193d7c25
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 18 12:51:51 2022 -0800

    [adc_ctrl] combine current status into new status
    
    - or the existing status into the next update to ensure filter
      match status is not lost
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
