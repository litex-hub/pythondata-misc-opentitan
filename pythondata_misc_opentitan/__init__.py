import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10785"
version_tuple = (0, 0, 10785)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10785")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10659"
data_version_tuple = (0, 0, 10659)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10659")
except ImportError:
    pass
data_git_hash = "f17bca818ba15f769ec1b8f4d398bdae69f6e052"
data_git_describe = "v0.0-10659-gf17bca818"
data_git_msg = """\
commit f17bca818ba15f769ec1b8f4d398bdae69f6e052
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Mar 8 11:12:41 2022 -0800

    [bazel] Fix scrambled flash VMEM file name
    
    This removes an additional "." that was included in the file extension
    of scrambled flash VMEM files by accident.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
