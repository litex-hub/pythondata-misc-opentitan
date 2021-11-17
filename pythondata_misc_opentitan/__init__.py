import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8751"
version_tuple = (0, 0, 8751)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8751")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8639"
data_version_tuple = (0, 0, 8639)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8639")
except ImportError:
    pass
data_git_hash = "0beb25531c1bbf75a269608f225c4c4a49b3caf8"
data_git_describe = "v0.0-8639-g0beb25531"
data_git_msg = """\
commit 0beb25531c1bbf75a269608f225c4c4a49b3caf8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Nov 16 20:22:35 2021 +0000

    [otbn,rtl] Weaken assertion about imem_addr_o
    
    The core can sometimes send X on this signal, but it doesn't matter
    because imem_req_o is false.
    
    To see this happen, run:
    
        util/dvsim/dvsim.py hw/ip/otbn/dv/uvm/otbn_sim_cfg.hjson \
            -i otbn_multi_err --fixed-seed 3982135834
    
    this is running the "jalr-0" test, which does a
    
        jalr x0, x1, 0
    
    with an empty callstack. I think the X's in the uninitialised call
    stack are appearing as the next address to load. Of course, this
    doesn't matter because we're also spotting the error and squashing the
    request.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
