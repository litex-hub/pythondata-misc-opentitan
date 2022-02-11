import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10246"
version_tuple = (0, 0, 10246)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10246")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10122"
data_version_tuple = (0, 0, 10122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10122")
except ImportError:
    pass
data_git_hash = "1a2c4ec9327c24d2ee9bcba4c2a08983ed7a79c7"
data_git_describe = "v0.0-10122-g1a2c4ec93"
data_git_msg = """\
commit 1a2c4ec9327c24d2ee9bcba4c2a08983ed7a79c7
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Thu Feb 10 04:44:08 2022 -0800

    [aes/dv] fixed compile errors introduced with new rtl
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
