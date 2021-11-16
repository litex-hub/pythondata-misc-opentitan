import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8741"
version_tuple = (0, 0, 8741)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8741")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8629"
data_version_tuple = (0, 0, 8629)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8629")
except ImportError:
    pass
data_git_hash = "859d51788975ee7c166b17539562803ab4dd375b"
data_git_describe = "v0.0-8629-g859d51788"
data_git_msg = """\
commit 859d51788975ee7c166b17539562803ab4dd375b
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Oct 26 14:27:48 2021 +0200

    [prim] Add option to not clear the packer FIFO upon read
    
    There are cases where leaving around the data just read doesn't hurt but
    instead outputting a deterministic value after read should be avoided.
    For example, if the packer FIFO is used to feed pseudo-random data into
    an LFSR, having the packer output such a deterministic value most of the
    time is bad as it may simplify an attack trying to load the LFSR with
    deterministic instead of random values.
    
    For this reason, this commit adds a new parameter to the packer FIFO
    primitive to control this behavior on a per-case basis and disables the
    clearing when used to feed LFSRs or inside prim_edn_req.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
