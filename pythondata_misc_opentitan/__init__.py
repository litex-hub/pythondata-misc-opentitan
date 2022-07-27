import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13281"
version_tuple = (0, 0, 13281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13139"
data_version_tuple = (0, 0, 13139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13139")
except ImportError:
    pass
data_git_hash = "542ef5653be7bcc1e1af4e01e75641c089475cf5"
data_git_describe = "v0.0-13139-g542ef5653b"
data_git_msg = """\
commit 542ef5653be7bcc1e1af4e01e75641c089475cf5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jul 15 10:15:32 2022 -0700

    [alert_handler] Update checklist and move to D3
    
    Fix #13576
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
