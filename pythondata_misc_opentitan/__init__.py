import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5040"
version_tuple = (0, 0, 5040)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5040")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4949"
data_version_tuple = (0, 0, 4949)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4949")
except ImportError:
    pass
data_git_hash = "bc2bc5877fe0ed7fc2dfa09ff7db279546fb0cca"
data_git_describe = "v0.0-4949-gbc2bc5877"
data_git_msg = """\
commit bc2bc5877fe0ed7fc2dfa09ff7db279546fb0cca
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 9 13:30:37 2021 +0000

    [reggen] Define a Window type to represent (memory) windows
    
    This also removes the Window class from reggen/data.py: we'll use the
    new Window class everywhere.
    
    There's a bit of code to handle window tags at the bottom of
    uvm_reg.sv.tpl that goes away completely (windows don't have tags, so
    this was dead code).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
