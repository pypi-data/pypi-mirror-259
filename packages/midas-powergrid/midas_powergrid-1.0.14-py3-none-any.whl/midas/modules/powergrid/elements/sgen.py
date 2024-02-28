import logging
import pandapower as pp
from ..constraints.sgen_voltage_change import ConstraintSgenVoltageChange
from .base import GridElement

LOG = logging.getLogger(__name__)


class PPSgen(GridElement):
    @staticmethod
    def pp_key() -> str:
        return "sgen"

    @staticmethod
    def res_pp_key() -> str:
        return "res_sgen"

    def __init__(self, index, grid, value=0.05):
        super().__init__(index, grid, LOG)

        self.current_bus_voltage = 1.0
        self.in_service = True
        self.p_mw = getattr(grid, self.pp_key()).p_mw.iloc[index]
        self.q_mvar = getattr(grid, self.pp_key()).q_mvar.iloc[index]

        self._constraints.append(ConstraintSgenVoltageChange(self, value))

    def step(self, time):
        old_state = self.in_service
        self.in_service = True
        self._check(time)

        self.set_value("p_mw", self.p_mw)
        self.set_value("q_mvar", self.q_mvar)
        self.set_value("in_service", self.in_service)
        # Run powerflow so that the next unit does not automatically
        # switch off, too.
        if old_state != self.in_service:
            if not self.in_service:
                LOG.debug(
                    f"At step {time}: Sgen {self.index} with p={self.p_mw:.5f} "
                    f"and q={self.q_mvar:.5f} out of service (Bus voltage: "
                    f"{self.current_bus_voltage:.5f})"
                )
                try:
                    pp.runpp(self.grid)
                except pp.LoadflowNotConverged:
                    LOG.debug("Sgen disabled. PF still not converging.")
            else:
                LOG.debug(
                    f"At step {time}: Sgen {self.index} back in service."
                )
                try:
                    pp.runpp(self.grid)
                except pp.LoadflowNotConverged:
                    LOG.debug("Sgen re-enabled. PF not converging.")

        return old_state != self.in_service
