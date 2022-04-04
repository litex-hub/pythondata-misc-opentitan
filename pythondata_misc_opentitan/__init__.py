import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11358"
version_tuple = (0, 0, 11358)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11358")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11232"
data_version_tuple = (0, 0, 11232)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11232")
except ImportError:
    pass
data_git_hash = "4fe6a21f63992ad13dcdbad4fffa99a8ae8e280a"
data_git_describe = "v0.0-11232-g4fe6a21f6"
data_git_msg = """\
commit 4fe6a21f63992ad13dcdbad4fffa99a8ae8e280a
Author: Alexander Williams <awill@google.com>
Date:   Fri Apr 1 10:58:43 2022 -0700

    [pinmux] Promote pad attribute comment to fields
    
    This enables software to have hjson-linked macros for accessing the
    fields.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
