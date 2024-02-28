import os
import string
import threading
from time import sleep
import time
import pandas as pd
import panel as pn
from bokeh.models import Div
from rrcgeoviz.features.FeatureOneYearMonths import FeatureOneYearMonths
from rrcgeoviz.features.FeatureOneYear import FeatureOneYear
from rrcgeoviz.features.FeatureAllMonths import FeatureAllMonths
from rrcgeoviz.features.FeatureHeatmap import FeatureHeatmap
from rrcgeoviz.features.FeatureThreeD import FeatureThreeD
from rrcgeoviz.features.FeatureYearlyRange import FeatureYearlyRange
from rrcgeoviz.features.pandas_profile import gen_profile_report
import warnings
from rrcgeoviz.arguments import Arguments

from panel.widgets.indicators import BooleanIndicator
from dateutil.parser import parse
from panel.io import server

import importlib.resources
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

LOGO_PATH = "https://i.imgur.com/Loud9RB.jpeg"
FAVICON_PATH = "https://i.imgur.com/x0JaYkq.png"

ALL_FEATURE_CLASSES = [
    FeatureHeatmap,
    FeatureYearlyRange,
    FeatureOneYear,
    FeatureAllMonths,
    FeatureOneYearMonths,
    FeatureThreeD,
]


class GeoVizPanelDashboard:
    def __init__(self, args: Arguments, test=False) -> None:
        self.test = test
        self.args = args
        self.columns = self.args.getColumns()
        self.data = self.args.getData()
        self.features = self.args.getFeatures()
        self.data = self.verifyDataFormat()
        self.data = self.modify_columns()
        self.dashboard = self.create_template(args)

    def render(self):
        if not self.test:
            pn.serve(self.dashboard)

    def verifyDataFormat(self) -> pd.DataFrame:
        self._verifyDataColumnsExist()

        self._warnIfNanExists()

        try:
            pd.to_datetime(self.data[self.columns["time_column"]])
        except:
            raise TypeError(
                "The given time column can't be parsed into datetime format."
            )

        if not is_numeric_dtype(self.data[self.columns["latitude_column"]]):
            raise TypeError("The given latitude column is non-numeric.")

        if not is_numeric_dtype(self.data[self.columns["longitude_column"]]):
            raise TypeError("The given longitude column is non-numeric.")

        if not ((self.data[self.columns["latitude_column"]] > -90).all()):
            raise TypeError("There are latitude values below -90.")
        if not ((self.data[self.columns["latitude_column"]] < 90).all()):
            raise TypeError("There are latitude values above 90.")

        if not ((self.data[self.columns["longitude_column"]] > -180).all()):
            raise TypeError("There are latitude values below -180.")
        if not ((self.data[self.columns["longitude_column"]] < 180).all()):
            raise TypeError("There are latitude values above 180.")

        return self.data

    def _warnIfNanExists(self):
        error_message = "A null value was found in the dataset. GeoViz ignores any rows with null values in the latitude, longitude, or date columns."
        relevant_data = self.data[self.columns.values()]
        null_columns = relevant_data.isnull().any()
        already_warned = False
        for col_name, is_null in null_columns.items():
            # index, 0
            if is_null and not already_warned:
                already_warned = True
                warnings.warn(error_message, UserWarning)
                self.data.dropna(subset=[col_name], inplace=True)

        return self.data

    def _verifyDataColumnsExist(self):
        error_message = "An incorrect column name was given. Check for misspellings and different capitalizations in the columns options section."
        if "time_column" in self.columns:
            if self.columns["time_column"] not in self.data.columns:
                raise TypeError(error_message)

        if "latitude_column" in self.columns:
            if self.columns["latitude_column"] not in self.data.columns:
                raise TypeError(error_message)

        if "longitude_column" in self.columns:
            if self.columns["longitude_column"] not in self.data.columns:
                raise TypeError(error_message)

    def modify_columns(self):
        if "time_column" in self.columns:
            self.data[self.columns["time_column"]] = pd.to_datetime(
                self.data[self.columns["time_column"]]
            )
        return self.data

    def create_template(self, args: Arguments):
        template = pn.template.BootstrapTemplate(
            title="GeoViz - " + str(args.getDataFileName()),
            collapsed_sidebar=True,
            logo=LOGO_PATH,
            favicon=FAVICON_PATH,
        )
        mainColumn = pn.Column()
        mainColumn = self.addCorrectElements(args, mainColumn)

        template.main.append(
            pn.Tabs(
                ("Visualizations", mainColumn),
                ("Pandas Profiling", pn.Column(gen_profile_report(args))),
            )
        )

        return template

    def addCorrectElements(self, arguments: Arguments, mainColumn):
        """Actually add the right elements to the display.
        A dictionary of generated data and the arguments are available for purchase at the gift store.
        """
        for featureType in ALL_FEATURE_CLASSES:
            feature = featureType(arguments)
            if feature.getOptionName() in self.features:
                for required_column in feature.getRequiredColumns():
                    if required_column not in self.columns:
                        raise TypeError(
                            "Column "
                            + required_column
                            + " is required for "
                            + feature.getOptionName()
                        )

                mainColumn.append(
                    pn.pane.HTML("<h2>" + feature.getHeaderText() + "</h2>")
                )
                mainColumn.append(feature.generateFeature())

        return mainColumn
