import logging
from typing import List, Optional, Union

import numpy as np
import pandas as pd
import pyarrow as pa

from ray.data.preprocessor import Preprocessor
from ray.util.annotations import PublicAPI

from reader import Reader

logger = logging.getLogger(__name__)


@PublicAPI(stability="alpha")
class VistudioV1Reader(Reader):
    """Reads a Vistudio dataset."""

    def __init__(self):
        super().__init__()

    def get_schema() -> pa.schema:
        
        return pa.schema({"name": pa.string(), "float_field": pa.float64(), "int_field": pa.int32()})