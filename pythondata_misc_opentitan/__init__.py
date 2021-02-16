import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5009"
version_tuple = (0, 0, 5009)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5009")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4918"
data_version_tuple = (0, 0, 4918)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4918")
except ImportError:
    pass
data_git_hash = "9d84982a28edbcadbb1f883f407863c18b2c6d86"
data_git_describe = "v0.0-4918-g9d84982a2"
data_git_msg = """\
commit 9d84982a28edbcadbb1f883f407863c18b2c6d86
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Tue Feb 16 14:25:01 2021 +0000

    [uart] Fix signal width
    
    Verilator lint correctly identifies the signal as one bit too short
    (should be 6, is 5).
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
