import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12274"
version_tuple = (0, 0, 12274)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12274")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12146"
data_version_tuple = (0, 0, 12146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12146")
except ImportError:
    pass
data_git_hash = "95efd6759381928720a568858f6ce20c12921d9a"
data_git_describe = "v0.0-12146-g95efd6759"
data_git_msg = """\
commit 95efd6759381928720a568858f6ce20c12921d9a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Apr 12 17:30:05 2022 +0100

    Tweak vendoring json; Update lowrisc_ibex to lowRISC/ibex@e1128aa2
    
    Now we explicitly pull in the stuff we need, rather than excluding the
    things we don't want.
    
    Once that was done, I re-ran the vendor tool (fetching the same
    version of the Ibex repository). The rest of this commit message is
    the auto-generated commit message from the tool.
    
    Update code from upstream repository
    https://github.com/lowRISC/ibex.git to revision
    e1128aa2d442efb7cbdd93f98708dfa0b875e7e1
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
