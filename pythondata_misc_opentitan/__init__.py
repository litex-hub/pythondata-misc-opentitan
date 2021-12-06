import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9007"
version_tuple = (0, 0, 9007)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9007")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8895"
data_version_tuple = (0, 0, 8895)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8895")
except ImportError:
    pass
data_git_hash = "09912c369722c240313288cbb8fff07be237652b"
data_git_describe = "v0.0-8895-g09912c369"
data_git_msg = """\
commit 09912c369722c240313288cbb8fff07be237652b
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Nov 16 22:14:19 2021 +0100

    [es/csrng/edn] Don't clear packer FIFOs upon read
    
    Previously, all packer FIFOs in the entropy complex where by default
    cleared to zero upon read. However, as this may simplify attacks trying
    to manipulate the random number distribution it should better be
    avoided. Leaving around the previous random data on the bus/wires after
    the read is preferred over outputting a deterministic value in this
    case.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
