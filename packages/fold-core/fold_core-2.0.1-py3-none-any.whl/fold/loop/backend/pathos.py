# Copyright (c) 2022 - Present Myalo UG (haftungbeschränkt) (Mark Aron Szulyovszky, Daniel Szemerey) <info@dreamfaster.ai>. All rights reserved. See LICENSE in root folder.


from collections.abc import Callable

import pandas as pd
from p_tqdm import p_imap
from tqdm import tqdm

from ...base import Artifact, Composite, Pipeline, TrainedPipeline, X
from ...splitters import Fold
from ..types import Backend, Stage


def train_pipeline(
    self,
    func: Callable,
    pipeline: Pipeline,
    X: pd.DataFrame,
    y: pd.Series,
    artifact: Artifact,
    splits: list[Fold],
    backend: Backend,
    project_name: str,
    project_hyperparameters: dict | None,
    preprocessing_max_memory_size: int,
    silent: bool,
):
    return p_imap(
        lambda split: func(
            X,
            y,
            artifact,
            pipeline,
            split,
            backend,
            project_name,
            project_hyperparameters,
            preprocessing_max_memory_size,
        ),
        splits,
        disable=silent,
    )


def backtest_pipeline(
    self,
    func: Callable,
    pipeline: TrainedPipeline,
    splits: list[Fold],
    X: pd.DataFrame,
    y: pd.Series,
    artifact: Artifact,
    backend: Backend,
    mutate: bool,
    silent: bool,
):
    return p_imap(
        lambda split: func(pipeline, split, X, y, artifact, backend, mutate),
        splits,
        disable=silent,
    )


def process_child_transformations(
    self,
    func: Callable,
    list_of_child_transformations_with_index: list,
    composite: Composite,
    X: X,
    y: pd.Series | None,
    artifacts: Artifact,
    stage: Stage,
    backend: Backend,
    results_primary: list[pd.DataFrame] | None,
    tqdm: tqdm | None = None,
):
    list_of_child_transformations_with_index = [
        {"index": index, "child_transformation": child_transformation}
        for index, child_transformation in list_of_child_transformations_with_index
    ]
    return p_imap(
        lambda obj: func(
            composite,
            obj["index"],
            obj["child_transformation"],
            X,
            y,
            artifacts,
            stage,
            backend,
            results_primary,
            tqdm,
        ),
        list_of_child_transformations_with_index,
        disable=True,
    )


class PathosBackend(Backend):
    name = "pathos"
    process_child_transformations = process_child_transformations
    train_pipeline = train_pipeline
    backtest_pipeline = backtest_pipeline
