class Constant:
    @classmethod
    def get_choices(cls):
        if hasattr(cls, "CHOICES"):
            return getattr(cls, "CHOICES")
        return []

    @classmethod
    def get_options(cls):
        options = []

        for choice in cls.get_choices():
            options.append(
                {
                    "value": choice[0],
                    "label": choice[1],
                }
            )
        return options

    @classmethod
    def get_display(cls, name):
        data = dict(cls.get_choices())
        return data.get(name, "")

    @classmethod
    def get_values(cls, *, exclude_field=("CHOICES",)):
        d = cls.__dict__
        ret = {
            str(d[item])
            for item in d.keys()
            if not item.startswith("_") and item not in exclude_field
        }
        return list(ret)

    @classmethod
    def get_key_by_value(cls, value):
        for items in cls.__dict__["CHOICES"]:
            if items[1] == value:
                key = items[0]
                return key
        return None

