import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8608"
version_tuple = (0, 0, 8608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8496"
data_version_tuple = (0, 0, 8496)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8496")
except ImportError:
    pass
data_git_hash = "3d156ce35e0ba559b5246c96286c0568cfa559c0"
data_git_describe = "v0.0-8496-g3d156ce35"
data_git_msg = """\
commit 3d156ce35e0ba559b5246c96286c0568cfa559c0
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Nov 3 03:11:04 2021 +0000

    [doc] Update DIF dev and style guide.
    
    After auto-generating a portion of the DIFs, as described in #8142, this
    commit cleans up the DIF developement and style guide on the website to
    match what is now implemented.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
