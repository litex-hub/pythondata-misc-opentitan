import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14959"
version_tuple = (0, 0, 14959)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14959")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14817"
data_version_tuple = (0, 0, 14817)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14817")
except ImportError:
    pass
data_git_hash = "8c40959740be6f198278f772638433a105652fda"
data_git_describe = "v0.0-14817-g8c40959740"
data_git_msg = """\
commit 8c40959740be6f198278f772638433a105652fda
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Oct 25 13:48:12 2022 -0700

    [dv/edn] Minor regression fix
    
    This PR fixes two minor issues in EDN regression:
    1). Add `alert_test` as a valid csr in scb
    2). Add functional coverage for interrupts in edn
    
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
