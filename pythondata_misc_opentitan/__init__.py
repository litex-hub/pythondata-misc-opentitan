import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5284"
version_tuple = (0, 0, 5284)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5284")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5189"
data_version_tuple = (0, 0, 5189)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5189")
except ImportError:
    pass
data_git_hash = "cd3ddb33bc56d9d80bbf2da6f5020f8d03f21b21"
data_git_describe = "v0.0-5189-gcd3ddb33b"
data_git_msg = """\
commit cd3ddb33bc56d9d80bbf2da6f5020f8d03f21b21
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Mar 4 20:34:43 2021 -0800

    [dv/sram] bijection test
    
    this PR implements the bijection test as described in the testplan.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
