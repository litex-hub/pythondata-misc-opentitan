import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5250"
version_tuple = (0, 0, 5250)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5250")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5159"
data_version_tuple = (0, 0, 5159)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5159")
except ImportError:
    pass
data_git_hash = "9393230584258360dacbbc1550d99aaacff24cf1"
data_git_describe = "v0.0-5159-g939323058"
data_git_msg = """\
commit 9393230584258360dacbbc1550d99aaacff24cf1
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Mar 4 11:40:36 2021 -0800

    [dv/sram] minor updates to sram tb
    
    this PR fixes a few unaligned statements and some minor style fixes
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
