import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8786"
version_tuple = (0, 0, 8786)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8786")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8674"
data_version_tuple = (0, 0, 8674)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8674")
except ImportError:
    pass
data_git_hash = "a5e3223e85d4715ab7949c069f9eab2c414ef53e"
data_git_describe = "v0.0-8674-ga5e3223e8"
data_git_msg = """\
commit a5e3223e85d4715ab7949c069f9eab2c414ef53e
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Nov 11 15:16:36 2021 -0800

    [mubi] Enhance mubi_sync with stability check
    
    - Stability check is not needed for most of the design and defaults
      to 0.
    
    - With stability enabled, a 3rd stage is compared to the sychronized
      output.  If the output is the same, the 3rd stage results are used,
      if not, the ResetValue is used.
    
    - This addresses some of the concerns raised with the original mubi_sync
      in #8848.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
