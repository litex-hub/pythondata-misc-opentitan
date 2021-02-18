import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5035"
version_tuple = (0, 0, 5035)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5035")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4944"
data_version_tuple = (0, 0, 4944)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4944")
except ImportError:
    pass
data_git_hash = "2b8ef7625242cd4d1f3bc6eb5294037d94192057"
data_git_describe = "v0.0-4944-g2b8ef7625"
data_git_msg = """\
commit 2b8ef7625242cd4d1f3bc6eb5294037d94192057
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 16 14:44:55 2021 -0800

    [aon_timer] Minor fixes and updates for integration
    
    - Add exclusions to clk_aon registers
    - Slightly rename reset request for consistency with wakeup request
    - Add dummy INTR_ENABLE register for #5260
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Integrate aon_timer and remove nmi_gen
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] update total interrupts
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
