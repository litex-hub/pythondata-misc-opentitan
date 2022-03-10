import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10821"
version_tuple = (0, 0, 10821)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10821")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10695"
data_version_tuple = (0, 0, 10695)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10695")
except ImportError:
    pass
data_git_hash = "f999d5515d774136880a666677f370f694c0e801"
data_git_describe = "v0.0-10695-gf999d5515"
data_git_msg = """\
commit f999d5515d774136880a666677f370f694c0e801
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Thu Mar 10 10:34:05 2022 +0000

    [util] Allow specifying hjson file in current directory
    
    Specifying a hjson in the current directory
    (e.g. ../../../../util/regtool.py uart.hjson) causes a pathlib error
    because parents[1] doesn't exist.
    
    Signed-off-by: Olof Kindgren <olof.kindgren@gmail.com>

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
