"""
Portfolio review
"""

import warnings
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from ensuro_analytics.analytics import today
from ensuro_analytics.analytics.dataframe import create_ensuro_accessors


@dataclass
class PortfolioReview:
    """
    A class used to review a portfolio of insurance policies.

    ...

    Attributes
    ----------
    data : pd.DataFrame
        a pandas DataFrame containing the policies data
    split_on : list[str]
        a list of columns to split the portfolio on

    Methods
    -------
    from_data(data: pd.DataFrame, split_on: str | list[str] = ["rm_name"]) -> "PortfolioReview":
        Creates a PortfolioReview object from a dataframe.
    _validate_data(data: pd.DataFrame, cols: Optional[list[str]] = None):
        Validates the data
    review(show_first_date: bool = True, show_predicted_loss_to_exposure: bool = True, show_current_portfolio_pct: bool = True, **kwargs) -> "_CompiledReview":
        Computes the portfolio review
    """

    data: pd.DataFrame
    split_on: list[str]

    @classmethod
    def from_data(
        cls,
        data: pd.DataFrame,
        split_on: str | list[str] = ["rm_name"],
        validate_columns: Optional[list[str]] = None,
    ) -> "PortfolioReview":
        """
        Creates a PortfolioReview object from a dataframe.

        Parameters
        ----------
        data : pd.DataFrame
            policies dataframe
        split_on : str | list[str]
            list of columns to split the portfolio on
        validate_columns : Optional[list[str]]
            list of columns that the data should have; standard policies columns are validated by default.

        Returns
        -------
        PortfolioReview
            a PortfolioReview object
        """

        cls._validate_data(data, cols=validate_columns)
        if isinstance(split_on, str):
            split_on = [split_on]

        create_ensuro_accessors()

        return cls(
            data=data,
            split_on=split_on,
        )

    @staticmethod
    def _validate_data(data: pd.DataFrame, cols: Optional[list[str]] = None):
        """
        Validates the data

        Parameters
        ----------
        data : pd.DataFrame
            policies dataframe
        cols : Optional[list[str]]
            list of columns to validate
        """
        assert "expired_on" in data.columns, "expired_on column is required"
        assert "start" in data.columns, "start column is required"
        assert "expiration" in data.columns, "expiration column is required"
        assert "pure_premium" in data.columns, "pure_premium column is required"
        assert "payout" in data.columns, "payout column is required"
        assert "actual_payout" in data.columns, "actual_payout column is required"

        if cols is not None:
            for col in cols:
                assert col in data.columns, f"{col} column is required"

    def review(
        self,
        show_first_date: bool = True,
        show_predicted_loss_to_exposure: bool = True,
        show_current_portfolio_pct: bool = True,
        average_duration: Optional[str] = None,
        **kwargs,
    ) -> "_CompiledReview":
        """
        Computes the portfolio review

        Parameters
        ----------
        show_first_date : bool
            whether to show the first date in the review
        show_predicted_loss_to_exposure : bool
            whether to show the predicted loss to exposure in the review
        show_current_portfolio_pct : bool
            whether to show the current portfolio percentage in the review
        average_duration : Optional[str]
            If "expected", the expected average duration is shown. If "actual", the actual average duration is shown. If None, the average duration is not shown.
        **kwargs
            arbitrary keyword arguments

        Returns
        -------
        _CompiledReview
            a compiled review object
        """

        columns = [
            "first_date",
            "pred_loss_to_exposure",
            "loss_to_exposure",
            "loss_ratio",
            "volume",
            "current_pct",
            "average_duration",
        ]

        if average_duration is not None:
            if average_duration not in ["expected", "actual"]:
                raise ValueError("average_duration should be 'expected', 'actual', or None")
            elif average_duration == "expected":
                self.data["duration"] = (self.data.expiration - self.data.start).dt.days
            elif average_duration == "actual":
                self.data["duration"] = (self.data.expired_on - self.data.start).dt.days

        if show_current_portfolio_pct is True:
            total_exposure = self.data.exposure.current_value()

        grouped_data = self.data.groupby(self.split_on)

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            result = {
                "loss_to_exposure": grouped_data.apply(
                    lambda x: x.loss_to_exposure.current_value(post_mortem=True)
                ),
                "loss_ratio": grouped_data.apply(lambda x: x.loss_ratio.current_value(post_mortem=True)),
                "volume": grouped_data.apply(lambda x: (x.expiration <= today()).sum()),
            }
        if show_first_date is True:
            result["first_date"] = grouped_data.start.min().dt.date
        else:
            columns.remove("first_date")

        if show_current_portfolio_pct is True:
            result["current_pct"] = (
                grouped_data.apply(lambda x: x.exposure.current_value()) / total_exposure * 100
            )
        else:
            columns.remove("current_pct")

        if show_predicted_loss_to_exposure is True:
            result["pred_loss_to_exposure"] = grouped_data.apply(
                lambda x: x.pure_premium.sum() / x.payout.sum() * 100
            )
        else:
            columns.remove("pred_loss_to_exposure")

        if average_duration is not None:
            result["average_duration"] = grouped_data.duration.mean()
        else:
            columns.remove("average_duration")

        # Put the results in a single dataframe
        results = pd.DataFrame(result)[columns]
        results.sort_index(inplace=True)

        return _CompiledReview(results)


@dataclass
class _CompiledReview:
    """
    A class used to compile and represent the results of a portfolio review.

    ...

    Attributes
    ----------
    portfolio_review : pd.DataFrame
        a pandas DataFrame containing the results of the portfolio review

    Methods
    -------
    to_df() -> pd.DataFrame:
        Returns a copy of the portfolio review results as a pandas DataFrame.
    to_string(**kwargs) -> str:
        Returns a string representation of the portfolio review results.
    print(**kwargs) -> None:
        Prints the string representation of the portfolio review results.
    """

    portfolio_review: pd.DataFrame

    def to_df(self) -> pd.DataFrame:
        """
        Returns a copy of the portfolio review results as a pandas DataFrame.

        Returns
        -------
        pd.DataFrame
            a copy of the portfolio review results
        """

        return self.portfolio_review.copy()

    def to_string(self, **kwargs) -> str:
        """
        Returns a string representation of the portfolio review results.

        Parameters
        ----------
        **kwargs
            arbitrary keyword arguments

        Returns
        -------
        str
            a string representation of the portfolio review results
        """

        return self.portfolio_review.to_string(float_format="{:,.2f}%".format, **kwargs)

    def print(self, **kwargs) -> None:
        """
        Prints the string representation of the portfolio review results.

        Parameters
        ----------
        **kwargs
            arbitrary keyword arguments
        """

        print(self.to_string(**kwargs))
