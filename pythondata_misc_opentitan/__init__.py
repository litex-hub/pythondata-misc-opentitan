import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9746"
version_tuple = (0, 0, 9746)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9746")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9624"
data_version_tuple = (0, 0, 9624)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9624")
except ImportError:
    pass
data_git_hash = "dd26aba348d4308d9e0b057a9dde159154a1c6ed"
data_git_describe = "v0.0-9624-gdd26aba34"
data_git_msg = """\
commit dd26aba348d4308d9e0b057a9dde159154a1c6ed
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jan 21 22:00:34 2022 -0800

    [reggen] Add standard BUS.INTEGRITY label to generated non-security IPs
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
