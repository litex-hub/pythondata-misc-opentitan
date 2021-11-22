import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8805"
version_tuple = (0, 0, 8805)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8805")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8693"
data_version_tuple = (0, 0, 8693)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8693")
except ImportError:
    pass
data_git_hash = "cc80879227cf914cb313599c380916113f812bfa"
data_git_describe = "v0.0-8693-gcc8087922"
data_git_msg = """\
commit cc80879227cf914cb313599c380916113f812bfa
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Nov 19 13:28:49 2021 +0000

    [sw/otbn] Move crypto assembly files into new folder.
    
    OTBN crypto assembly files are a bit of a different category than the
    other small example programs in code-snippets; move these to their own,
    new folder under sw/otbn/crypto.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
