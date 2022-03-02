import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10651"
version_tuple = (0, 0, 10651)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10651")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10525"
data_version_tuple = (0, 0, 10525)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10525")
except ImportError:
    pass
data_git_hash = "285c5f2df0e0d6c635483d11285df55eae30f9f2"
data_git_describe = "v0.0-10525-g285c5f2df"
data_git_msg = """\
commit 285c5f2df0e0d6c635483d11285df55eae30f9f2
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 2 11:19:19 2022 +0000

    [otbn,dv] Use always (not always_ff) for a block in otbn_core_model
    
    Xcelium correctly complains about using an always_ff here: we also
    initialise model_state in an (implicit) inital block, which isn't
    allowed by always_ff (a construct that's really designed for
    synthesizable code).
    
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
