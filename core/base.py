def default_setup_func(values):
    return values


class Base:

    def __init__(self, func, object_name: str = None):
        self.object_name = object_name if object_name else str(self)
        self.func = func
        self.setups = {}

    def apply(self, params: list) -> (int, dict):
        """

        :param params: list of dicts.
        :return: case: int, and values: dict with the fields for the next block.
        """
        case, values = self.func(self, params)
        return case, values

    def add_setup(self, case, setup_in=None, setup_out=None, setup_func=default_setup_func):  # setup_out = END
        self.setups[case] = Setup(setup_in, setup_out, setup_func)

    def forward(self, params):
        case, values = self.apply(params)
        values["__object_name__"] = self.object_name
        if case in self.setups.keys():
            params.append(self.setups[case].setup(values))
            return self.setups[case].setup_out.forward(params)
        else:
            params.append(values)
            return params


class Setup:

    def __init__(self, setup_in=None, setup_out=None, setup_func=default_setup_func):
        self.setup_in = setup_in
        self.setup_out = setup_out
        self.setup_func = setup_func

    def setup(self, values):
        return self.setup_func(values)


def start_func(self, params):
    case = None
    return case, params


def start_setup_func(params):
    return params


class Start(Base):

    def __init__(self):
        super().__init__(object_name="start", func=start_func)
        self.setups[0] = End()

