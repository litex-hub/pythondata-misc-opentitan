import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5884"
version_tuple = (0, 0, 5884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5789"
data_version_tuple = (0, 0, 5789)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5789")
except ImportError:
    pass
data_git_hash = "624ff14a9075db1cd1c9cfd7aac8569ef094ce67"
data_git_describe = "v0.0-5789-g624ff14a9"
data_git_msg = """\
commit 624ff14a9075db1cd1c9cfd7aac8569ef094ce67
Author: Rafal Kapuscik <rkapuscik@antmicro.com>
Date:   Wed Apr 7 09:37:51 2021 +0200

    Add formatting changes from allow list
    
    Signed-off-by: Rafal Kapuscik <rkapuscik@antmicro.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
