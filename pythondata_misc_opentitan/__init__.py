import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5486"
version_tuple = (0, 0, 5486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5391"
data_version_tuple = (0, 0, 5391)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5391")
except ImportError:
    pass
data_git_hash = "967319ded21fa93734dcc8a2756099dd370b8071"
data_git_describe = "v0.0-5391-g967319ded"
data_git_msg = """\
commit 967319ded21fa93734dcc8a2756099dd370b8071
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Mar 19 09:18:42 2021 +0000

    [aon_timer] Lint fixes
    
    Ascentlint doesn't pick up the unused_* bits from inside a struct and so
    is failing on the intr_state bits. This commit lists them out explicitly
    which will hopefully silence the warning.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
