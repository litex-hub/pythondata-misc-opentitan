import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12918"
version_tuple = (0, 0, 12918)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12918")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12776"
data_version_tuple = (0, 0, 12776)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12776")
except ImportError:
    pass
data_git_hash = "dd256fe3b7d5aed44574baf3b10278ef741fdc54"
data_git_describe = "v0.0-12776-gdd256fe3b7"
data_git_msg = """\
commit dd256fe3b7d5aed44574baf3b10278ef741fdc54
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Jul 1 08:18:59 2022 -0700

    [doc] Update top earlgrey block diagram
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
