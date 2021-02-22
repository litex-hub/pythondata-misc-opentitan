import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5095"
version_tuple = (0, 0, 5095)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5095")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5004"
data_version_tuple = (0, 0, 5004)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5004")
except ImportError:
    pass
data_git_hash = "254cf26b9f1b782fe58addb9084a638fc09d9bb2"
data_git_describe = "v0.0-5004-g254cf26b9"
data_git_msg = """\
commit 254cf26b9f1b782fe58addb9084a638fc09d9bb2
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Feb 19 16:18:50 2021 +0000

    [otbn] Rewrite CSR reads and writes in operation docs
    
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
