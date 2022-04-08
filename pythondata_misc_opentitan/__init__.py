import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11492"
version_tuple = (0, 0, 11492)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11492")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11366"
data_version_tuple = (0, 0, 11366)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11366")
except ImportError:
    pass
data_git_hash = "88a4bcc87472a2e29d75faa2ee2756b6d5d19bec"
data_git_describe = "v0.0-11366-g88a4bcc87"
data_git_msg = """\
commit 88a4bcc87472a2e29d75faa2ee2756b6d5d19bec
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri Apr 8 10:21:39 2022 -0700

    [edn/dv] Implement my V2 Review TODO Items listed in Issue #11489
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
