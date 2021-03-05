import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5252"
version_tuple = (0, 0, 5252)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5252")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5161"
data_version_tuple = (0, 0, 5161)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5161")
except ImportError:
    pass
data_git_hash = "dadebce3951540a3624ce936d79f06b46691e68d"
data_git_describe = "v0.0-5161-gdadebce39"
data_git_msg = """\
commit dadebce3951540a3624ce936d79f06b46691e68d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 4 15:55:22 2021 +0000

    [otbn] Fix bad_insn_addr ERR_BITS description
    
    Write to IMEM cannot occur from OTBN, so bad_insn_addr will only be
    signalled on IMEM reads from OTBN.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
