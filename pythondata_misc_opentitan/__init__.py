import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10644"
version_tuple = (0, 0, 10644)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10644")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10518"
data_version_tuple = (0, 0, 10518)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10518")
except ImportError:
    pass
data_git_hash = "b04083ba8b2b5c671f962654b02457ca2dbe936a"
data_git_describe = "v0.0-10518-gb04083ba8"
data_git_msg = """\
commit b04083ba8b2b5c671f962654b02457ca2dbe936a
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Feb 21 17:08:54 2022 +0000

    [rv_core_ibex, rtl] Add local escalation path to disable fetch
    
    When a major core error is seen the local escalation path immediately
    shuts down fetch enable in addition to raising a fatal alert.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
