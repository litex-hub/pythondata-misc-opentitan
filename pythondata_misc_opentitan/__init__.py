import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5296"
version_tuple = (0, 0, 5296)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5296")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5201"
data_version_tuple = (0, 0, 5201)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5201")
except ImportError:
    pass
data_git_hash = "915df6982ec6094bd351fa9db15ee9d22a2c1cd7"
data_git_describe = "v0.0-5201-g915df6982"
data_git_msg = """\
commit 915df6982ec6094bd351fa9db15ee9d22a2c1cd7
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 5 13:16:36 2021 -0800

    [tlul] Enable tlul integrity check across the design
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [tlul] Minor enhancements
    
    - remove commented out code after placing tlul_host_adapter inside lc_ctrl
    - add full width parameters to tlul_pkg.sv
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dv] Minor hacks to get tlul integrity checks going
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [tlul] correct comment typo
    
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
