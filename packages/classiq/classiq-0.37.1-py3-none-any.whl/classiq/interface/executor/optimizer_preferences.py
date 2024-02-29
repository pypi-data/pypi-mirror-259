from typing import List, Optional

import pydantic
from pydantic import BaseModel

from classiq.interface.helpers.custom_pydantic_types import PydanticAlphaParamCVAR

from classiq._internals.enum_utils import StrEnum


class CostType(StrEnum):
    MIN = "MIN"
    AVERAGE = "AVERAGE"
    CVAR = "CVAR"


class OptimizerType(StrEnum):
    COBYLA = "COBYLA"
    SPSA = "SPSA"
    L_BFGS_B = "L_BFGS_B"
    NELDER_MEAD = "NELDER_MEAD"
    ADAM = "ADAM"


class OptimizerPreferences(BaseModel):
    name: OptimizerType = pydantic.Field(
        default=OptimizerType.COBYLA, description="Classical optimization algorithm."
    )
    num_shots: Optional[pydantic.PositiveInt] = pydantic.Field(
        default=None,
        description="Number of repetitions of the quantum ansatz.",
    )
    max_iteration: pydantic.PositiveInt = pydantic.Field(
        default=100, description="Maximal number of optimizer iterations"
    )
    tolerance: pydantic.PositiveFloat = pydantic.Field(
        default=None, description="Final accuracy in the optimization"
    )
    step_size: pydantic.PositiveFloat = pydantic.Field(
        default=None,
        description="step size for numerically " "calculating the gradient",
    )
    random_seed: Optional[int] = pydantic.Field(
        default=None,
        description="The random seed used for the generation",
    )
    initial_point: Optional[List[float]] = pydantic.Field(
        default=None,
        description="Initial values for the ansatz parameters",
    )
    skip_compute_variance: bool = pydantic.Field(
        default=False,
        description="If True, the optimizer will not compute the variance of the ansatz.",
    )

    @pydantic.validator("tolerance", pre=True, always=True)
    def check_tolerance(cls, tolerance, values):
        optimizer_type = values.get("type")
        if tolerance is not None and optimizer_type == OptimizerType.SPSA:
            raise ValueError("No tolerance param for SPSA optimizer")

        if tolerance is None and optimizer_type != OptimizerType.SPSA:
            tolerance = 0.001

        return tolerance

    @pydantic.validator("step_size", pre=True, always=True)
    def check_step_size(cls, step_size, values):
        optimizer_type = values.get("name")
        if step_size is not None and optimizer_type not in (
            OptimizerType.L_BFGS_B,
            OptimizerType.ADAM,
        ):
            raise ValueError("Use step_size only for L_BFGS_B or ADAM optimizers.")

        if step_size is None and optimizer_type in (
            OptimizerType.L_BFGS_B,
            OptimizerType.ADAM,
        ):
            step_size = 0.05

        return step_size


class GroundStateOptimizer(OptimizerPreferences):
    pass


class CombinatorialOptimizer(OptimizerPreferences):
    cost_type: CostType = pydantic.Field(
        default=CostType.CVAR,
        description="Summarizing method of the measured bit strings",
    )
    alpha_cvar: PydanticAlphaParamCVAR = pydantic.Field(
        default=None, description="Parameter for the CVAR summarizing method"
    )
    is_maximization: bool = pydantic.Field(
        default=False,
        description="Whether the optimization goal is to maximize",
    )
    should_check_valid_solutions: bool = pydantic.Field(
        default=False,
        description="Whether to check if all the solutions satisfy the constraints",
    )

    @pydantic.validator("alpha_cvar", pre=True, always=True)
    def check_alpha_cvar(cls, alpha_cvar, values):
        cost_type = values.get("cost_type")
        if alpha_cvar is not None and cost_type != CostType.CVAR:
            raise ValueError("Use CVAR params only for CostType.CVAR.")

        if alpha_cvar is None and cost_type == CostType.CVAR:
            alpha_cvar = 0.2

        return alpha_cvar
