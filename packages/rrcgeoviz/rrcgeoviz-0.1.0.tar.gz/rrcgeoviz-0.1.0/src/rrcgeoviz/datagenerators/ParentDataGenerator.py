from rrcgeoviz.arguments import Arguments


class ParentDataGenerator:
    def __init__(self, args: Arguments) -> None:
        self.args = args

    def getOptionName(self):
        raise NotImplementedError(
            "Generator subclasses need to return the name of the corresponding feature to be put in the options file."
        )

    def generateData(self):
        raise NotImplementedError(
            "Generator subclasses need to return (pickl serializable) data, e.g. a dictionary."
        )
