import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10320"
version_tuple = (0, 0, 10320)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10320")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10194"
data_version_tuple = (0, 0, 10194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10194")
except ImportError:
    pass
data_git_hash = "b29822d679fd46c2652a534f25934d3b7d075201"
data_git_describe = "v0.0-10194-gb29822d67"
data_git_msg = """\
commit b29822d679fd46c2652a534f25934d3b7d075201
Author: Weicai Yang <weicai@google.com>
Date:   Mon Feb 14 23:02:15 2022 -0800

    [sram/dv] Minor update for lc_esc
    
    Update sequence to use random value to enable lc_esc, rather than always
    use `On`.
    Also  update scb to treat other values as `On`
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
