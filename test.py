import numpy as np
import pandas as pd
import geopandas as gpd

from pandas_questions import load_data
from pandas_questions import plot_referendum_map
from pandas_questions import merge_referendum_and_areas
from pandas_questions import merge_regions_and_departments
from pandas_questions import compute_referendum_result_by_regions


referendum, df_reg, df_dep = load_data()
regions_and_departments = merge_regions_and_departments(
    df_reg, df_dep
)
referendum_and_areas = merge_referendum_and_areas(
    referendum, regions_and_departments
)

