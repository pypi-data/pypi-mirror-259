# SPDX-FileCopyrightText: Copyright 2022-2023, Arm Limited and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
"""Ethos-U MLIA module events."""
from dataclasses import dataclass
from pathlib import Path

from mlia.core.events import Event
from mlia.core.events import EventDispatcher
from mlia.target.ethos_u.config import EthosUConfiguration


@dataclass
class EthosUAdvisorStartedEvent(Event):
    """Event with Ethos-U advisor parameters."""

    model: Path
    target_config: EthosUConfiguration


class EthosUAdvisorEventHandler(EventDispatcher):
    """Event handler for the Ethos-U inference advisor."""

    def on_ethos_u_advisor_started(self, event: EthosUAdvisorStartedEvent) -> None:
        """Handle EthosUAdvisorStarted event."""
