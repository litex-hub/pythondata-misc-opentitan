import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11178"
version_tuple = (0, 0, 11178)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11178")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11052"
data_version_tuple = (0, 0, 11052)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11052")
except ImportError:
    pass
data_git_hash = "7d6a1355a0a38701e13740492f6ec45466ee5620"
data_git_describe = "v0.0-11052-g7d6a1355a"
data_git_msg = """\
commit 7d6a1355a0a38701e13740492f6ec45466ee5620
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Mon Mar 28 12:57:10 2022 -0400

    [vendor] Remove unused vendored BUILD file for FreeRTOS
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
