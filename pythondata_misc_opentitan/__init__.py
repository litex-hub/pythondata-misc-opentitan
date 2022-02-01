import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9964"
version_tuple = (0, 0, 9964)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9964")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9840"
data_version_tuple = (0, 0, 9840)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9840")
except ImportError:
    pass
data_git_hash = "315e2f1b3fd1ff35061021e40c8eddc12c443c9b"
data_git_describe = "v0.0-9840-g315e2f1b3"
data_git_msg = """\
commit 315e2f1b3fd1ff35061021e40c8eddc12c443c9b
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jan 31 14:45:27 2022 -0800

    [lc_ctrl] Beef up internal usage of redundant CSR encoding
    
    The replicated enum encoding of the LC_STATE and TRANSITION_TARGET CSRs
    has been added in order to ease hardening on the firmware side.
    
    This patch lists this as an explicit countermeasure, and beefs up the
    internal usage of this encoding. I.e., the transition logic only checked
    the TRANSITION_TARGET encoding coming from the CSRs before. With this
    change, the logic now also makes use of the redundancy present in the
    decoded state vector. This is useful in particular when indexing the
    transition matrix LUT (to get the valid bits and token indices), since
    this indexing operation can now be duplicated.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
