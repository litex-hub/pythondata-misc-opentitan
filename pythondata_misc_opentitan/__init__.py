import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9462"
version_tuple = (0, 0, 9462)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9462")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9344"
data_version_tuple = (0, 0, 9344)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9344")
except ImportError:
    pass
data_git_hash = "d5413a727ad941c6ad817011706569399c8956ca"
data_git_describe = "v0.0-9344-gd5413a727"
data_git_msg = """\
commit d5413a727ad941c6ad817011706569399c8956ca
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 11 12:56:52 2022 -0800

    [flash_ctrl] Documentation update
    
    - clarify behavior and usage of flash read buffers
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
