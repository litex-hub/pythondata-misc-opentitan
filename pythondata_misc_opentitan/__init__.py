import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10889"
version_tuple = (0, 0, 10889)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10889")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10763"
data_version_tuple = (0, 0, 10763)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10763")
except ImportError:
    pass
data_git_hash = "6813c96838d2aa989fcadd9381b6a4bba9c80bcf"
data_git_describe = "v0.0-10763-g6813c9683"
data_git_msg = """\
commit 6813c96838d2aa989fcadd9381b6a4bba9c80bcf
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Mon Feb 21 02:23:04 2022 -0800

    [aes/cover] added cover sample to scoreboad
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
