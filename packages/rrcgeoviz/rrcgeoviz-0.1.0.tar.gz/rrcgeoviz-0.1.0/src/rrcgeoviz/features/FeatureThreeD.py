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


class FeatureThreeD(ParentGeovizFeature):
    def getOptionName(self):
        return "threeD"

    def getRequiredColumns(self):
        return ["time_column", "latitude_column", "longitude_column"]

    def getHeaderText(self):
        return "Latitude/Longitude/Time 3D Visualization"

    def _generateComponent(self):
        first_datetime = self.df[self.time_column_name].min()

        self.df["days_int"] = (self.df[self.time_column_name] - first_datetime).dt.days
        lat_min, lat_max = (
            self.df[self.latitude_column_name].min(),
            self.df[self.latitude_column_name].max(),
        )
        long_min, long_max = (
            self.df[self.longitude_column_name].min(),
            self.df[self.longitude_column_name].max(),
        )
        date_min, date_max = self.df["days_int"].min(), self.df["days_int"].max()
        self.df["Normalized_Longitude"] = (
            self.df[self.longitude_column_name] - long_min
        ) / (long_max - long_min)
        self.df["Normalized_Latitude"] = (
            self.df[self.latitude_column_name] - lat_min
        ) / (lat_max - lat_min)
        self.df["Time"] = (self.df["days_int"] - date_min) / (date_max - date_min)
        X = self.df[["Normalized_Longitude", "Normalized_Latitude", "Time"]].dropna()
        db = DBSCAN(eps=0.05, min_samples=5)
        try:
            self.df["cluster"] = db.fit_predict(X)
        except:
            raise TypeError(
                "An error occured trying to cluster for the threeD feature. Most likely, not enough data is available for clustering."
            )
        num_colors = len(self.df)
        colors = np.random.randint(0, 256, size=(num_colors, 3))
        plotly_df = pd.concat(
            [self.df, pd.DataFrame(colors, columns=["r", "g", "b"])], axis=1
        )
        fig = px.scatter_3d(
            plotly_df,
            x="Normalized_Longitude",
            y="Normalized_Latitude",
            z="Time",
            color="cluster",
            color_continuous_scale="solar",
            size_max=10,
        )
        fig.update_layout(scene_aspectmode="auto")
        fig.update_layout(width=800, height=800)

        three_D = pn.Column(fig)

        return three_D
