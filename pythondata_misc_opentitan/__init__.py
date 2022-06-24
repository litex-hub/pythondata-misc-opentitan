import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12834"
version_tuple = (0, 0, 12834)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12834")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12692"
data_version_tuple = (0, 0, 12692)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12692")
except ImportError:
    pass
data_git_hash = "36a3fa830eccc4d4ec2daecad62cf8d0954538c2"
data_git_describe = "v0.0-12692-g36a3fa830e"
data_git_msg = """\
commit 36a3fa830eccc4d4ec2daecad62cf8d0954538c2
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Sat Jun 4 23:38:33 2022 +0000

    [top,dv,rv_dm] ndm reset request test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>
    
    ndm reset with dif patch

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
