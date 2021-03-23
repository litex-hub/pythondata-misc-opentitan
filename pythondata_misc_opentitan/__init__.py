import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5532"
version_tuple = (0, 0, 5532)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5532")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5437"
data_version_tuple = (0, 0, 5437)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5437")
except ImportError:
    pass
data_git_hash = "04b1c25924dfc22247a80f44a98577e95c54f994"
data_git_describe = "v0.0-5437-g04b1c2592"
data_git_msg = """\
commit 04b1c25924dfc22247a80f44a98577e95c54f994
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 18 12:22:34 2021 +0000

    [otbn] Use DpiMemutil / MemArea to access memory for otbn_model.cc
    
    This removes the duplicated calls to simutil_get_mem and
    simutil_set_mem. It also avoids duplicating the SV paths to the guts
    of the memories: they were in otbn_memutil.cc and otbn.sv and
    otbn_top_sim.sv; now they're just in otbn_memutil.cc.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
