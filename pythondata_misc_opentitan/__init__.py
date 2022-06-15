import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12690"
version_tuple = (0, 0, 12690)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12690")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12548"
data_version_tuple = (0, 0, 12548)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12548")
except ImportError:
    pass
data_git_hash = "43b77237219b2c3ccaae7a516d227c7624a02adb"
data_git_describe = "v0.0-12548-g43b772372"
data_git_msg = """\
commit 43b77237219b2c3ccaae7a516d227c7624a02adb
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Tue Jun 14 11:13:46 2022 +0100

    [sw,tests] Add -f option to copy in sim.mk
    
    Fixes write permission errors in top level test builds.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
