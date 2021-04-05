import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5712"
version_tuple = (0, 0, 5712)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5712")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5617"
data_version_tuple = (0, 0, 5617)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5617")
except ImportError:
    pass
data_git_hash = "a14b2ce07f0dec3bdd692e61671a4a6e417a5399"
data_git_describe = "v0.0-5617-ga14b2ce07"
data_git_msg = """\
commit a14b2ce07f0dec3bdd692e61671a4a6e417a5399
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Dec 9 08:50:51 2020 -0500

    Initial commit
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>
    
    [sw] Add dif_pwrmgr_smoktest
    
    - The test puts the device to sleep and immediately wakes up via usb
    - The usb wakeup is FAKE, the usb device is not actually enumerated.  Instead the usbdev presents to be in suspend to activate the wake logic, which is then used to trigger a wakeup.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dv] Convert existing dif_pwrmgr_smoketest into a dv only test
    
    - The test relies on specific dv behvaior that cannot always be replicated in other systems without intervention.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] update dif_pwrmgr_smoketest
    
    - use aon_timer for wakeup instead of usb
    - this should now be portable across all targets
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] Fix typo
    
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
