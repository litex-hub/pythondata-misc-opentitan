import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10653"
version_tuple = (0, 0, 10653)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10653")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10527"
data_version_tuple = (0, 0, 10527)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10527")
except ImportError:
    pass
data_git_hash = "9f60770816a837425c5cc3faf71d748ae7e7f3b9"
data_git_describe = "v0.0-10527-g9f6077081"
data_git_msg = """\
commit 9f60770816a837425c5cc3faf71d748ae7e7f3b9
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Tue Mar 1 10:58:05 2022 -0800

    [edn/dv] Allow/generate additional command data
    
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
