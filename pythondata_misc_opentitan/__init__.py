import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8761"
version_tuple = (0, 0, 8761)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8761")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8649"
data_version_tuple = (0, 0, 8649)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8649")
except ImportError:
    pass
data_git_hash = "085cef5b6b2b7dc2044cb4679623999871d561c3"
data_git_describe = "v0.0-8649-g085cef5b6"
data_git_msg = """\
commit 085cef5b6b2b7dc2044cb4679623999871d561c3
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Nov 17 17:24:09 2021 +0000

    [prim] Fix prim_packer_fifo when ClearOnRead is false
    
    When we take the first part of an output word, we need to zero the
    existing contents.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
