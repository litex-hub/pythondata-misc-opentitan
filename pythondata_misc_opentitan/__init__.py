import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14575"
version_tuple = (0, 0, 14575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14433"
data_version_tuple = (0, 0, 14433)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14433")
except ImportError:
    pass
data_git_hash = "4afba27874da8a78d0c5f3d66759cb75f74f047a"
data_git_describe = "v0.0-14433-g4afba27874"
data_git_msg = """\
commit 4afba27874da8a78d0c5f3d66759cb75f74f047a
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Sep 30 21:42:49 2022 -0700

    [top/dv] Additional test updates to check isolated flash partition.
    
    The accessibility of the isolated partition should not be affected
    by the insertion of a scrambling key since it is in a region that
    is not scramble enabled.
    
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
