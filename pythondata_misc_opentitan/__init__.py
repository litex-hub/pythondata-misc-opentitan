import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12567"
version_tuple = (0, 0, 12567)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12567")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12425"
data_version_tuple = (0, 0, 12425)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12425")
except ImportError:
    pass
data_git_hash = "e7f754ffc8d592421981e7321aa254901df883f0"
data_git_describe = "v0.0-12425-ge7f754ffc"
data_git_msg = """\
commit e7f754ffc8d592421981e7321aa254901df883f0
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Jun 7 04:22:38 2022 -0700

    Refixed 12236 to a more rubust solution
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
