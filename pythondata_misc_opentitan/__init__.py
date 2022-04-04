import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11343"
version_tuple = (0, 0, 11343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11217"
data_version_tuple = (0, 0, 11217)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11217")
except ImportError:
    pass
data_git_hash = "35d9712caf174da4da19e737386f4239db7ccfdb"
data_git_describe = "v0.0-11217-g35d9712ca"
data_git_msg = """\
commit 35d9712caf174da4da19e737386f4239db7ccfdb
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Mon Apr 4 11:25:38 2022 -0400

    [ci] Inform the Bazel regression tests that some tests moved
    
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
