import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9355"
version_tuple = (0, 0, 9355)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9355")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9238"
data_version_tuple = (0, 0, 9238)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9238")
except ImportError:
    pass
data_git_hash = "cb56b467022a58683cdbf5589cc7a8a7c15944a6"
data_git_describe = "v0.0-9238-gcb56b4670"
data_git_msg = """\
commit cb56b467022a58683cdbf5589cc7a8a7c15944a6
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Jan 4 19:00:40 2022 +0100

    [prim_xilinx] Replace KEEP with DONT_TOUCH attributes
    
    Previously, we have been using KEEP attributes to prevent synthesis
    optimizations across these primitives to ensure that FI and SCA
    countermeasures are not optimized away. However, according to the
    Vivado Design Suite User Guide: Synthesis (UG901), the KEEP attribute
    is commonly used in conjunction with timing constraints but
    doesn't force place and route to keep the signal. Instead, the
    DONT_TOUCH attribute is recommended for this purpose (see Chapter 2):
    
    "Unlike KEEP and KEEP_HIERARCHY, DONT_TOUCH is forward-annotated to
    place and route to prevent logic optimization."
    
    In addition, the KEEP/DONT_TOUCH attributes are not supported on ports
    of modules and instead should be applied to the module itself.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
