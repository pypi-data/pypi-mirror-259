import logging
from typing import List, Optional, Union

import numpy as np
import pandas as pd
import pyarrow as pa

from ray.data.preprocessor import Preprocessor
from ray.util.annotations import PublicAPI

logger = logging.getLogger(__name__)


@PublicAPI(stability="alpha")
class Reader(Preprocessor):
    """Reader."""

    def read():
        """Read the data."""
        raise NotImplementedError

    def get_schema() -> pa.schema:
        """Get the schema of the reader."""
        raise NotImplementedError