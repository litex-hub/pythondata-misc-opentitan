import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12454"
version_tuple = (0, 0, 12454)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12454")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12312"
data_version_tuple = (0, 0, 12312)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12312")
except ImportError:
    pass
data_git_hash = "780e05e7b64764ae36a5421eae5c418c5fe84565"
data_git_describe = "v0.0-12312-g780e05e7b"
data_git_msg = """\
commit 780e05e7b64764ae36a5421eae5c418c5fe84565
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jun 1 15:06:02 2022 -0400

    [sw/silicon_creator] Remove fake_deps.c
    
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
