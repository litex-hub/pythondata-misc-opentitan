import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10292"
version_tuple = (0, 0, 10292)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10292")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10166"
data_version_tuple = (0, 0, 10166)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10166")
except ImportError:
    pass
data_git_hash = "bc1f42e264cc1c2f203fc2b80d9253e7761f01a8"
data_git_describe = "v0.0-10166-gbc1f42e26"
data_git_msg = """\
commit bc1f42e264cc1c2f203fc2b80d9253e7761f01a8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 14 17:22:05 2022 +0000

    [tlul] Send blanking data unless we have rdata in tlul_adapter_sram
    
    This ensures that we respond with error_blanking_data rather than '0
    in the case of a TL read that fails its integrity check. The previous
    code didn't do that because vld_rd_rsp depends on rdata_i which, in
    turn, depends on req_o that we suppress when the transaction is
    ill-formed.
    
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
