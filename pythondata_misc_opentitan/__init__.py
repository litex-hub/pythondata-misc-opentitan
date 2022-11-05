import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15259"
version_tuple = (0, 0, 15259)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15259")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15117"
data_version_tuple = (0, 0, 15117)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15117")
except ImportError:
    pass
data_git_hash = "484e732d31951d1b1995a21e7e0db6aa382d2a56"
data_git_describe = "v0.0-15117-g484e732d31"
data_git_msg = """\
commit 484e732d31951d1b1995a21e7e0db6aa382d2a56
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Nov 4 16:38:30 2022 -0700

    [prim] Add an internal check flag
    
    - The check flag always disables upon reset.  When the
      first rising edge of the request is seen, it is then activated
      again until the next reset.  This ensures we check only during
      active periods and not accidentally across a reset, which is
      what caused the failure previously.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
