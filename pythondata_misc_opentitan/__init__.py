import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12626"
version_tuple = (0, 0, 12626)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12626")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12484"
data_version_tuple = (0, 0, 12484)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12484")
except ImportError:
    pass
data_git_hash = "a772b85ca276e9ba67ddd7fefae1656169ec8d33"
data_git_describe = "v0.0-12484-ga772b85ca"
data_git_msg = """\
commit a772b85ca276e9ba67ddd7fefae1656169ec8d33
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Jun 3 10:16:36 2022 -0700

    [flash/tlul] Enhance tlul_lc_gate to handle outstanding
    
    - enhance tlul_lc_gate to better handle outstanding transactions
    - when lc_en drops when there are outstanding trasnactions, any
      further commands are blocked but existing trasnactions are allowed
      to complete. Then the tlul_lc_gate transitions to an error state
      where all future commands are directly err'd.
    
    - Also adjust existing instantiations in otp_ctrl and rv_dm
    
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
