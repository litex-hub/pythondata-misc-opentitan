import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11167"
version_tuple = (0, 0, 11167)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11167")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11041"
data_version_tuple = (0, 0, 11041)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11041")
except ImportError:
    pass
data_git_hash = "39fea81ce959d724a01e14593ec17cc6891acedf"
data_git_describe = "v0.0-11041-g39fea81ce"
data_git_msg = """\
commit 39fea81ce959d724a01e14593ec17cc6891acedf
Author: Miles Dai <milesdai@google.com>
Date:   Fri Mar 25 15:37:26 2022 -0400

    [doc] Add information about downloading pre-built bitstreams
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
