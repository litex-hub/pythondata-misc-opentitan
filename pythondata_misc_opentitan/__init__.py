import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15029"
version_tuple = (0, 0, 15029)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15029")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14887"
data_version_tuple = (0, 0, 14887)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14887")
except ImportError:
    pass
data_git_hash = "af907a42040b901a9579e92806af3f2eb3016e3d"
data_git_describe = "v0.0-14887-gaf907a4204"
data_git_msg = """\
commit af907a42040b901a9579e92806af3f2eb3016e3d
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Oct 25 17:56:55 2022 -0700

    [entropy_src/dv] Properly count coincident HT failures
    
    If Windowed, Continuous and/or External HT's simultaneously fail in the same sample
    the DUT's alert count only registers one failure, for the sample, which in generally
    fine.  However the previous approach at counting these coincident failures
    overestimated the overcounting factor and was unable to predict certain alerts.
    
    This commit corrects the accounting for alert counts when simultaneous alerts occur.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
