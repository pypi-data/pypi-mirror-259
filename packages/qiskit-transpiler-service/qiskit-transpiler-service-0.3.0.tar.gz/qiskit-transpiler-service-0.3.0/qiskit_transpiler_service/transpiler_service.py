# -*- coding: utf-8 -*-

# (C) Copyright 2023 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import logging
from typing import List, Union

from qiskit import QuantumCircuit

from .transpiler_service_api import TranspilerServiceAPI

logging.getLogger().setLevel(logging.INFO)


class TranspilerService:
    def __init__(
        self,
        optimization_level: int,
        ai: bool = True,
        coupling_map: Union[List[List[int]], None] = None,
        backend_name: Union[str, None] = None,
        qiskit_transpile_options: dict = None,
        ai_layout_mode: str = None,
    ) -> None:
        self.transpiler_service = TranspilerServiceAPI()

        self.backend_name = backend_name
        self.coupling_map = coupling_map
        self.optimization_level = optimization_level
        self.ai = ai
        self.qiskit_transpile_options = qiskit_transpile_options

        if ai_layout_mode is not None:
            if ai_layout_mode.upper() not in ["KEEP", "OPTIMIZE", "IMPROVE"]:
                raise (
                    f"ERROR. Unknown ai_layout_mode: {ai_layout_mode.upper()}. Valid modes: 'KEEP', 'OPTIMIZE', 'IMPROVE'"
                )
            self.ai_layout_mode = ai_layout_mode.upper()
        else:
            self.ai_layout_mode = ai_layout_mode
        super().__init__()

    def run(
        self,
        circuits: Union[List[Union[str, QuantumCircuit]], Union[str, QuantumCircuit]],
    ):
        logging.info(f"Requesting transpile to the service")
        transpile_result = self.transpiler_service.transpile(
            circuits=circuits,
            backend=self.backend_name,
            coupling_map=self.coupling_map,
            optimization_level=self.optimization_level,
            ai=self.ai,
            qiskit_transpile_options=self.qiskit_transpile_options,
        )
        if transpile_result is None:
            logging.warning("Cloud Transpiler couldn't transpile the circuit(s)")
            return None

        # TODO: Restore final measurements if they were removed

        logging.info("Cloud Transpiler returned a result!")
        return transpile_result
