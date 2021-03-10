import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5329"
version_tuple = (0, 0, 5329)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5329")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5234"
data_version_tuple = (0, 0, 5234)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5234")
except ImportError:
    pass
data_git_hash = "d20804dfa0f1699919dd8c189561a9ec9078d697"
data_git_describe = "v0.0-5234-gd20804dfa"
data_git_msg = """\
commit d20804dfa0f1699919dd8c189561a9ec9078d697
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 10 15:15:31 2021 +0000

    [rstmgr] Remove duplicated parameters from rstmgr_ctrl
    
    These are also defined in rstmgr_pkg.sv with the same values, causing
    a namespace clash. I think we probably just forgot to remove them from
    rstmgr_ctrl.sv when we added them to the package.
    
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
