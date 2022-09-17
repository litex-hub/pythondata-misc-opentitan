import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14285"
version_tuple = (0, 0, 14285)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14285")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14143"
data_version_tuple = (0, 0, 14143)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14143")
except ImportError:
    pass
data_git_hash = "eaa2430855297f50971c1fefe4d03e14a0febc60"
data_git_describe = "v0.0-14143-geaa2430855"
data_git_msg = """\
commit eaa2430855297f50971c1fefe4d03e14a0febc60
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Sep 16 10:23:40 2022 -0700

    [top/dv] Add some basic IO tests to the smoke regression
    
    This ensures smoke functionality and also ensures that
    block level DV agent changes do not break top level
    test functionality.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
