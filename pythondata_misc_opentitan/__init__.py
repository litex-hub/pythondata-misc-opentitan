import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13253"
version_tuple = (0, 0, 13253)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13253")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13111"
data_version_tuple = (0, 0, 13111)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13111")
except ImportError:
    pass
data_git_hash = "761a1390cb95473b68c0fb3a08c7a42877b90435"
data_git_describe = "v0.0-13111-g761a1390cb"
data_git_msg = """\
commit 761a1390cb95473b68c0fb3a08c7a42877b90435
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 9 08:11:27 2022 -0700

    [dv,chip_sw_clkmgr] Enhance peri_off test
    
    Make this test all four peripheral clock.
    Checks cpu_info dump last address matches expectations.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
