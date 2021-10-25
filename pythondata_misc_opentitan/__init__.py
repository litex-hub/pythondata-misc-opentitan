import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8418"
version_tuple = (0, 0, 8418)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8418")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8306"
data_version_tuple = (0, 0, 8306)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8306")
except ImportError:
    pass
data_git_hash = "b19dec1b90e724341fbd24f2646d96d1e968407f"
data_git_describe = "v0.0-8306-gb19dec1b9"
data_git_msg = """\
commit b19dec1b90e724341fbd24f2646d96d1e968407f
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Oct 22 16:16:37 2021 +0200

    [aes/pre_syn] Re-enable Yosys synthesis
    
    This commit causes `prim_sec_anchor_*` primitives to be replaced by
    the corresponding Xilinx primitives before calling Yosys.
    
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
