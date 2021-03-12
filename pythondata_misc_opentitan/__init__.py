import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5358"
version_tuple = (0, 0, 5358)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5358")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5263"
data_version_tuple = (0, 0, 5263)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5263")
except ImportError:
    pass
data_git_hash = "11017d6bb5b510fbdd8d6c91dcb1260ee38d0fe1"
data_git_describe = "v0.0-5263-g11017d6bb"
data_git_msg = """\
commit 11017d6bb5b510fbdd8d6c91dcb1260ee38d0fe1
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 10 15:07:53 2021 -0800

    [dcd] add auto generated tb
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dcd] update fifo depth
    
    pending #5028
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dv] add dcd csr tests to smoke regression
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dcd] updates to address comments
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dcd] Add doc placeholder
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
