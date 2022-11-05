import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15258"
version_tuple = (0, 0, 15258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15116"
data_version_tuple = (0, 0, 15116)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15116")
except ImportError:
    pass
data_git_hash = "e79ed27d68a104c310817f18b577808d246fcf85"
data_git_describe = "v0.0-15116-ge79ed27d68"
data_git_msg = """\
commit e79ed27d68a104c310817f18b577808d246fcf85
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Nov 4 20:49:11 2022 -0700

    [dv/rstmgr] Update reset consistency checker instances
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
