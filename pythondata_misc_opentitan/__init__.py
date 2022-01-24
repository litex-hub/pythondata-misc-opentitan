import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9717"
version_tuple = (0, 0, 9717)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9717")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9595"
data_version_tuple = (0, 0, 9595)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9595")
except ImportError:
    pass
data_git_hash = "f1661052e9676eadec99601bfa46485b2c0a85e1"
data_git_describe = "v0.0-9595-gf1661052e"
data_git_msg = """\
commit f1661052e9676eadec99601bfa46485b2c0a85e1
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 18 17:04:56 2022 -0800

    [flash_ctrl] D2 preparation steps
    
    - fully covnert to new sparse fsm
    - add additional fsms as needed
    
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
