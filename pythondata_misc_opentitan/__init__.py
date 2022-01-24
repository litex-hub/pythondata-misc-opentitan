import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9715"
version_tuple = (0, 0, 9715)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9715")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9593"
data_version_tuple = (0, 0, 9593)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9593")
except ImportError:
    pass
data_git_hash = "b603d64c392f0d844697690dd595fd56ae77d677"
data_git_describe = "v0.0-9593-gb603d64c3"
data_git_msg = """\
commit b603d64c392f0d844697690dd595fd56ae77d677
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jan 19 17:24:31 2022 -0800

    [pwrmgr, rstmgr] D2S preparation
    
    - convert to new sparse fsms
    - add addidiontal sparse fsms to reset
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
