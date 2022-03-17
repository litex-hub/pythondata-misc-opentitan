import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10963"
version_tuple = (0, 0, 10963)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10963")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10837"
data_version_tuple = (0, 0, 10837)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10837")
except ImportError:
    pass
data_git_hash = "e5928dfec8723c6be150342a18b80c72b1c4659f"
data_git_describe = "v0.0-10837-ge5928dfec"
data_git_msg = """\
commit e5928dfec8723c6be150342a18b80c72b1c4659f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 10 15:01:51 2022 +0000

    [otbn,dv] Clear the "imem is invalidated" flag when loading program
    
    This hasn't usually mattered because we reset the dut (and also the
    ISS) after injecting IMEM errors to clear the locked state. However,
    there was a race window where we injected the errors just after OTBN
    had finished. In this case, we don't need to reset the DUT, but we do
    have to clear the flag when the IMEM contents are replaced.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
