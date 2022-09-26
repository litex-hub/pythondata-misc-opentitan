import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14439"
version_tuple = (0, 0, 14439)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14439")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14297"
data_version_tuple = (0, 0, 14297)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14297")
except ImportError:
    pass
data_git_hash = "c43e2906516442dec36022f101e109c050d2dd69"
data_git_describe = "v0.0-14297-gc43e290651"
data_git_msg = """\
commit c43e2906516442dec36022f101e109c050d2dd69
Author: Michael Schaffner <msf@google.com>
Date:   Fri Sep 23 15:34:53 2022 +0200

    [rv_core_ibex] Add SVA to check PC is not advancing
    
    The PC must not advance if the CPU is not enabled.
    Addresses part of #11208.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
