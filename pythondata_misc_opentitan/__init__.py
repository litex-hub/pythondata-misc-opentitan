import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5627"
version_tuple = (0, 0, 5627)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5627")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5532"
data_version_tuple = (0, 0, 5532)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5532")
except ImportError:
    pass
data_git_hash = "5ae27ddee53838fef73512ea3cee1f4170e5312f"
data_git_describe = "v0.0-5532-g5ae27ddee"
data_git_msg = """\
commit 5ae27ddee53838fef73512ea3cee1f4170e5312f
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 29 22:49:59 2021 +0100

    [otbn] Pedantic style fix
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
