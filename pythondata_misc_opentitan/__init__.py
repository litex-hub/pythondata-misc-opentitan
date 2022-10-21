import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14890"
version_tuple = (0, 0, 14890)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14890")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14748"
data_version_tuple = (0, 0, 14748)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14748")
except ImportError:
    pass
data_git_hash = "e3651d7abada0598ada1742d7903db616675353a"
data_git_describe = "v0.0-14748-ge3651d7aba"
data_git_msg = """\
commit e3651d7abada0598ada1742d7903db616675353a
Author: Michael Schaffner <msf@google.com>
Date:   Fri Oct 21 13:56:22 2022 -0700

    [rv_dm] Add comment to ROM window in Hjson
    
    Explains that the HaltAddress, ResumeAddress
    and ExceptionAddress locations are part of the ROM.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
