import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5566"
version_tuple = (0, 0, 5566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5471"
data_version_tuple = (0, 0, 5471)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5471")
except ImportError:
    pass
data_git_hash = "7444b1113cd3177570dc4efccf70abc2bdc5c919"
data_git_describe = "v0.0-5471-g7444b1113"
data_git_msg = """\
commit 7444b1113cd3177570dc4efccf70abc2bdc5c919
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Mar 24 18:26:35 2021 +0000

    [ast] Remove whitespace in core file
    
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
