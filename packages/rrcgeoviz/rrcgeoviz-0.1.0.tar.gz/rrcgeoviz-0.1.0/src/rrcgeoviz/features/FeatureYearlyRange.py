import datetime
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import panel as pn
import seaborn as sns
from sklearn.cluster import DBSCAN
from rrcgeoviz.features.ParentGeovizFeature import ParentGeovizFeature
from rrcgeoviz.arguments import Arguments
import plotly.express as px
import rrcgeoviz


class FeatureYearlyRange(ParentGeovizFeature):
    def getOptionName(self):
        return "yearly_range"

    def getRequiredColumns(self):
        return ["time_column", "latitude_column", "longitude_column"]

    def getHeaderText(self):
        return "Year Range Map"

    def _generateComponent(self):
        year_range_slider = pn.widgets.RangeSlider(
            name="Select Year Range",
            start=self.df["Year"].min(),
            end=self.df["Year"].max(),
            value=(self.df["Year"].min(), self.df["Year"].max()),
            step=1,
        )
        yearly_range_plot = pn.bind(
            self._update_yearly_range_plot, value=year_range_slider
        )

        yearly_range = pn.Column(
            year_range_slider,
            pn.pane.Plotly(yearly_range_plot, sizing_mode="stretch_width"),
        )

        return yearly_range

    def _update_yearly_range_plot(self, value):
        min_year, max_year = value
        filtered_df = self.df[
            (self.df["Year"] >= min_year) & (self.df["Year"] <= max_year)
        ]
        if "hover_text_columns" in self.featureCustomizations:
            fig = px.scatter_mapbox(
                filtered_df,
                lat="latitude",
                lon="longitude",
                hover_name="date",
                hover_data=self.featureCustomizations["hover_text_columns"],
                color="Year",
                zoom=1,
                height=400,
            )
        else:
            fig = px.scatter_mapbox(
                filtered_df,
                lat=self.latitude_column_name,
                lon=self.longitude_column_name,
                color="Year",
                zoom=1,
                height=400,
            )
        fig.update_layout(
            mapbox_style="open-street-map", margin={"r": 20, "t": 20, "l": 20, "b": 20}
        )
        return fig
