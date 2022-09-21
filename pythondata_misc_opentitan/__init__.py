import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14360"
version_tuple = (0, 0, 14360)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14360")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14218"
data_version_tuple = (0, 0, 14218)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14218")
except ImportError:
    pass
data_git_hash = "6978ac72828fabd72fd9aaf3c071d07157c125b9"
data_git_describe = "v0.0-14218-g6978ac7282"
data_git_msg = """\
commit 6978ac72828fabd72fd9aaf3c071d07157c125b9
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Sep 20 18:18:04 2022 -0700

    fix(chip): Fix index size
    
    Index size of `miodio_to_ios()` function was incorrect.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
