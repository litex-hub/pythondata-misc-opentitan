import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12586"
version_tuple = (0, 0, 12586)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12586")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12444"
data_version_tuple = (0, 0, 12444)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12444")
except ImportError:
    pass
data_git_hash = "b2dc980f7cc37d4f5391c1158a7ac80285251944"
data_git_describe = "v0.0-12444-gb2dc980f7"
data_git_msg = """\
commit b2dc980f7cc37d4f5391c1158a7ac80285251944
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Sun Jun 5 22:49:02 2022 +0100

    [doc] Add Nir Tasher to the technical committee
    
    Nir has been appointed to the technical committee by the steering
    committee. Welcome Nir!
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
