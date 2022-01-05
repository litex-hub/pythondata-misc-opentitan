import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9332"
version_tuple = (0, 0, 9332)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9332")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9215"
data_version_tuple = (0, 0, 9215)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9215")
except ImportError:
    pass
data_git_hash = "37ec7a232eff9fc95fdbf5eabe1975e14a5dd318"
data_git_describe = "v0.0-9215-g37ec7a232"
data_git_msg = """\
commit 37ec7a232eff9fc95fdbf5eabe1975e14a5dd318
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 4 13:58:55 2022 -0800

    [dv/uart] Fix typo in scoreboard
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
