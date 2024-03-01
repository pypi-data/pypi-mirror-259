# Copyright (c) 2022 - Present Myalo UG (haftungbeschränkt) (Mark Aron Szulyovszky, Daniel Szemerey) <info@dreamfaster.ai>. All rights reserved. See LICENSE in root folder.

from __future__ import annotations

from collections.abc import Callable
from inspect import getfullargspec

import pandas as pd
from finml_utils.dataframes import concat_on_columns
from sklearn.base import BaseEstimator

from ..base import Artifact, Tunable
from .base import Model


class WrapSKLearnClassifier(Model, Tunable):
    """
    Wraps an SKLearn Classifier model.
    There's no need to use it directly, `fold` automatically wraps all sklearn classifiers into this class.
    """

    def __init__(
        self,
        model_class: type,
        init_args: dict,
        name: str | None = None,
        params_to_try: dict | None = None,
    ) -> None:
        self.model = model_class(**init_args)
        self.params_to_try = params_to_try
        self.name = name or self.model.__class__.__name__
        self.properties = Model.Properties(
            requires_X=True, model_type=Model.Properties.ModelType.classifier
        )

    @classmethod
    def from_model(
        cls,
        model,
        name: str | None = None,
        params_to_try: dict | None = None,
    ) -> WrapSKLearnClassifier:
        return cls(
            model_class=model.__class__,
            init_args=model.get_params(),
            params_to_try=params_to_try,
            name=name,
        )

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        sample_weights: pd.Series | None = None,
        raw_y: pd.Series | None = None,
    ) -> Artifact | None:
        if hasattr(self.model, "partial_fit"):
            self.model.partial_fit(X, y, sample_weights)
        else:
            fit_with_parameters(self.model, X, y, sample_weights)

    def update(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        sample_weights: pd.Series | None = None,
        raw_y: pd.Series | None = None,
    ) -> Artifact | None:
        if hasattr(self.model, "partial_fit"):
            self.model.partial_fit(X, y, sample_weights)

    def predict(self, X: pd.DataFrame) -> pd.Series | pd.DataFrame:
        probabilities = pd.DataFrame(
            data=self.model.predict_proba(X),
            index=X.index,
            columns=[
                f"probabilities_{self.name}_{item}" for item in self.model.classes_
            ],
        )
        predictions = pd.Series(
            data=self.model.predict(X).squeeze(),
            index=X.index,
            name=f"predictions_{self.name}",
        )
        return concat_on_columns([predictions, probabilities])

    predict_in_sample = predict

    def get_params(self) -> dict:
        return self.model.get_params()

    def clone_with_params(
        self, parameters: dict, clone_children: Callable | None = None
    ) -> Tunable:
        return WrapSKLearnClassifier(
            model_class=self.model.__class__,
            init_args=parameters,
            name=self.name,
        )


class WrapSKLearnRegressor(Model, Tunable):
    """
    Wraps an SKLearn regressor model.
    There's no need to use it directly, `fold` automatically wraps all sklearn regressors into this class.
    """

    def __init__(
        self,
        model_class: type,
        init_args: dict,
        name: str | None = None,
        params_to_try: dict | None = None,
    ) -> None:
        self.model = model_class(**init_args)
        self.params_to_try = params_to_try
        self.name = name or self.model.__class__.__name__
        self.properties = Model.Properties(
            requires_X=True, model_type=Model.Properties.ModelType.regressor
        )

    @classmethod
    def from_model(
        cls,
        model,
        name: str | None = None,
        params_to_try: dict | None = None,
    ) -> WrapSKLearnRegressor:
        return cls(
            model_class=model.__class__,
            init_args=model.get_params(),
            name=name,
            params_to_try=params_to_try,
        )

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        sample_weights: pd.Series | None = None,
        raw_y: pd.Series | None = None,
    ) -> Artifact | None:
        if hasattr(self.model, "partial_fit"):
            self.model.partial_fit(X, y, sample_weights)
        else:
            fit_with_parameters(self.model, X, y, sample_weights)

    def update(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        sample_weights: pd.Series | None = None,
        raw_y: pd.Series | None = None,
    ) -> Artifact | None:
        if hasattr(self.model, "partial_fit"):
            self.model.partial_fit(X, y, sample_weights)

    def predict(self, X: pd.DataFrame) -> pd.Series | pd.DataFrame:
        return pd.Series(
            data=self.model.predict(X).squeeze(),
            index=X.index,
            name=f"predictions_{self.name}",
        ).to_frame()

    predict_in_sample = predict

    def get_params(self) -> dict:
        return self.model.get_params()

    def clone_with_params(
        self, parameters: dict, clone_children: Callable | None = None
    ) -> Tunable:
        return WrapSKLearnRegressor(
            model_class=self.model.__class__,
            init_args=parameters,
            name=self.name,
        )


def fit_with_parameters(
    instance: BaseEstimator,
    X: pd.DataFrame,
    y: pd.Series,
    sample_weights: pd.Series | None,
) -> None:
    argspec = getfullargspec(instance.fit)  # type: ignore
    if len(argspec.args) == 1:
        instance.fit(X, y)  # type: ignore
    elif len(argspec.args) == 2:
        instance.fit(X, y, sample_weights)  # type: ignore
    else:
        raise ValueError(
            f"Expected 2 or 3 arguments for fit, but got {len(argspec.args)}."
        )
