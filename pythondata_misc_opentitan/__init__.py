import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10216"
version_tuple = (0, 0, 10216)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10216")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10092"
data_version_tuple = (0, 0, 10092)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10092")
except ImportError:
    pass
data_git_hash = "610b263796030b80a8ee1f218127deedbe22dc33"
data_git_describe = "v0.0-10092-g610b26379"
data_git_msg = """\
commit 610b263796030b80a8ee1f218127deedbe22dc33
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Feb 8 23:36:02 2022 -0800

    [sw/ottf] move OTTF to flash address space
    
    To demonstrate the flash translation capabilities of the Ibex core
    wrapper, the OTTF was loaded at the virtual flash address space and the
    Ibex wrapper IP's address translation features were used to map the
    virtual flash address space to the physical address space.
    
    Unfortunately, in order to run OTTF-launched tests with mask ROM (vs
    test ROM), the OTTF manifest and entry point must be in the ROM_EXT slot
    a (or b, though we load (currently) load slot a only for simplicity)
    address space, wich is the beginning of the physical flash address space.
    
    If the mask ROM evolves to make use of these translation features, then
    the OTTF and test ROM can be updated to follow suit. This is captured in
    issue #10712.
    
    This partially addresses a task in #10498.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
