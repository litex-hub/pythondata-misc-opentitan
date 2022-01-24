import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9736"
version_tuple = (0, 0, 9736)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9736")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9614"
data_version_tuple = (0, 0, 9614)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9614")
except ImportError:
    pass
data_git_hash = "c98f979876e2946a3efeb1c816c68a77c3d7e643"
data_git_describe = "v0.0-9614-gc98f97987"
data_git_msg = """\
commit c98f979876e2946a3efeb1c816c68a77c3d7e643
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jan 21 09:55:22 2022 -0800

    [dv/pwrmgr] Disable escalation ping fcov
    
    This PR disable the fcov collected by escalation agent regarding the
    ping coverage. Because pwrmgr stimulus doesn't send out ping request.
    This feature is covered in alert_handler testbench.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
