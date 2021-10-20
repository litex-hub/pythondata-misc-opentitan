import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8347"
version_tuple = (0, 0, 8347)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8347")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8235"
data_version_tuple = (0, 0, 8235)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8235")
except ImportError:
    pass
data_git_hash = "0604a5dd0aea440737605f24fa89093bcc410900"
data_git_describe = "v0.0-8235-g0604a5dd0"
data_git_msg = """\
commit 0604a5dd0aea440737605f24fa89093bcc410900
Author: Timothy Trippel <ttrippel@google.com>
Date:   Sat Oct 16 00:25:58 2021 +0000

    [dif] Prepare templates for rv_timer modifications.
    
    To adapt the templates to auto-generate the RV timer IRQ DIFs, the
    template functions must be adapted to be more generic (in terms of
    passing in the register offset macro/variable with the address).
    Additionally, the "params_list" from the RV timer's HJSON will need to
    be parsed, to exract the number of HARTs/timers, so that capability is
    added to the make_new_dif.py tool.
    
    This partially addresses #8142.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
