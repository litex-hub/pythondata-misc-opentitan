import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13307"
version_tuple = (0, 0, 13307)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13307")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13165"
data_version_tuple = (0, 0, 13165)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13165")
except ImportError:
    pass
data_git_hash = "09115123e5481699ef91c490e9206161290540cc"
data_git_describe = "v0.0-13165-g09115123e5"
data_git_msg = """\
commit 09115123e5481699ef91c490e9206161290540cc
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jul 18 12:09:56 2022 +0200

    [top] Daisy chaining of LC RMA req/ack interface for Flash and OTBN
    
    It has been decided that in addition to Flash also some non-reset
    registers inside OTBN should be securely wiped before LC can enter RMA.
    Since LC is already in D3, meaning we want to avoid changes to LC if
    possible, it has been decided to daisy chain the LC RMA req/ack
    interface. More precisely, LC will send the REQ to Flash as before,
    but Flash will send the ACK to the REQ input of OTBN, and OTBNs ACK is
    then connected to the LC ACK.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
