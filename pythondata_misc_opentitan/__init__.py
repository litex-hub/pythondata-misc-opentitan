import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10581"
version_tuple = (0, 0, 10581)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10581")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10455"
data_version_tuple = (0, 0, 10455)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10455")
except ImportError:
    pass
data_git_hash = "d8c1e9c230d93910593472bf1f0962aa7d351a41"
data_git_describe = "v0.0-10455-gd8c1e9c23"
data_git_msg = """\
commit d8c1e9c230d93910593472bf1f0962aa7d351a41
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Feb 18 12:41:34 2022 -0800

    [dv] Add rv_dm to regressions
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
