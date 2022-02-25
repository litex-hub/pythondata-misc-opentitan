import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10546"
version_tuple = (0, 0, 10546)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10546")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10420"
data_version_tuple = (0, 0, 10420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10420")
except ImportError:
    pass
data_git_hash = "bf77c5f2ae1ac443d75b47498484f1a458ce0538"
data_git_describe = "v0.0-10420-gbf77c5f2a"
data_git_msg = """\
commit bf77c5f2ae1ac443d75b47498484f1a458ce0538
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Feb 23 15:18:22 2022 +0000

    [otbn,dv] Check DMEM to happen at start of wipe
    
    This commit ensures that the DMEM checking only happens
    when we have just started wiping (checks with the old key)
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
