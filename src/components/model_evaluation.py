import pandas as pd 
import numpy as np
from src.logger.logger import logging
from src.exception.exception import CustomException
import os, sys
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import load_object
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse


@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e, sys)
