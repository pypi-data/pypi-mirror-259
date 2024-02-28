from os import listdir
from os.path import isfile, join
from pathlib import Path
import pickle
from rrcgeoviz.datagenerators.ParentDataGenerator import ParentDataGenerator
from rrcgeoviz.datagenerators.GeneratorExample import GeneratorExample

from rrcgeoviz.arguments import Arguments

DATA_GENERATORS = [GeneratorExample]


class GeneratedData:
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

        self.location = self._setLocation()
        self.should_cache = self._setShouldCache()
        self.use_cache = self._setUseCache()
        self.cache_files = self._setCacheFiles()

        self.data_dict = {}
        self.fresh_data_dict = {}

        # check if each feature was requested to generate
        for generatorType in DATA_GENERATORS:
            generator = generatorType(self.arguments)
            feature = generator.getOptionName()
            if feature in arguments.getFeatures():
                if self.shouldMakeFresh(feature):
                    # actually generate the data
                    self.callDataGeneration(generator)
                else:
                    self.loadData(featureName=feature)

        # if should cache, store the data
        if self.should_cache:
            self.cacheGeneratedData(fresh_data_dict=self.fresh_data_dict)

        # TODO: make any calls to generate_data get the data through the parameter data_dict

    def _setLocation(self):
        if "cache_location" in self.arguments.getCaching():
            return self.arguments.getCaching()["cache_location"]
        else:
            return "/.geovizcache"

    def _setShouldCache(self):
        if (
            "cache_results" in self.arguments.getCaching()
            and self.arguments.getCaching()["cache_results"] == True
        ):
            Path(self.location).mkdir(parents=True, exist_ok=True)
            return True
        else:
            return False

    def _setUseCache(self):
        if (
            "use_cache" in self.arguments.getCaching()
            and self.arguments.getCaching()["use_cache"] == False
        ):
            return False
        else:
            return True

    def _setCacheFiles(self):
        if self.use_cache:
            return [f for f in listdir(self.location) if isfile(join(self.location, f))]
        else:
            return []

    def loadData(self, featureName):
        read_path = self.location + "/" + str(featureName) + ".pkl"
        with open(read_path, "rb") as pickle_file:
            result = pickle.load(pickle_file)
        self.data_dict[featureName] = result

    def callDataGeneration(self, generator: ParentDataGenerator):
        result = generator.generateData()
        self.data_dict[generator.getOptionName()] = result
        self.fresh_data_dict[generator.getOptionName()] = result

    def shouldMakeFresh(self, featureName):
        if str(featureName) + ".pkl" not in self.cache_files or self.use_cache == False:
            return True
        return False

    def cacheGeneratedData(self, fresh_data_dict: dict):
        print("caching data...")
        for key, value in fresh_data_dict.items():
            filepath = self.location + "/" + str(key) + ".pkl"
            file = open(filepath, "wb")
            pickle.dump(value, file)
            file.close()
