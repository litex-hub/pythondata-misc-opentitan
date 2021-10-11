import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8211"
version_tuple = (0, 0, 8211)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8211")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8099"
data_version_tuple = (0, 0, 8099)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8099")
except ImportError:
    pass
data_git_hash = "32c28ca951013f2e866f444f771316ead4249a76"
data_git_describe = "v0.0-8099-g32c28ca95"
data_git_msg = """\
commit 32c28ca951013f2e866f444f771316ead4249a76
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Oct 8 14:50:09 2021 -0700

    [reggen] Add mubi support into hjson
    
    - This primarily ensures reset values are consistent
    - Fixes #8521
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [reggen] Report error when bit fields are re-used
    
    - Fixes #7566
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    Update used bits check
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [reggen] Relocate mubi script
    
    - Add to `util/design` area so that it can be directly referenced
      by fields.py
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    address comments
    
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
