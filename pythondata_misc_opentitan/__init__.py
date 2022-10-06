import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14593"
version_tuple = (0, 0, 14593)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14593")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14451"
data_version_tuple = (0, 0, 14451)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14451")
except ImportError:
    pass
data_git_hash = "6d6115fd069c50cfd11dcb6f2563d82671dd2f10"
data_git_describe = "v0.0-14451-g6d6115fd06"
data_git_msg = """\
commit 6d6115fd069c50cfd11dcb6f2563d82671dd2f10
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Oct 4 18:13:55 2022 -0700

    [dv] add several Xcelium regressions to scale up presubmit testing
    
    This adds several top-level test regression suites to enable scaling up
    DV presubmit testing in CI using Xcelium.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
