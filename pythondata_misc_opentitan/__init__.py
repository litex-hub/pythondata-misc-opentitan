import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14718"
version_tuple = (0, 0, 14718)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14718")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14576"
data_version_tuple = (0, 0, 14576)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14576")
except ImportError:
    pass
data_git_hash = "dd3d4e46aa33d10ca2d89312345d158fe1a0c6fa"
data_git_describe = "v0.0-14576-gdd3d4e46aa"
data_git_msg = """\
commit dd3d4e46aa33d10ca2d89312345d158fe1a0c6fa
Author: Eli Kim <eli@opentitan.org>
Date:   Wed Oct 12 09:45:33 2022 -0700

    refactor(spid): Change `tpm_header_not_empty` to level
    
    _Related Issue: https://github.com/lowRISC/opentitan/issues/15282_
    
    The current interrupt scheme assumes the input is an event (pulse). If
    the input is a status, it was recommented to add an edge detector to
    create a pulse.
    
    In certain cases, this may create unwanted (phantom) interrupts or
    missing interrupts depending on the SW approach to handling the
    interrupts.
    
    To remove the race condition, HW now connects the status signal to the
    interrupt in this commit. With the change, now SW is responsible to mask
    the interrupt while the SW queues the interrupt to event queues.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
