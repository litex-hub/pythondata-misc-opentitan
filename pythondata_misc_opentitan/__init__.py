import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12889"
version_tuple = (0, 0, 12889)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12889")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12747"
data_version_tuple = (0, 0, 12747)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12747")
except ImportError:
    pass
data_git_hash = "dd97ef8a84a055a0f0b4d730cdf61bcb6535020e"
data_git_describe = "v0.0-12747-gdd97ef8a84"
data_git_msg = """\
commit dd97ef8a84a055a0f0b4d730cdf61bcb6535020e
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Jun 9 16:46:32 2022 +0200

    [otbn] Feed blanked shifter output into Adder Y when not using Adder Y
    
    Previously, the MOD WSR was fed into Adder Y during some ALU operations
    not requiring Adder Y at all (RSHI, XOR, OR, AND, NOT). Since the
    output of Adder Y is connected to the zero flag generation (ORing all
    bits together), this could lead to undesired SCA leakage.
    
    As we already correctly blank the shifter output connected to Adder Y,
    it's better select this as input for Adder Y when not using Adder Y to
    avoid undesired leakage due to the zero flag generation.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
