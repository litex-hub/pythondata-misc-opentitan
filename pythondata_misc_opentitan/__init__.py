import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10674"
version_tuple = (0, 0, 10674)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10674")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10548"
data_version_tuple = (0, 0, 10548)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10548")
except ImportError:
    pass
data_git_hash = "7f5aca5cc0b0a08d69e242661a8afd320a184e94"
data_git_describe = "v0.0-10548-g7f5aca5cc"
data_git_msg = """\
commit 7f5aca5cc0b0a08d69e242661a8afd320a184e94
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 2 17:23:14 2022 -0800

    [rv_dm dv] Add rv_dm SBA access test
    
    This commit updates the RV DM env and adds the SBA access test.
    There is no checking at the moment- the checks will be implemented
    in the scoreboard, which will be updated in the next PR.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
