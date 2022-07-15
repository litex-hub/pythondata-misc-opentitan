import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13117"
version_tuple = (0, 0, 13117)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13117")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12975"
data_version_tuple = (0, 0, 12975)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12975")
except ImportError:
    pass
data_git_hash = "77d9624db87f02ba7b9d4e78d18d29b2b377c230"
data_git_describe = "v0.0-12975-g77d9624db8"
data_git_msg = """\
commit 77d9624db87f02ba7b9d4e78d18d29b2b377c230
Author: Drew Macrae <drewmacrae@google.com>
Date:   Tue Jul 12 09:58:52 2022 -0400

    [english_breakfast] fake relevant drivers for test_rom reset reasons
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
