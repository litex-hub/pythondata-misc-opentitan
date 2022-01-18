import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9601"
version_tuple = (0, 0, 9601)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9601")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9479"
data_version_tuple = (0, 0, 9479)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9479")
except ImportError:
    pass
data_git_hash = "d3975c6cff90e0764dd1e5f30022eac674699597"
data_git_describe = "v0.0-9479-gd3975c6cf"
data_git_msg = """\
commit d3975c6cff90e0764dd1e5f30022eac674699597
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 18 18:00:53 2022 +0000

    [otbn,dv] Add a stress_all_with_rand_reset test
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
