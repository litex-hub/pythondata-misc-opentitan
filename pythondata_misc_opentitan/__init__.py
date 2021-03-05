import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5254"
version_tuple = (0, 0, 5254)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5254")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5163"
data_version_tuple = (0, 0, 5163)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5163")
except ImportError:
    pass
data_git_hash = "c88e97fe0634880a8e617a8594e1a3e883394569"
data_git_describe = "v0.0-5163-gc88e97fe0"
data_git_msg = """\
commit c88e97fe0634880a8e617a8594e1a3e883394569
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Mar 4 13:38:20 2021 +0000

    [ibex] Connect up crash dump output
    
    Fixes #4618
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
