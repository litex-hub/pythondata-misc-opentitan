import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14224"
version_tuple = (0, 0, 14224)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14224")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14082"
data_version_tuple = (0, 0, 14082)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14082")
except ImportError:
    pass
data_git_hash = "259a661278b1a5e8aa1aa3424a6bef6a7675efae"
data_git_describe = "v0.0-14082-g259a661278"
data_git_msg = """\
commit 259a661278b1a5e8aa1aa3424a6bef6a7675efae
Author: Johnathan Van Why <jrvanwhy@google.com>
Date:   Thu Sep 8 09:46:13 2022 -0700

    Move opentitantool's set-pll and load-bitstream commands into a new fpga command group.
    
    In a future PR, I will add a new command to this group to reset the FPGA board (described in #14686).
    
    Signed-off-by: Johnathan Van Why <jrvanwhy@google.com>

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
