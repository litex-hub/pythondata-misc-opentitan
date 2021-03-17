import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5424"
version_tuple = (0, 0, 5424)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5424")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5329"
data_version_tuple = (0, 0, 5329)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5329")
except ImportError:
    pass
data_git_hash = "998b3fabcfbf56ec093d6c13a145e245f19aba52"
data_git_describe = "v0.0-5329-g998b3fabc"
data_git_msg = """\
commit 998b3fabcfbf56ec093d6c13a145e245f19aba52
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Tue Mar 16 21:55:25 2021 +0000

    [rv_plic] Clean up core files
    
    * Only depend primitives which we actually need.
    * Depend on the tlul code (which is used in the SV files produced by
      reggen) in the core which actually includes the relevant source files.
    * Improve the description of core files a bit.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
