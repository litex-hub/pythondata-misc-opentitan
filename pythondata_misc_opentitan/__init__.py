import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14385"
version_tuple = (0, 0, 14385)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14385")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14243"
data_version_tuple = (0, 0, 14243)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14243")
except ImportError:
    pass
data_git_hash = "c1308a72923b6262af7ff96697c1c5ec2bbe24d9"
data_git_describe = "v0.0-14243-gc1308a7292"
data_git_msg = """\
commit c1308a72923b6262af7ff96697c1c5ec2bbe24d9
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Sep 22 11:41:31 2022 -0400

    [util] Print stderr if generate_compilation_db.py fails
    
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
