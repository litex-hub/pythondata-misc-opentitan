import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5041"
version_tuple = (0, 0, 5041)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5041")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4950"
data_version_tuple = (0, 0, 4950)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4950")
except ImportError:
    pass
data_git_hash = "588819ef9a4df185741ae2b59a830d20c9a494ae"
data_git_describe = "v0.0-4950-g588819ef9"
data_git_msg = """\
commit 588819ef9a4df185741ae2b59a830d20c9a494ae
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 10 16:27:53 2021 +0000

    [regtool] Remove support for alternate-style headers
    
    This is unused, and seems not to have been used since the start of
    development history.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
