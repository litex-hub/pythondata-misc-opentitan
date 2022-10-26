import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14950"
version_tuple = (0, 0, 14950)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14950")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14808"
data_version_tuple = (0, 0, 14808)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14808")
except ImportError:
    pass
data_git_hash = "0573dd72b4b63bd528c52a489bf8fc24b097b486"
data_git_describe = "v0.0-14808-g0573dd72b4"
data_git_msg = """\
commit 0573dd72b4b63bd528c52a489bf8fc24b097b486
Author: Alexander Williams <awill@google.com>
Date:   Mon Oct 24 08:39:47 2022 -0700

    [spi_host] Adjust passthrough not-X assertions
    
    The assertions for the passthrough-related I/Os were overzealous and did
    not account for conditions where X is allowable. Adjust them to focus on
    SCK and CSB only and have the SCK assertion activate only when CSB is
    asserted.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
