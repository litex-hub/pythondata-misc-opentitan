import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13185"
version_tuple = (0, 0, 13185)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13185")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13043"
data_version_tuple = (0, 0, 13043)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13043")
except ImportError:
    pass
data_git_hash = "1df07f798273d74a465ca5f9fbfbae322b6303ba"
data_git_describe = "v0.0-13043-g1df07f7982"
data_git_msg = """\
commit 1df07f798273d74a465ca5f9fbfbae322b6303ba
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Mon Jul 18 18:23:54 2022 +0200

    [otbn,data] Fix synopsis of `bn.mulqacc.wo` instruction
    
    This instruction writes the full 256-bit accumulator value to the
    destination WDR, not just the lower 128 bit (which `bn.mulqacc.so`
    does).  Prior to this commit, the synopsis of the `bn.mulqacc.wo`
    instruction was incorrect in this regard.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
