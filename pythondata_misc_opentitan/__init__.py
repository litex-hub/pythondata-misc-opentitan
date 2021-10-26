import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8456"
version_tuple = (0, 0, 8456)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8456")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8344"
data_version_tuple = (0, 0, 8344)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8344")
except ImportError:
    pass
data_git_hash = "d8ba072b3f239cb505c07cb058b97120d26d473f"
data_git_describe = "v0.0-8344-gd8ba072b3"
data_git_msg = """\
commit d8ba072b3f239cb505c07cb058b97120d26d473f
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Oct 25 17:58:44 2021 +0100

    [verible] Rename rule file
    
    Upstream suggests naming rule files with a suffix `.rules.verible_lint`.
    We didn't follow this rule so far, but named both waivers and rule files
    with the (custom) extension `.vbl`. Follow upstream naming to simplify
    some tooling.
    
    Fixes #8850
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
