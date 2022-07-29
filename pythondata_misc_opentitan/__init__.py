import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13326"
version_tuple = (0, 0, 13326)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13326")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13184"
data_version_tuple = (0, 0, 13184)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13184")
except ImportError:
    pass
data_git_hash = "3db58a50e3b8739cfde242bbf29079a4707c888d"
data_git_describe = "v0.0-13184-g3db58a50e3"
data_git_msg = """\
commit 3db58a50e3b8739cfde242bbf29079a4707c888d
Author: Alexander Williams <awill@google.com>
Date:   Mon Jul 25 09:28:10 2022 -0700

    [fpga/cw310] Add hyperdebug variant of the CW310
    
    Add a new fusesoc core that switches in a hyperdebug-specific XDC for a
    CW310 bitstream build.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
