import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14441"
version_tuple = (0, 0, 14441)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14441")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14299"
data_version_tuple = (0, 0, 14299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14299")
except ImportError:
    pass
data_git_hash = "6028b2035db694e9f77517dcd7e0dedaa632a7c5"
data_git_describe = "v0.0-14299-g6028b2035d"
data_git_msg = """\
commit 6028b2035db694e9f77517dcd7e0dedaa632a7c5
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Sep 23 15:02:06 2022 -0700

    [i2c] fix how sda_interference is detected.
    
    - fixes #15067
    - instead of checking the input value immediately after changing
      sda, we instead wait through the rise time and sychronization delays.
    - After waiting through that delay, if the input does not match the
      output, then assert sda interference.
    
    In the process of making this fix, the fsm was simplified a tiny bit
    on the host side.  The SetupBit states were removed since they do not
    serve any function.  There is no need for the host to wait until the
    setup window before driving its output.
    
    Additioanlly, minor fixes were made to the testbench to correct some
    of the ack and nak sampling behavior.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
