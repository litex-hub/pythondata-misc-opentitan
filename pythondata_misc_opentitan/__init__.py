import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14975"
version_tuple = (0, 0, 14975)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14975")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14833"
data_version_tuple = (0, 0, 14833)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14833")
except ImportError:
    pass
data_git_hash = "faafbabd0dfbda4291eaf3c52d5b752e7c8d7805"
data_git_describe = "v0.0-14833-gfaafbabd0d"
data_git_msg = """\
commit faafbabd0dfbda4291eaf3c52d5b752e7c8d7805
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Oct 25 12:28:20 2022 -0700

    [rdc] Waive TPM CSb -> FIFO.wvalid
    
    RDC tool detecs the metastability issue when TPM CSb is de-asserted
    (0->1). However, in that case in normal scenario, SCK is quiescent.
    
    Only case this matters is that the CSb un-intentionally violates the
    assumption. In that case, unexpected commnand or write data may be
    pushed to the FIFOs.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
