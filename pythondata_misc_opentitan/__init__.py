import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11180"
version_tuple = (0, 0, 11180)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11180")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11054"
data_version_tuple = (0, 0, 11054)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11054")
except ImportError:
    pass
data_git_hash = "91f2a7e5b815e33d9e048daf14c837ba5911eaef"
data_git_describe = "v0.0-11054-g91f2a7e5b"
data_git_msg = """\
commit 91f2a7e5b815e33d9e048daf14c837ba5911eaef
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Mar 24 15:07:19 2022 -0700

    [dv/jtag] Fix chip_level jtag csr rw failure
    
    This PR fixes the chip_level jtag csr_rw test failure by assigning a
    wrong default map to subblks.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
