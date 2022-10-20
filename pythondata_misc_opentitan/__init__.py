import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14856"
version_tuple = (0, 0, 14856)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14856")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14714"
data_version_tuple = (0, 0, 14714)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14714")
except ImportError:
    pass
data_git_hash = "be7318d6859548c47238b89a3920c73da316abf7"
data_git_describe = "v0.0-14714-gbe7318d685"
data_git_msg = """\
commit be7318d6859548c47238b89a3920c73da316abf7
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 19 14:56:06 2022 -0400

    [test] Set pmpaddr0 to match the entire address space
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
