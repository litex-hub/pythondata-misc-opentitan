import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14363"
version_tuple = (0, 0, 14363)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14363")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14221"
data_version_tuple = (0, 0, 14221)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14221")
except ImportError:
    pass
data_git_hash = "a18d6f6810beb8c7db850ad186ab9ed5f06c3f0f"
data_git_describe = "v0.0-14221-ga18d6f6810"
data_git_msg = """\
commit a18d6f6810beb8c7db850ad186ab9ed5f06c3f0f
Author: Eli Kim <eli@opentitan.org>
Date:   Wed Sep 21 09:39:30 2022 -0700

    test(chip): Add chip_sw_sleep_pin_mio_dio_val to testplan
    
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
