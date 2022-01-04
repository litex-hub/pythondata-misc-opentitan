import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9317"
version_tuple = (0, 0, 9317)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9317")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9200"
data_version_tuple = (0, 0, 9200)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9200")
except ImportError:
    pass
data_git_hash = "4d0617cb43e9965eeffe3b603c0d0b42b128d6ef"
data_git_describe = "v0.0-9200-g4d0617cb4"
data_git_msg = """\
commit 4d0617cb43e9965eeffe3b603c0d0b42b128d6ef
Author: Michael Schaffner <msf@google.com>
Date:   Tue Jan 4 08:08:07 2022 -0800

    [rv_core_ibex] Minor fix in waiver comment
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
