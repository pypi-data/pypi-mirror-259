# SPDX-FileCopyrightText: Copyright 2022-2023, Arm Limited and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
"""Cortex-A MLIA module."""
from __future__ import annotations

from pathlib import Path
from typing import Any
from typing import cast

from mlia.core.advice_generation import AdviceProducer
from mlia.core.advisor import DefaultInferenceAdvisor
from mlia.core.advisor import InferenceAdvisor
from mlia.core.common import AdviceCategory
from mlia.core.context import Context
from mlia.core.context import ExecutionContext
from mlia.core.data_analysis import DataAnalyzer
from mlia.core.data_collection import DataCollector
from mlia.core.events import Event
from mlia.target.common.optimization import add_common_optimization_params
from mlia.target.common.optimization import OptimizingDataCollector
from mlia.target.cortex_a.advice_generation import CortexAAdviceProducer
from mlia.target.cortex_a.config import CortexAConfiguration
from mlia.target.cortex_a.data_analysis import CortexADataAnalyzer
from mlia.target.cortex_a.data_collection import CortexAOperatorCompatibility
from mlia.target.cortex_a.events import CortexAAdvisorStartedEvent
from mlia.target.cortex_a.handlers import CortexAEventHandler
from mlia.target.registry import profile


class CortexAInferenceAdvisor(DefaultInferenceAdvisor):
    """Cortex-A Inference Advisor."""

    @classmethod
    def name(cls) -> str:
        """Return name of the advisor."""
        return "cortex_a_inference_advisor"

    def get_collectors(self, context: Context) -> list[DataCollector]:
        """Return list of the data collectors."""
        model = self.get_model(context)
        target_profile = self.get_target_profile(context)
        target_config = cast(CortexAConfiguration, profile(target_profile))

        collectors: list[DataCollector] = []

        if context.category_enabled(AdviceCategory.COMPATIBILITY):
            collectors.append(CortexAOperatorCompatibility(model, target_config))

        if context.category_enabled(AdviceCategory.PERFORMANCE):
            raise RuntimeError(
                "Performance estimation is currently not supported for Cortex-A."
            )

        if context.category_enabled(AdviceCategory.OPTIMIZATION):
            collectors.append(OptimizingDataCollector(model, target_config))

        return collectors

    def get_analyzers(self, context: Context) -> list[DataAnalyzer]:
        """Return list of the data analyzers."""
        return [
            CortexADataAnalyzer(),
        ]

    def get_producers(self, context: Context) -> list[AdviceProducer]:
        """Return list of the advice producers."""
        return [CortexAAdviceProducer()]

    def get_events(self, context: Context) -> list[Event]:
        """Return list of the startup events."""
        model = self.get_model(context)
        target_profile = self.get_target_profile(context)

        return [
            CortexAAdvisorStartedEvent(
                model, cast(CortexAConfiguration, profile(target_profile))
            ),
        ]


def configure_and_get_cortexa_advisor(
    context: ExecutionContext,
    target_profile: str | Path,
    model: str | Path,
    **extra_args: Any,
) -> InferenceAdvisor:
    """Create and configure Cortex-A advisor."""
    if context.event_handlers is None:
        context.event_handlers = [CortexAEventHandler()]

    if context.config_parameters is None:
        context.config_parameters = _get_config_parameters(
            model, target_profile, **extra_args
        )

    return CortexAInferenceAdvisor()


def _get_config_parameters(
    model: str | Path, target_profile: str | Path, **extra_args: Any
) -> dict[str, Any]:
    """Get configuration parameters for the advisor."""
    advisor_parameters: dict[str, Any] = {
        "cortex_a_inference_advisor": {
            "model": str(model),
            "target_profile": target_profile,
        },
    }
    add_common_optimization_params(advisor_parameters, extra_args)
    return advisor_parameters
