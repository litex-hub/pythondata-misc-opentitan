import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5307"
version_tuple = (0, 0, 5307)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5307")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5212"
data_version_tuple = (0, 0, 5212)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5212")
except ImportError:
    pass
data_git_hash = "eb619e67ff2d81fd4c59c3647254e5dff10563ff"
data_git_describe = "v0.0-5212-geb619e67f"
data_git_msg = """\
commit eb619e67ff2d81fd4c59c3647254e5dff10563ff
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 5 15:01:54 2021 +0000

    [topgen] Don't copy data from block into instances
    
    There's no need to do this, as long as we can look up the block
    quickly. The nicest way to do that would be to add a "block" field to
    the instance dictionary, but that would be enormous when we dumped
    top_earlgrey.gen.hjson (I tried it - it added 32k lines!), so we just
    pass around a dictionary mapping block name to the IpBlock object
    instead.
    
    Note that we do still have to copy inter_signal_list, because that
    gets annotated (through references; it's not very easy to trace) by
    the code in intermodule.py.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
