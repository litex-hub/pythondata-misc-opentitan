import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8766"
version_tuple = (0, 0, 8766)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8766")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8654"
data_version_tuple = (0, 0, 8654)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8654")
except ImportError:
    pass
data_git_hash = "fa484ab1a2ab9a7e9818c96cf01b9929e64cc5fd"
data_git_describe = "v0.0-8654-gfa484ab1a"
data_git_msg = """\
commit fa484ab1a2ab9a7e9818c96cf01b9929e64cc5fd
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Nov 17 13:27:24 2021 -0800

    [dv/alert_esc_agent] support lpg in alert_esc_agent
    
    This PR supports lpg in alert_esc_agent. In alert_handler testbench, if
    lpg is enabled and alert triggered from the alert sender side,
    alert_handler testbench needs to ignore the alert.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
