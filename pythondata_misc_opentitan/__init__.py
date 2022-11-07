import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15307"
version_tuple = (0, 0, 15307)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15307")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15165"
data_version_tuple = (0, 0, 15165)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15165")
except ImportError:
    pass
data_git_hash = "f753444e59409b74182606be441024200a6b13c6"
data_git_describe = "v0.0-15165-gf753444e59"
data_git_msg = """\
commit f753444e59409b74182606be441024200a6b13c6
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Nov 7 13:58:10 2022 -0800

    [dv/clklmgr] Comment about the sec_cm testplan location
    
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
