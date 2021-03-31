import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5651"
version_tuple = (0, 0, 5651)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5651")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5556"
data_version_tuple = (0, 0, 5556)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5556")
except ImportError:
    pass
data_git_hash = "0e71a67020285dda3a24a9fce6c5ca38d0025f9e"
data_git_describe = "v0.0-5556-g0e71a6702"
data_git_msg = """\
commit 0e71a67020285dda3a24a9fce6c5ca38d0025f9e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 31 10:46:42 2021 +0100

    [topgen] Impose an ordering on blocks in top_uvm_reg.sv.tpl
    
    Tracing things back through topgen.py, the insertion order of
    top.blocks depends on the order that the glob returns filenames in
    search_ips (in lib.py). This isn't guaranteed to be stable across
    machines and the whole thing feels a bit delicate either way.
    
    This commit uses the blocks in alphabetical order. Another option
    would be to order by the base address of the first instance: maybe a
    bit nicer, but more work so I've gone with the easy solution first.
    
    To check this works on a single machine, add the line
    
        ips.reverse()
    
    just after the definition of ips in search_ips (in lib.py). The
    generate results before and after the addition, diffing the two
    
        mkdir -p X
        util/topgen.py -t hw/top_earlgrey/data/top_earlgrey.hjson -r -o X
    
    With this patch, nothing changes.
    
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
