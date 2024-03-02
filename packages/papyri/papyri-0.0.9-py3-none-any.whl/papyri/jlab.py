import sys

from IPython.core.magic import Magics, line_magic, magics_class
from IPython.display import IFrame
import IPython


# The class MUST call this class decorator at creation time
@magics_class
class Papyri(Magics):
    def newhelp(self, obj):
        mod = obj.__module__
        root = mod.split(".")[0]
        fq = mod + "." + obj.__name__

        version = sys.modules[root].__version__
        return IFrame(
            f"http://127.0.0.1:1234/p/{root}/{version}/api/{fq}", "100%", "100%"
        )

    @line_magic
    def papyri(self, line):
        path0, *path = line.strip().split(".")
        obj = self.shell.user_ns[path0]
        for p in path:
            obj = getattr(obj, p)
        return self.newhelp(obj)


ip = IPython.get_ipython()
if ip:
    ip.register_magics(Papyri)
