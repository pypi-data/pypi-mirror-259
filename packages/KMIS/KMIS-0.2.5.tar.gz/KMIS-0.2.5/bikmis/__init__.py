#######################
# BI library for KMIS #
#######################

import datetime
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from delta.tables import DeltaTable
from notebookutils import mssparkutils

from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

import traceback
import sys
import pandas as pd
import time
import pandera as pa
import pyspark.sql.types as T




def calc(num1, num2):
    return num1 + num2
