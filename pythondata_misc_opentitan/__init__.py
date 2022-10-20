import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14854"
version_tuple = (0, 0, 14854)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14854")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14712"
data_version_tuple = (0, 0, 14712)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14712")
except ImportError:
    pass
data_git_hash = "9644452702ff6cb6eadaa7110a2952ab0d25aab9"
data_git_describe = "v0.0-14712-g9644452702"
data_git_msg = """\
commit 9644452702ff6cb6eadaa7110a2952ab0d25aab9
Author: Dan McArdle <dmcardle@google.com>
Date:   Tue Oct 18 17:30:39 2022 -0400

    [bazel] Add manual tag to //hw:verilator_real
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
