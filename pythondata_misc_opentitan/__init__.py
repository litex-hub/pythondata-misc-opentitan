import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9431"
version_tuple = (0, 0, 9431)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9431")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9313"
data_version_tuple = (0, 0, 9313)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9313")
except ImportError:
    pass
data_git_hash = "56ab31bb62792dd25cbf61da91c215bdf1f51d38"
data_git_describe = "v0.0-9313-g56ab31bb6"
data_git_msg = """\
commit 56ab31bb62792dd25cbf61da91c215bdf1f51d38
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Wed Dec 22 12:57:06 2021 -0800

    [spi_host/dv] adding framework for the coverage model
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
