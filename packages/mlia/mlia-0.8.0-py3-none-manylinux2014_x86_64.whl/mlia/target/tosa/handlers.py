# SPDX-FileCopyrightText: Copyright 2022-2023, Arm Limited and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
"""TOSA Advisor event handlers."""
# pylint: disable=R0801
from __future__ import annotations

import logging

from mlia.backend.tosa_checker.compat import TOSACompatibilityInfo
from mlia.core.events import CollectedDataEvent
from mlia.core.handlers import WorkflowEventsHandler
from mlia.nn.tensorflow.tflite_compat import TFLiteCompatibilityInfo
from mlia.target.tosa.events import TOSAAdvisorEventHandler
from mlia.target.tosa.events import TOSAAdvisorStartedEvent
from mlia.target.tosa.reporters import tosa_formatters

logger = logging.getLogger(__name__)


class TOSAEventHandler(WorkflowEventsHandler, TOSAAdvisorEventHandler):
    """Event handler for TOSA advisor."""

    def __init__(self) -> None:
        """Init event handler."""
        super().__init__(tosa_formatters)

    def on_tosa_advisor_started(self, event: TOSAAdvisorStartedEvent) -> None:
        """Handle TOSAAdvisorStartedEvent event."""
        self.reporter.submit(event.target)
        self.reporter.submit(event.tosa_metadata)

    def on_collected_data(self, event: CollectedDataEvent) -> None:
        """Handle CollectedDataEvent event."""
        data_item = event.data_item

        if isinstance(data_item, TOSACompatibilityInfo):
            self.reporter.submit(data_item, delay_print=True)

        if isinstance(data_item, TFLiteCompatibilityInfo) and not data_item.compatible:
            self.reporter.submit(data_item, delay_print=True)
