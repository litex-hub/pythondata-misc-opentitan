import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8740"
version_tuple = (0, 0, 8740)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8740")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8628"
data_version_tuple = (0, 0, 8628)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8628")
except ImportError:
    pass
data_git_hash = "c366ef897e9b66e01d166e7f0743173981b9e565"
data_git_describe = "v0.0-8628-gc366ef897"
data_git_msg = """\
commit c366ef897e9b66e01d166e7f0743173981b9e565
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Oct 25 14:39:48 2021 +0200

    [aes/lint] Waive Verilator lint warnings related to split_var
    
    Verilator 4.210 - 4.214 erroneously generates some UNOPTFLAT warnings
    despite split_var. This will most likely be resolved in Verilator 4.215.
    
    See also Verilator/Verilator#3177.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
