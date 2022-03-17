import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10937"
version_tuple = (0, 0, 10937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10811"
data_version_tuple = (0, 0, 10811)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10811")
except ImportError:
    pass
data_git_hash = "be2a187152275c826463744b4fa8691c79b865e2"
data_git_describe = "v0.0-10811-gbe2a18715"
data_git_msg = """\
commit be2a187152275c826463744b4fa8691c79b865e2
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 16 23:04:43 2022 +0000

    [chip,dv] Remove chip_sw_rom_ctrl_reset_glitch from testplan
    
    This test is to verify functionality that we never got around to
    adding to KMAC and has been ICEBOXed.
    
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
