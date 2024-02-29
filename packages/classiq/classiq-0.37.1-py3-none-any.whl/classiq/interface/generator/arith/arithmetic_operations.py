from __future__ import annotations

import abc
from typing import ClassVar, Iterable, Optional, Tuple

import pydantic

from classiq.interface.generator.arith import argument_utils, number_utils
from classiq.interface.generator.arith.register_user_input import RegisterArithmeticInfo
from classiq.interface.generator.function_params import FunctionParams

DEFAULT_GARBAGE_OUT_NAME: str = "extra_qubits"


class ArithmeticOperationParams(FunctionParams):
    output_size: Optional[pydantic.PositiveInt]
    machine_precision: pydantic.PositiveInt = number_utils.MAX_FRACTION_PLACES
    output_name: ClassVar[str]
    garbage_output_name: ClassVar[str] = DEFAULT_GARBAGE_OUT_NAME
    _result_register: Optional[RegisterArithmeticInfo] = pydantic.PrivateAttr(
        default=None
    )

    @abc.abstractmethod
    def _get_result_register(self) -> RegisterArithmeticInfo:
        pass

    @property
    def result_register(self) -> RegisterArithmeticInfo:
        if self._result_register is None:
            self._result_register = self._get_result_register()
        return self._result_register

    @abc.abstractmethod
    def is_inplaced(self) -> bool:
        pass

    @property
    def _include_sign(self) -> bool:
        return self.output_size is None

    def _legal_bounds(
        self, suggested_bounds: Tuple[float, float]
    ) -> Optional[Tuple[float, float]]:
        if self._include_sign or min(suggested_bounds) >= 0:
            return suggested_bounds
        return None

    def _compute_fraction_places(self, argument: argument_utils.RegisterOrConst) -> int:
        return argument_utils.fraction_places(
            argument, machine_precision=self.machine_precision
        )

    @abc.abstractmethod
    def get_params_inplace_options(self) -> Iterable[ArithmeticOperationParams]:
        pass
