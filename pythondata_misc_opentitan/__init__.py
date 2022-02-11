import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10251"
version_tuple = (0, 0, 10251)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10251")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10127"
data_version_tuple = (0, 0, 10127)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10127")
except ImportError:
    pass
data_git_hash = "dbe7801fe1635cb930cc5a63d06555b3e7a2f4ab"
data_git_describe = "v0.0-10127-gdbe7801fe"
data_git_msg = """\
commit dbe7801fe1635cb930cc5a63d06555b3e7a2f4ab
Author: Alexander Williams <awill@google.com>
Date:   Thu Feb 10 16:22:09 2022 -0800

    [pinmux/sw] Replace hard-coded with named constant
    
    Use the named constant in this pre-DIF software.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
