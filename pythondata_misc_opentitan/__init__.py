import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12434"
version_tuple = (0, 0, 12434)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12434")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12292"
data_version_tuple = (0, 0, 12292)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12292")
except ImportError:
    pass
data_git_hash = "cf8ea0c9502802b974c65c9f7a87e4d694ca2c74"
data_git_describe = "v0.0-12292-gcf8ea0c95"
data_git_msg = """\
commit cf8ea0c9502802b974c65c9f7a87e4d694ca2c74
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue May 31 17:27:41 2022 -0400

    [sw/silicon_creator] Minor updates to shutdown_unittest.cc
    
    The only remaining mock in shutdown_unittest.cc mocks the internal
    functions of the shutdown module and thus it's appropriate to keep its
    definition there.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
