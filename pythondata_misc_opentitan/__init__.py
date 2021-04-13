import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5842"
version_tuple = (0, 0, 5842)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5842")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5747"
data_version_tuple = (0, 0, 5747)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5747")
except ImportError:
    pass
data_git_hash = "6f9c25b351c6e1c09197010da87c20e03466b49b"
data_git_describe = "v0.0-5747-g6f9c25b35"
data_git_msg = """\
commit 6f9c25b351c6e1c09197010da87c20e03466b49b
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Apr 12 19:28:16 2021 -0700

    [top] Fix a templating bug that breaks CI
    
    This appears to be a CI escape (possibly due to multiple PRs colliding),
    and causes multiply-driven errors in VCS.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
