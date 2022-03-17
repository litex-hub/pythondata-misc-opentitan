import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10951"
version_tuple = (0, 0, 10951)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10951")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10825"
data_version_tuple = (0, 0, 10825)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10825")
except ImportError:
    pass
data_git_hash = "c4e9f84094831bae578803be809a827667f28c80"
data_git_describe = "v0.0-10825-gc4e9f8409"
data_git_msg = """\
commit c4e9f84094831bae578803be809a827667f28c80
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Mar 9 15:33:12 2022 +0000

    [rv_core_ibex] Move to D2S and bump version to 1.0
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
