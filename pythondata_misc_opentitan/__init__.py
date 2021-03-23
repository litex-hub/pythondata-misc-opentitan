import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5521"
version_tuple = (0, 0, 5521)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5521")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5426"
data_version_tuple = (0, 0, 5426)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5426")
except ImportError:
    pass
data_git_hash = "3cba4f8e67af5280b89353b458fd76013cbd424a"
data_git_describe = "v0.0-5426-g3cba4f8e6"
data_git_msg = """\
commit 3cba4f8e67af5280b89353b458fd76013cbd424a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 19 17:06:54 2021 +0000

    [prim] Split out PRESENT and PRINCE support from prim:all
    
    Also move a waiver that applies to prim:cipher_pkg to the right
    package (it was still in prim.waiver, which is only included by
    prim:all).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
