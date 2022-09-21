import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14340"
version_tuple = (0, 0, 14340)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14340")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14198"
data_version_tuple = (0, 0, 14198)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14198")
except ImportError:
    pass
data_git_hash = "4358baf636fea6358e7ad8cbfeb060f94138473c"
data_git_describe = "v0.0-14198-g4358baf636"
data_git_msg = """\
commit 4358baf636fea6358e7ad8cbfeb060f94138473c
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Sep 20 15:00:27 2022 -0700

    refactor(chip): Convert MIO/DIO retention type to IOS type
    
    This commit adds `miodio_to_ios()` function. The function converts
    MIO/DIO specific retention type to ios_if map.
    
    With the conversion, the test code can have unified test regardless of
    MIO/DIO types.
    
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
