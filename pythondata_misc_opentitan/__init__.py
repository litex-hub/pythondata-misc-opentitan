import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12428"
version_tuple = (0, 0, 12428)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12428")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12286"
data_version_tuple = (0, 0, 12286)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12286")
except ImportError:
    pass
data_git_hash = "1842d60e925f686f86186acc6dd07d8cf3001348"
data_git_describe = "v0.0-12286-g1842d60e9"
data_git_msg = """\
commit 1842d60e925f686f86186acc6dd07d8cf3001348
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Apr 22 16:35:53 2022 -0700

    [opentitantool] Add version command
    
    `opentitantool version` will print git version including SHA hash.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I719d30411bf05d6764f7f414344e533d66b61f35

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
