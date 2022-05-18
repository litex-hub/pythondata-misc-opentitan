import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12227"
version_tuple = (0, 0, 12227)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12227")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12099"
data_version_tuple = (0, 0, 12099)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12099")
except ImportError:
    pass
data_git_hash = "f616ce61e7b9a432eeed648cf58973f58ca6e3d5"
data_git_describe = "v0.0-12099-gf616ce61e"
data_git_msg = """\
commit f616ce61e7b9a432eeed648cf58973f58ca6e3d5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed May 18 16:05:09 2022 +0100

    [otbn,dv] Correct the boundary of a "critical section"
    
    The running_ flag is used to handle process control in
    start_running_otbn. The idea is that it gets set when we start
    run_otbn() and then cleared just before we exit. That lets us get the
    timing right before running a "disable fork" in start_running_otbn.
    
    A series of commits starting with 1b1b7aa had added some extra stuff
    that run after we cleared the flag, causing occasional weird errors
    where a UVM sequencer spots that a process has been killed while
    waiting to send a sequence item.
    
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
