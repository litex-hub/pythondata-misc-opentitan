import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14525"
version_tuple = (0, 0, 14525)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14525")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14383"
data_version_tuple = (0, 0, 14383)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14383")
except ImportError:
    pass
data_git_hash = "5fb5570a8d5d1673b72ec02d6a795f0e480d1444"
data_git_describe = "v0.0-14383-g5fb5570a8d"
data_git_msg = """\
commit 5fb5570a8d5d1673b72ec02d6a795f0e480d1444
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Fri Sep 30 12:02:16 2022 +0100

    Revert "[rv_core_ibex] Add SVA to check PC is not advancing"
    
    This reverts commit c43e2906516442dec36022f101e109c050d2dd69.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
