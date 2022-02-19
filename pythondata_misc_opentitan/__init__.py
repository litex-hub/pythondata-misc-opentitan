import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10453"
version_tuple = (0, 0, 10453)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10453")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10327"
data_version_tuple = (0, 0, 10327)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10327")
except ImportError:
    pass
data_git_hash = "93d120cbfd7207b75010cefa9ac61f9a717631b9"
data_git_describe = "v0.0-10327-g93d120cbf"
data_git_msg = """\
commit 93d120cbfd7207b75010cefa9ac61f9a717631b9
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Feb 18 08:50:16 2022 -0800

    [edn/rtl/doc] Update doc and debug state machine reg
    
    Some edn register cleanup, along with adding the
    complete main state machine to be read-only.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
