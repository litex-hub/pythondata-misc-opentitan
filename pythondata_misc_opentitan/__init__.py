import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12895"
version_tuple = (0, 0, 12895)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12895")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12753"
data_version_tuple = (0, 0, 12753)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12753")
except ImportError:
    pass
data_git_hash = "be5236c029f018715868d822a97407f6721f5582"
data_git_describe = "v0.0-12753-gbe5236c029"
data_git_msg = """\
commit be5236c029f018715868d822a97407f6721f5582
Author: Alexander Williams <awill@google.com>
Date:   Mon Jun 27 14:39:11 2022 -0700

    [usbdev] Do not write to unallocated buffer
    
    The "put" derived from the OUT state machine is not gated by whether a
    buffer is available. Prevent writing to an unallocated buffer by taking
    into consideration whether the AV FIFO is empty.
    
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
