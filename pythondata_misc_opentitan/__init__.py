import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8473"
version_tuple = (0, 0, 8473)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8473")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8361"
data_version_tuple = (0, 0, 8361)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8361")
except ImportError:
    pass
data_git_hash = "f0ec0dfbca422de353da798eaaab06d5cbfaab81"
data_git_describe = "v0.0-8361-gf0ec0dfbc"
data_git_msg = """\
commit f0ec0dfbca422de353da798eaaab06d5cbfaab81
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Oct 26 10:09:29 2021 +0100

    [otbn, dv] Picks signed base addresses while executing JALR
    
    An if block is added to check if the 32nd bit of base address is 1. If
    it is set, it means the base address is a negative address and it is
    converted into signed integer.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
