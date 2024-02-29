import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
import warnings

# Ignore a specific type of warning
warnings.filterwarnings("ignore")


class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """

    @abstractmethod
    def handle_data(self, data: DataFrame) -> Union[DataFrame, Series]:
        pass


class DataPreprocessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocesses the data.
    """

    def handle_data(self, data: DataFrame) -> DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values, and converts the data type to float.
        """
        try:
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp",
                ],
                axis=1,
            )
            fill_values = {
                 "product_weight_g": data["product_weight_g"].median(),
                 "product_length_cm": data["product_length_cm"].median(),
                 "product_height_cm": data["product_height_cm"].median(),
                 "product_width_cm": data["product_width_cm"].median(),
                 "review_comment_message": "No review"
                 }
            data.fillna(value=fill_values, inplace=True)

            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)

            return data
        except Exception as e:
            logging.error(e)
            raise e


class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """

    def handle_data(self, data: DataFrame) -> Union[DataFrame, Series]:
        """
        Divides the data into train and test data.
        """
        try:
            X = data.drop("review_score", axis=1)
            y = data["review_score"]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(e)
            raise e


class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """

    def __init__(self, data: DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.df = data
        self.strategy = strategy

    def handle_data(self) -> Union[DataFrame, Series]:
        """Handle data based on the provided strategy"""
        return self.strategy.handle_data(self.df)
