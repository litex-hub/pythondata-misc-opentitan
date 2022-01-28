import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9887"
version_tuple = (0, 0, 9887)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9887")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9763"
data_version_tuple = (0, 0, 9763)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9763")
except ImportError:
    pass
data_git_hash = "ef5bc57ef8f9c06db162afd4fe79129b3eefae4f"
data_git_describe = "v0.0-9763-gef5bc57ef"
data_git_msg = """\
commit ef5bc57ef8f9c06db162afd4fe79129b3eefae4f
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Jan 28 11:38:29 2022 -0800

    [dv/mubi] Fix randomization
    
    This changes the distributions for mubi values to be more uniform.
    The true and false values weights are scaled to the others become
    uniform.
    
    The distributions for 400000 values of mubi4 with weights
    False=4, True=2, Others=2 become more uniform: a measurement gives
    
    mubi 00000000 count 0.017827
    mubi 00000001 count 0.017930
    mubi 00000002 count 0.017708
    mubi 00000003 count 0.017695
    mubi 00000004 count 0.017825
    mubi 00000005 count 0.499032
    mubi 00000006 count 0.017642
    mubi 00000007 count 0.018132
    mubi 00000008 count 0.017825
    mubi 00000009 count 0.017962
    mubi 0000000a count 0.250962
    mubi 0000000b count 0.018163
    mubi 0000000c count 0.018027
    mubi 0000000d count 0.017687
    mubi 0000000e count 0.017718
    mubi 0000000f count 0.017862
    
    The previous code's measurement is shown in the linked issue.
    
    Fixes #10257
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
