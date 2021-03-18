import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5478"
version_tuple = (0, 0, 5478)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5478")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5383"
data_version_tuple = (0, 0, 5383)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5383")
except ImportError:
    pass
data_git_hash = "07494a3f350b69db7813bbb8f6e4579a05d42038"
data_git_describe = "v0.0-5383-g07494a3f3"
data_git_msg = """\
commit 07494a3f350b69db7813bbb8f6e4579a05d42038
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Thu Mar 18 15:59:57 2021 +0000

    [doc] Prefer relative links in Markdown
    
    Relative links make it easier to relocate files, prefer using them where
    possible.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
