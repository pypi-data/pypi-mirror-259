from collections import Counter
from collections.abc import Callable
from copy import deepcopy

from deepmerge import always_merger

from ..base import Clonable, Composite, Pipeline, Transformation, Tunable, traverse
from ..transformations.dev import Identity


def _process_params(params_to_try: dict) -> dict:
    if "passthrough" in params_to_try:
        params_to_try["passthrough"] = [True, False]
    return params_to_try


def _get_tunables_with_params_to_try(pipeline: Pipeline) -> list[Tunable]:
    return [
        i
        for i in traverse(pipeline)
        if isinstance(i, Tunable) and i.get_params_to_try() is not None
    ]


def _apply_params(params: dict) -> Callable:
    def __apply_params_to_transformation(
        item: Composite | Transformation, clone_children: Callable
    ) -> Composite | Transformation:
        if not isinstance(item, Tunable):
            if isinstance(item, Clonable):
                return item.clone(clone_children)
            return item
        selected_params = params.get(item.name, {})
        if "passthrough" in selected_params and selected_params["passthrough"] is True:
            return Identity()  # type: ignore
        return item.clone_with_params(
            parameters=always_merger.merge(
                item.get_params(), _clean_params(selected_params)
            ),
            clone_children=clone_children,
        )  # type: ignore

    return __apply_params_to_transformation


def _clean_params(params_to_try: dict, keys: list[str] | None = None) -> dict:
    if keys is None:
        keys = ["passthrough", "_conditional"]
    return {
        k: _clean_params(v) if isinstance(v, dict) else deepcopy(v)
        for k, v in params_to_try.items()
        if k not in keys
    }


def _check_for_duplicate_names(pipeline: Pipeline):
    names = [i.name for i in _get_tunables_with_params_to_try(pipeline)]
    if len(set(names)) != len(names):
        duplicate_names = [item for item, count in Counter(names).items() if count > 1]
        raise ValueError(
            f"Duplicate names in pipeline are not allowed. {duplicate_names}"
        )


def _extract_param_grid(pipeline: Pipeline, divider: str = "¦"):
    tunables = _get_tunables_with_params_to_try(pipeline)

    return {
        f"{transformation.name}{divider}{key}": value
        for transformation in tunables
        for key, value in _process_params(transformation.get_params_to_try()).items()
    }
