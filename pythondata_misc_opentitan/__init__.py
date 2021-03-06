import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5266"
version_tuple = (0, 0, 5266)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5266")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5171"
data_version_tuple = (0, 0, 5171)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5171")
except ImportError:
    pass
data_git_hash = "12cce14e3355f5df1c1d2c533a9686b88cc84b93"
data_git_describe = "v0.0-5171-g12cce14e3"
data_git_msg = """\
commit 12cce14e3355f5df1c1d2c533a9686b88cc84b93
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 2 18:11:01 2021 -0800

    [tlul] Add memory transmission integrity checks
    
    - Add optional integrity generation / checks into tlul_adapter_sram
    - Update sram_scr to make use of the integrity error information
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Fix for englishbreakfast
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [all] update for intg_error_o port
    
    - Create alert from sram controllers
    - Unused for all other modules
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sram dv] Add extra alert
    
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
