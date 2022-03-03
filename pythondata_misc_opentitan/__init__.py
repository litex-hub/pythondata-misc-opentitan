import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10680"
version_tuple = (0, 0, 10680)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10680")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10554"
data_version_tuple = (0, 0, 10554)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10554")
except ImportError:
    pass
data_git_hash = "34e37876127b2fcb4c12fc80daf0fbb60f07f056"
data_git_describe = "v0.0-10554-g34e378761"
data_git_msg = """\
commit 34e37876127b2fcb4c12fc80daf0fbb60f07f056
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Feb 24 06:05:36 2022 -0800

    [entropy_src/data] Remove exclusions to increase coverage
    
    Certain exclusion tags have been removed from the hjson file
    so that coverage can increase while avoiding false miscompares.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
