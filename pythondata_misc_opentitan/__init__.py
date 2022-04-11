import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11502"
version_tuple = (0, 0, 11502)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11502")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11376"
data_version_tuple = (0, 0, 11376)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11376")
except ImportError:
    pass
data_git_hash = "c83256698562dd4d5ab0fa24e69759139f79b49b"
data_git_describe = "v0.0-11376-gc83256698"
data_git_msg = """\
commit c83256698562dd4d5ab0fa24e69759139f79b49b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 8 12:20:56 2022 +0100

    [reggen] Move shadow register error aggregation into reg_top
    
    This was duplicated in all of the different IPs that used shadow
    registers and it's not particularly difficult to just put the giant
    ORs in reg_top instead. Do so.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
