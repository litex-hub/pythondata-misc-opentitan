import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14268"
version_tuple = (0, 0, 14268)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14268")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14126"
data_version_tuple = (0, 0, 14126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14126")
except ImportError:
    pass
data_git_hash = "e3894c4e4dd8e2cd612ec340e2f7ec2b9a588c38"
data_git_describe = "v0.0-14126-ge3894c4e4d"
data_git_msg = """\
commit e3894c4e4dd8e2cd612ec340e2f7ec2b9a588c38
Author: Michael Schaffner <msf@google.com>
Date:   Mon Sep 12 20:40:43 2022 -0700

    [test] Do not use PLIC for NMI test
    
    This disables regular interrupts and the PLIC for the NMI test so that
    we can be certain that the NMI handler is triggered via NMI channels
    only.
    
    Fix #14673
    
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
