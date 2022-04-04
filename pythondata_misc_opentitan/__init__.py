import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11328"
version_tuple = (0, 0, 11328)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11328")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11202"
data_version_tuple = (0, 0, 11202)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11202")
except ImportError:
    pass
data_git_hash = "55db958b26235dd786d231a79c060a5d5d47358d"
data_git_describe = "v0.0-11202-g55db958b2"
data_git_msg = """\
commit 55db958b26235dd786d231a79c060a5d5d47358d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 4 13:11:50 2022 +0100

    [dvsim,xcelium] Fix sed commands to generate plusargs
    
    I really messed up 0dc541c. I think that I'd checked the code with .*
    and a non-empty string, then noticed that it also matched empty
    strings. So I changed to .+, but forgot to check that .+ worked with
    non-empty strings. It turns out that "+" for "one or more occurrences"
    is only supported by sed with -E.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
