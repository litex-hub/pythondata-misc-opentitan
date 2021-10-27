import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8475"
version_tuple = (0, 0, 8475)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8475")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8363"
data_version_tuple = (0, 0, 8363)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8363")
except ImportError:
    pass
data_git_hash = "b51084435ad3a7de7a7719899172ec597d130698"
data_git_describe = "v0.0-8363-gb51084435"
data_git_msg = """\
commit b51084435ad3a7de7a7719899172ec597d130698
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Oct 21 17:47:33 2021 +0100

    [otbn, dv] Generate instructions with bad CSR / WSR addresses.
    
    Following additions/ modifications are done in this commit:
    1.bad_ispr.py: A new snippet generator that picks up instructions only
    related to CSR/ WSR registers and replaces the good register address
    with bad address.
    2.known_mem.py: A method called pick_bad_addr is added to pick an
    address from the gaps in known memory.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
