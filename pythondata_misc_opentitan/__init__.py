import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9673"
version_tuple = (0, 0, 9673)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9673")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9551"
data_version_tuple = (0, 0, 9551)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9551")
except ImportError:
    pass
data_git_hash = "6f124bdf1273e671a272acc7fcf5a3091a05a3ef"
data_git_describe = "v0.0-9551-g6f124bdf1"
data_git_msg = """\
commit 6f124bdf1273e671a272acc7fcf5a3091a05a3ef
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Tue Jan 11 16:51:18 2022 +0000

    [sw,tests] Adding chip_sw_kmac_app_lc test
    
    Added entry to cross-reference with chip_sw_lc_ctrl_transition test.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
