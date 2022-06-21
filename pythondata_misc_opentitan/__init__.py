import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12755"
version_tuple = (0, 0, 12755)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12755")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12613"
data_version_tuple = (0, 0, 12613)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12613")
except ImportError:
    pass
data_git_hash = "58d38c160e6de7fabd5cfdfe7ebd253611d497cd"
data_git_describe = "v0.0-12613-g58d38c160e"
data_git_msg = """\
commit 58d38c160e6de7fabd5cfdfe7ebd253611d497cd
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Thu Jun 16 07:50:33 2022 +0200

    [otbn,sw] Use app symbols for parameter addresses
    
    `otbn_smoketest` runs the `barrett384` OTBN application.  Before and
    after OTBN execution, data is copied to and from OTBN data memory,
    respectively.  Prior to this commit, `otbn_smoketest` had hard-coded
    offsets for the input and output data.  Instead of hard-coded offsets,
    the OTBN DIF can extract the address of a symbol in data memory from an
    OTBN object file.  This commit replaces the hard-coded offsets with
    symbol-derived addresses.
    
    The instruction count of `barrett384` increases by 10:  Before running
    the actual algorithm, OTBN now loads four operands from symbol-defined
    addresses instead of a hard-coded offset.  This code uses one `la` per
    operand, which is a pseudo-instruction implemented as two real
    instructions.  After running the algorithm, OTBN now stores one operand
    using the same method.  That sums up to 8 additional instructions for
    loading and 2 additional instructions for storing.  For repeated
    invocations of `barrett384`, the code could be optimized so that the
    additional instructions don't reduce the overall performance.
    
    Co-authored-by: Jade Philipoom <jadep@google.com>
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
