import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12404"
version_tuple = (0, 0, 12404)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12404")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12264"
data_version_tuple = (0, 0, 12264)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12264")
except ImportError:
    pass
data_git_hash = "306c584d0fc0fa1a10e21c6a88753602420ada5b"
data_git_describe = "v0.0-12264-g306c584d0"
data_git_msg = """\
commit 306c584d0fc0fa1a10e21c6a88753602420ada5b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Sat May 28 22:24:34 2022 +0100

    [otbn,rtl] Drop pending RND prefetch at end of operation
    
    Consider a situation where we have two operations, A and B, that run
    back-to-back. Suppose operation A writes to RND_PREFETCH and then
    finishes before the EDN replies. Now suppose that operation B also
    writes to RND_PREFETCH. In this case, the RTL uses a signal called
    rnd_req_queued_q to track the fact that it should send out another RND
    request once the first (ignored) one comes back. But what if operation
    B also finishes before the EDN has replied to the first request?
    
    Once the result comes in, there was a slight mismatch between how the
    ISS and RTL handled things (depending on the timing of the *next*
    operation, the ISS might or might not have sent out another request).
    But this whole situation is silly! We know we don't care about the
    result of the second prefetch, so we don't need to do it at all.
    
    This patch tweaks the RTL to drop the pending request in this
    situation and adds a "forget" function in the ISS to do the same.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
