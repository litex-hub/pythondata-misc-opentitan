import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10189"
version_tuple = (0, 0, 10189)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10189")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10065"
data_version_tuple = (0, 0, 10065)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10065")
except ImportError:
    pass
data_git_hash = "db0ffc00954f03d9e6e5dcaa7c54cad52077f4bd"
data_git_describe = "v0.0-10065-gdb0ffc009"
data_git_msg = """\
commit db0ffc00954f03d9e6e5dcaa7c54cad52077f4bd
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 4 15:35:32 2022 -0800

    [flash_ctrl] D2S checklist and rtl annotation
    
    - Also add an anchor buffer to integrity error
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
