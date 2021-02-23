import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5121"
version_tuple = (0, 0, 5121)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5121")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5030"
data_version_tuple = (0, 0, 5030)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5030")
except ImportError:
    pass
data_git_hash = "c40f2db4b87ad811e4b50b1c3825c744df9c6838"
data_git_describe = "v0.0-5030-gc40f2db4b"
data_git_msg = """\
commit c40f2db4b87ad811e4b50b1c3825c744df9c6838
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 22 08:37:37 2021 +0000

    [prim_packer] Silence verilator width warnings
    
    There are two changes here. The first is to explicitly zero-extend
    wdata_i from InW up to OutW when computing wdata_shifted in pack mode.
    The second is to slice out just the bits we need from MaxW / MinW when
    comparing depth_q against it (otherwise Verilator complains that we're
    comparing a small bitvector against a 32-bit int).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
