import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8722"
version_tuple = (0, 0, 8722)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8722")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8610"
data_version_tuple = (0, 0, 8610)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8610")
except ImportError:
    pass
data_git_hash = "3ab2d2557de984053698378b50e753d9f39d015f"
data_git_describe = "v0.0-8610-g3ab2d2557"
data_git_msg = """\
commit 3ab2d2557de984053698378b50e753d9f39d015f
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Nov 15 16:56:06 2021 +0000

    [doc] Update OTBN style guide.
    
    Add some advice on inline data, and update the variable-time example to
    show good practice with regard to the OTBN loop stack.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
