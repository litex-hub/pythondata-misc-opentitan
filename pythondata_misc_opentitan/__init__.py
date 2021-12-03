import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8990"
version_tuple = (0, 0, 8990)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8990")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8878"
data_version_tuple = (0, 0, 8878)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8878")
except ImportError:
    pass
data_git_hash = "d9d2faa7b33f8bb45931778792d930b13f421f9d"
data_git_describe = "v0.0-8878-gd9d2faa7b"
data_git_msg = """\
commit d9d2faa7b33f8bb45931778792d930b13f421f9d
Author: Michael Schaffner <msf@google.com>
Date:   Wed Nov 3 13:18:04 2021 -0700

    [syn/cdc] Tune SDC file to fix all SDC warnings/errors in CDC
    
    This introduces some more flexibility to the SDC file so that we can
    reuse it for open-source-only CDC runs where the hookup paths have
    different hierarchical names.
    
    Also, there are a few constraints that CDC does not understand, and we
    introduce a variable to exclude them conditionally for CDC flows.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
