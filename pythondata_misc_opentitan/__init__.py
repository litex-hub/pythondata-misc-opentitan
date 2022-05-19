import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12240"
version_tuple = (0, 0, 12240)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12240")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12112"
data_version_tuple = (0, 0, 12112)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12112")
except ImportError:
    pass
data_git_hash = "8472b339452fc9189faae736bfbfd5695eb3d8a8"
data_git_describe = "v0.0-12112-g8472b3394"
data_git_msg = """\
commit 8472b339452fc9189faae736bfbfd5695eb3d8a8
Author: Michael Schaffner <msf@google.com>
Date:   Wed May 18 10:53:10 2022 -0700

    [rv_core_ibex] align default config with config used in top
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
