import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10742"
version_tuple = (0, 0, 10742)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10742")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10616"
data_version_tuple = (0, 0, 10616)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10616")
except ImportError:
    pass
data_git_hash = "2b37bc7b9c0a3574ac71bdb3b0afe27425a629e9"
data_git_describe = "v0.0-10616-g2b37bc7b9"
data_git_msg = """\
commit 2b37bc7b9c0a3574ac71bdb3b0afe27425a629e9
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Mar 4 17:27:08 2022 -0800

    [dif/pwm] Make X macro names consistent across DIF libs
    
    This commit aims to make then names of X macros (used for code gen)
    consistent across DIF libraries. X macros simplify maintenance of DIF
    libraries that rely on a specific number of resources (e.g., pins,
    channels, alerts, etc.) to be available in the HW.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
