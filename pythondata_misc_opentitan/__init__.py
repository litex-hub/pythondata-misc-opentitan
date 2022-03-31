import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11232"
version_tuple = (0, 0, 11232)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11232")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11106"
data_version_tuple = (0, 0, 11106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11106")
except ImportError:
    pass
data_git_hash = "ce1e77f88498dd4c0c128cb069cc1317e382245e"
data_git_describe = "v0.0-11106-gce1e77f88"
data_git_msg = """\
commit ce1e77f88498dd4c0c128cb069cc1317e382245e
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Mar 30 10:15:26 2022 -0700

    [rv_dm] Use instantiate dv_dm directly to deduplicate code
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
