import datetime
from rrcgeoviz.datagenerators.ParentDataGenerator import ParentDataGenerator


class GeneratorExample(ParentDataGenerator):
    def getOptionName(self):
        return "generator_example"

    def generateData(self):
        """An example of making a data generation function.
        Every data generator should take an Arguments object and return the data in a pickle-storable format.
        """
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        return formatted_time
