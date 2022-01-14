import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9530"
version_tuple = (0, 0, 9530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9408"
data_version_tuple = (0, 0, 9408)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9408")
except ImportError:
    pass
data_git_hash = "60c1f1277317ce3fa447d6955124d77a9b559fd4"
data_git_describe = "v0.0-9408-g60c1f1277"
data_git_msg = """\
commit 60c1f1277317ce3fa447d6955124d77a9b559fd4
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jan 13 20:29:42 2022 +0000

    [spi_device] Lint fix
    
    use constant 0 for lint tool to assume the correct bit size
    
    To avoid Out of Bound lint error, logic is changed to explicit
    assignment in jedec.sv
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
