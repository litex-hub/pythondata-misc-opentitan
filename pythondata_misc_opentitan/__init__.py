import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14771"
version_tuple = (0, 0, 14771)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14771")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14629"
data_version_tuple = (0, 0, 14629)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14629")
except ImportError:
    pass
data_git_hash = "d214b80d1936f0ff0f702dc527131d68973db6cb"
data_git_describe = "v0.0-14629-gd214b80d19"
data_git_msg = """\
commit d214b80d1936f0ff0f702dc527131d68973db6cb
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Wed Oct 5 15:49:03 2022 +0100

    [dv, e2e] Add bootstrap_watchdog_disable test
    
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
