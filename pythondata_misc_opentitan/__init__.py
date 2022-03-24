import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11091"
version_tuple = (0, 0, 11091)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11091")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10965"
data_version_tuple = (0, 0, 10965)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10965")
except ImportError:
    pass
data_git_hash = "8fce79d5d833689d9c2aa996a2c9a3976c656200"
data_git_describe = "v0.0-10965-g8fce79d5d"
data_git_msg = """\
commit 8fce79d5d833689d9c2aa996a2c9a3976c656200
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Mar 23 15:37:39 2022 -0400

    [bazel] Format all BUILD files in the repo
    
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
