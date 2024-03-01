#
# EIS Equivalent Circuit Model
#
import pybamm
import numpy as np


class EISModel(pybamm.BaseModel):
    """EIS Equivalent Circuit Model for EIS.

    Parameters
    ----------
    name : str, optional
        The name of the model.
    """

    def __init__(self, name="EIS Equivalent Circuit Model"):
        super().__init__({}, name)
       
        # In this case our model is a function of frequency, but given we can treat
        # pybamm's time (i.e. the independent variable) as frequency
        s = pybamm.t
        ######################
        # Parameters
        ######################

        d_s = pybamm.Parameter("Positive electrode diffusivity [m2.s-1]")

        c_s_max = pybamm.Parameter(
            "Maximum concentration in positive electrode [mol.m-3]"
        )

        i_app = param.current_density_with_time

        U = pybamm.Parameter("Reference OCP [V]")

        Uprime = pybamm.Parameter("Derivative of the OCP wrt stoichiometry [V]")

        epsilon = pybamm.Parameter("Positive electrode active material volume fraction")

        r_particle = pybamm.Parameter("Positive particle radius [m]")

        a = 3 * (epsilon / r_particle)

        F = param.F

        l_w = param.p.L

        ######################
        # Governing equations
        ######################
        u_surf = (2 / (np.pi**0.5)) * (i_app / ((d_s**0.5) * a * F * l_w)) * (t**0.5)
        # Linearised voltage
        V = U + (Uprime * u_surf) / c_s_max
        ######################
        # (Some) variables
        ######################
        self.variables = {
            "Voltage [V]": V,
        }

    @property
    def default_geometry(self):
        return {}

    @property
    def default_submesh_types(self):
        return {}

    @property
    def default_var_pts(self):
        return {}

    @property
    def default_spatial_methods(self):
        return {}

    @property
    def default_solver(self):
        return pybamm.DummySolver()
