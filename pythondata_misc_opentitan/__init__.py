import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15169"
version_tuple = (0, 0, 15169)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15169")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15027"
data_version_tuple = (0, 0, 15027)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15027")
except ImportError:
    pass
data_git_hash = "2161715b558cb25b4c38e3fa0a282f602b9c2d8f"
data_git_describe = "v0.0-15027-g2161715b55"
data_git_msg = """\
commit 2161715b558cb25b4c38e3fa0a282f602b9c2d8f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Nov 2 15:39:55 2022 -0700

    [dv/edn] Add csr_rd for locked regs
    
    This PR adds a csr_rd after locking the locked register so we can
    collect coverage for the auto-generate regwen.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
