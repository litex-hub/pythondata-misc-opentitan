import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12884"
version_tuple = (0, 0, 12884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12742"
data_version_tuple = (0, 0, 12742)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12742")
except ImportError:
    pass
data_git_hash = "b6544149552c484f1caa78ef578a867bff0b5f8d"
data_git_describe = "v0.0-12742-gb654414955"
data_git_msg = """\
commit b6544149552c484f1caa78ef578a867bff0b5f8d
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jun 22 10:46:50 2022 -0400

    [CI] Shorter names for all the tests that don't fit on a column for me
    
    We only see about 20 characters of the display names in most cases so
    the most important information should be in those 20 characters.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
