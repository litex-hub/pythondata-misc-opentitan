import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13010"
version_tuple = (0, 0, 13010)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13010")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12868"
data_version_tuple = (0, 0, 12868)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12868")
except ImportError:
    pass
data_git_hash = "a4de3812bf7856afd6fc99c9fa80bfecf59df31f"
data_git_describe = "v0.0-12868-ga4de3812bf"
data_git_msg = """\
commit a4de3812bf7856afd6fc99c9fa80bfecf59df31f
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Jun 29 11:33:08 2022 +0100

    [otbn,fcov] Add coverpoint for UNIMP insn
    
    When we have this specific CSRRW insn (CSRRW x0, 0xC00, x0)
    that would be UNIMP. In order to guarantee that we see it
    an explicit coverpoint is needed.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
