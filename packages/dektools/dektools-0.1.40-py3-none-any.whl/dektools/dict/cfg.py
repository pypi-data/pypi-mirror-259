from dynaconf import Dynaconf
from dynaconf.utils.boxing import Box
from .simple import assign, is_dict


class AssignCfg:
    def __init__(self, prefix, *objects):
        self.prefix = prefix
        self.objects = objects
        self.object_cls = objects[0].__class__

    def generate(self):
        def walk(d, s):
            for k, v in d.items():
                vv = getattr(s, k, empty)
                if isinstance(vv, Box):
                    if is_dict(v):
                        walk(v, vv)
                    else:
                        x = self.object_cls()
                        x.update(vv)
                        d[k] = x
                elif vv is not empty:
                    d[k] = vv

        empty = object()
        settings = Dynaconf(
            envvar_prefix=self.prefix
        )
        data = assign(*self.objects, cls=self.object_cls)
        walk(data, settings)
        return data
