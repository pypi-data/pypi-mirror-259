from wagtail import hooks

class DefaultToObject(dict):
    def set(self, key, value, *args, **kwargs):
        self[key] = value

    def set_many(self, objects: dict=None, *args, **kwargs):
        if objects is None:
            objects = {}
        self.update(objects)

    def get(self, key, *args, **kwargs):
        if key in self:
            return self[key]
        if "default" in kwargs:
            return kwargs["default"]
        return None
    
    def get_many(self, keys: list[str]=None, *args, **kwargs):
        if keys is None:
            keys = []
        return {key: self.get(key, *args, **kwargs) for key in keys}

    def delete(self, key, *args, **kwargs):
        del self[key]

    def delete_many(self, keys: list[str]=None, *args, **kwargs):
        if keys is None:
            keys = []
        for key in keys:
            self.delete(key, *args, **kwargs)

class HookData:
    def __init__(self, to_object: DefaultToObject=None):
        if to_object is None:
            to_object = DefaultToObject()
        self.to_object: dict = to_object

    def __len__(self):
        return len(self.to_object)
    
    def __iter__(self):
        return iter(self.to_object)
    
    def __contains__(self, key):
        return key in self.to_object

    def __getattr__(self, key):
        try:
            return self.to_object[key]
        except KeyError:
            return super().__getattr__(key)

    def __setattr__(self, key, value):
        self.to_object[key] = value
    
    def __delattr__(self, key):
        try:
            del self.to_object[key]
        except KeyError:
            super().__delattr__(key)

    def __getitem__(self, key):
        return self.to_object[key]
    
    def __setitem__(self, key, value):
        self.to_object[key] = value

    def __delitem__(self, key):
        del self.to_object[key]


class MultiHook:
    def __init__(self, base_hook_name: str, prefix: str = "", to_object: DefaultToObject = None):
        if to_object is None:
            to_object = DefaultToObject()

        self.base_hook_name: str = base_hook_name
        self.prefix: str = prefix
        self._data = to_object

    def scheme(self, hook_name: str, append_base=True):
        if append_base:
            hook_name = f"{self.prefix}{hook_name}{self.base_hook_name}"
        else:
            hook_name = f"{self.prefix}{hook_name}"
        return hook_name
    
    def __mod__(self, other):
        if isinstance(other, str):
            return self.scheme(other)
        elif isinstance(other, (list, tuple)):
            return [self.scheme(item) for item in other]
        elif isinstance(other, dict):
            return {key: self.scheme(value) for key, value in other.items()}
        elif isinstance(other, MultiHook):
            return self.scheme(other.base_hook_name)
        raise TypeError(f"Cannot modulo {type(other)} with MultiHook")
    
    def __rmod__(self, other):
        return self.__mod__(other)
    
    @property
    def hook_name(self):
        return f"{self.prefix}{self.base_hook_name}"

    @property
    def before_hook_name(self):
        return self.scheme("before_")
    
    @property
    def during_hook_name(self):
        return self.hook_name
    
    @property
    def after_hook_name(self):
        return self.scheme("after_")

    def before(self, *args, **kwargs):
        for hook in hooks.get_hooks(self.before_hook_name):
            hook(data=self._data, *args, **kwargs)

    def during(self, *args, **kwargs):
        for hook in hooks.get_hooks(self.during_hook_name):
            hook(data=self._data, *args, **kwargs)

    def after(self, *args, **kwargs):
        for hook in hooks.get_hooks(self.after_hook_name):
            hook(data=self._data, *args, **kwargs)

