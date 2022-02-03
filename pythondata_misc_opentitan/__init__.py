import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10034"
version_tuple = (0, 0, 10034)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10034")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9910"
data_version_tuple = (0, 0, 9910)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9910")
except ImportError:
    pass
data_git_hash = "c9552e7c9e4ef4bca4ac468ca01902a0b4b17da5"
data_git_describe = "v0.0-9910-gc9552e7c9"
data_git_msg = """\
commit c9552e7c9e4ef4bca4ac468ca01902a0b4b17da5
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 1 13:21:40 2022 +0100

    [aes] Fix VCS warning
    
    VCS erroneously thinks below statement would result in an out-of-bounds
    index:
    
      for (genvar i = 0; i < 4; i++) begin : gen_out
        assign out[i] = (i == 0) ? {in[3],   in1[i]} :
                                   {in[i-1], in1[i]};
      end
    
    To avoid this, this commit introduces a function to compute the index
    rotation and avoid the ternary expression.
    
    This resolves lowRISC/OpenTitan#10379.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
