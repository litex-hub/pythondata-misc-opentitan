import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14559"
version_tuple = (0, 0, 14559)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14559")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14417"
data_version_tuple = (0, 0, 14417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14417")
except ImportError:
    pass
data_git_hash = "926c1605b5135f247f28c51fa708fec6ad9be5b1"
data_git_describe = "v0.0-14417-g926c1605b5"
data_git_msg = """\
commit 926c1605b5135f247f28c51fa708fec6ad9be5b1
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Oct 4 16:24:07 2022 -0700

    fix(spid): Revise invalid_locality desc
    
    Intention of HW is to upload TPM commands even if it points to invalid
    locality.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
