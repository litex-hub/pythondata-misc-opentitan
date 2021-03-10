import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5318"
version_tuple = (0, 0, 5318)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5318")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5223"
data_version_tuple = (0, 0, 5223)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5223")
except ImportError:
    pass
data_git_hash = "7247d8aa62c7fa1878cf91c7bc8a1b2b8dd3fc9e"
data_git_describe = "v0.0-5223-g7247d8aa6"
data_git_msg = """\
commit 7247d8aa62c7fa1878cf91c7bc8a1b2b8dd3fc9e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 5 18:07:38 2021 +0000

    [otbn] Fix read/write enables in tracer
    
    * `insn_valid` must be factored in with the read enable for the bignum
      register file as it uses the raw decoder signal.
    * `rf_base_wr_commit` must be combined with the write enable for the
      base register file to determine if the write occurred.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
