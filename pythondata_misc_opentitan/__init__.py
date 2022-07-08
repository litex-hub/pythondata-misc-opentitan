import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12977"
version_tuple = (0, 0, 12977)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12977")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12835"
data_version_tuple = (0, 0, 12835)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12835")
except ImportError:
    pass
data_git_hash = "ee49544c240fd58a9568877c46e6dfbb5260334d"
data_git_describe = "v0.0-12835-gee49544c24"
data_git_msg = """\
commit ee49544c240fd58a9568877c46e6dfbb5260334d
Author: Michał Mazurek <maz@semihalf.com>
Date:   Mon Jun 13 15:25:18 2022 +0200

    [opentitanlib] Add error cleaning to Ti50Emulator stop command
    
    Allows Ti50Emulator command stop to clear the error
    in case the sub-process is not running.
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
