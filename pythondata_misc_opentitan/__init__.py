import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5613"
version_tuple = (0, 0, 5613)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5613")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5518"
data_version_tuple = (0, 0, 5518)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5518")
except ImportError:
    pass
data_git_hash = "f0d5b0cfb27f804d41057dbbbfda276e21703430"
data_git_describe = "v0.0-5518-gf0d5b0cfb"
data_git_msg = """\
commit f0d5b0cfb27f804d41057dbbbfda276e21703430
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 26 11:48:42 2021 +0000

    [ci] Add a CI check to avoid committing executable .sv files
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
