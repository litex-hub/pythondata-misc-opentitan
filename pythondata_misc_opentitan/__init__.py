import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15337"
version_tuple = (0, 0, 15337)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15337")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15195"
data_version_tuple = (0, 0, 15195)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15195")
except ImportError:
    pass
data_git_hash = "dd21c8a81c8c395b2c5a918bb1ef436840878ae4"
data_git_describe = "v0.0-15195-gdd21c8a81c"
data_git_msg = """\
commit dd21c8a81c8c395b2c5a918bb1ef436840878ae4
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Nov 7 23:51:36 2022 -0800

    [dv,test] simplify `chip_tap_straps_prod`
    
    This implements review feedback from #16053.
    
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
