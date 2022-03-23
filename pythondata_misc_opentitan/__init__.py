import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11044"
version_tuple = (0, 0, 11044)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11044")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10918"
data_version_tuple = (0, 0, 10918)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10918")
except ImportError:
    pass
data_git_hash = "c3628a53481278bc63e60f40f35e580bc291900e"
data_git_describe = "v0.0-10918-gc3628a534"
data_git_msg = """\
commit c3628a53481278bc63e60f40f35e580bc291900e
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Mar 23 14:40:46 2022 -0400

    [bazel] Unbreak building //sw/device/tests:all
    
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
