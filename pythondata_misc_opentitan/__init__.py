import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9532"
version_tuple = (0, 0, 9532)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9532")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9410"
data_version_tuple = (0, 0, 9410)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9410")
except ImportError:
    pass
data_git_hash = "f3ce1a11d87b9a040d0ca556bacba68eec9980c6"
data_git_describe = "v0.0-9410-gf3ce1a11d"
data_git_msg = """\
commit f3ce1a11d87b9a040d0ca556bacba68eec9980c6
Author: Jacob Levy <jacob.levy@opentitan.org>
Date:   Wed Jan 12 19:26:07 2022 +0200

    [AST] Add 2 DFT padmux2ast (remove 2 analog DFT inputs) and solve AST Lint/Synth OSCs issue
    
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

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
