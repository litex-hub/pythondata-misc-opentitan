import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11403"
version_tuple = (0, 0, 11403)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11403")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11277"
data_version_tuple = (0, 0, 11277)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11277")
except ImportError:
    pass
data_git_hash = "e321840afe2d4b7fd62e8c0493392a64e942a6f2"
data_git_describe = "v0.0-11277-ge321840af"
data_git_msg = """\
commit e321840afe2d4b7fd62e8c0493392a64e942a6f2
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Apr 6 11:30:26 2022 +0100

    [otbn, dv] Fixes regression failures in otbn_sec_cm
    
    This commit turns off StartStopStateValid assertion when fsm errors are
    injected.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
