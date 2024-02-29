# SPDX-FileCopyrightText: Copyright 2022-2023, Arm Limited and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
"""TOSA data analysis module."""
from __future__ import annotations

from dataclasses import dataclass
from functools import singledispatchmethod

from mlia.backend.tosa_checker.compat import TOSACompatibilityInfo
from mlia.core.common import DataItem
from mlia.core.data_analysis import Fact
from mlia.core.data_analysis import FactExtractor
from mlia.nn.tensorflow.tflite_compat import TFLiteCompatibilityInfo
from mlia.target.common.reporters import analyze_tflite_compatibility_common


@dataclass
class ModelIsTOSACompatible(Fact):
    """Model is completely TOSA compatible."""


@dataclass
class ModelIsNotTOSACompatible(Fact):
    """Model is not TOSA compatible."""


class TOSADataAnalyzer(FactExtractor):
    """TOSA data analyzer."""

    @singledispatchmethod
    def analyze_data(self, data_item: DataItem) -> None:  # type: ignore
        """Analyse the data."""

    @analyze_data.register
    def analyze_tosa_compatibility(self, data_item: TOSACompatibilityInfo) -> None:
        """Analyse TOSA compatibility information."""
        if data_item.tosa_compatible:
            self.add_fact(ModelIsTOSACompatible())
        else:
            self.add_fact(ModelIsNotTOSACompatible())

    @analyze_data.register
    def analyze_tflite_compatibility(self, data_item: TFLiteCompatibilityInfo) -> None:
        """Analyze TensorFlow Lite compatibility information."""
        analyze_tflite_compatibility_common(self, data_item)
