import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5230"
version_tuple = (0, 0, 5230)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5230")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5139"
data_version_tuple = (0, 0, 5139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5139")
except ImportError:
    pass
data_git_hash = "bc4df4bb63165bfd60c7037291e4e41d20c5d4bd"
data_git_describe = "v0.0-5139-gbc4df4bb6"
data_git_msg = """\
commit bc4df4bb63165bfd60c7037291e4e41d20c5d4bd
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Feb 3 16:36:03 2021 -0800

    [dv/chip] Update mem_bkdr_if in chip level TB
    
    This commit updates the usage of `mem_bkdr_if` throughout the chip level
    testbench.
    
    The OTP testbencch also has minor updates to enable ECC in the
    mem_bkdr_if.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
