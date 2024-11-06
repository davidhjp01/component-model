from math import sqrt

import numpy as np
from component_model.model import Model
from component_model.variable import Variable


class BouncingBallXZ(Model):
    """Fmi2Slave implementation of a model made in Python, performing the FMU 'packaging', implements the pythonfmu.Fmi2Slave and runs buildFMU, i.e.
          * prepare the modeldescription.xml
          * implement the FMI2 C interface for the present platform (as .dll, .so, ...).

       The following is expected of any valid Python model:
          * a complete list of variables including meta information, the model.variables dictionary contains that
          * a do_step method specifying what happens at each simulation step

    Args:
       model (obj): reference to the (instantiated) model object

       licenseTxt (str)='Open Source'
       copyright (str)='See copyright notice of used tools'
       defaultExperiment (dict) = None: key/value dictionary for the default experiment setup
       guid (str)=None: Unique identifier of the model (supplied or automatically generated)
       non_default_flags (dict)={}: Any of the defined FMI flags with a non-default value (see FMI 2.0.4, Section 4.3.1)
       **kwargs: Any other keyword argument (transferred to the basic slave object)

    """

    def __init__(
        self,
        name="BouncingBallXZ",
        description="Simple bouncing ball test FMU",
        author="DNV, SEACo project",
        version="0.1",
        defaultExperiment: dict | None = None,
        guid="06128d688f4d404d8f6d49d6e493946b",
        v_min=1e-15,
        **kwargs,
    ):
        if defaultExperiment is None:
            defaultExperiment = {"start_time": 0.0, "step_size": 0.1, "stop_time": 10.0, "tolerance": 0.001}
        super().__init__(
            name=name,
            description=description,
            author=author,
            version=version,
            defaultExperiment=defaultExperiment,
            **kwargs,
        )
        self.v_min = v_min
        Variable(
            self,
            start=(0.0, 0.0),
            name="x",
            description="""Position of ball (x,z) at time.""",
            causality="output",
            variability="continuous",
            initial="exact",
        )
        Variable(
            self,
            start=(1.0, 1.0),
            name="v",
            description="speed at time as (x,z) vector",
            causality="output",
            variability="continuous",
            initial="exact",
        )
        Variable(
            self,
            start=(1.0, 1.0),
            name="v0",
            description="speed at time=0 as (x,z) vector",
            causality="parameter",
            variability="fixed",
            initial="exact",
        )
        Variable(
            self,
            start=0.95,
            name="bounceFactor",
            description="factor on speed when bouncing",
            causality="parameter",
            variability="fixed",
        )
        Variable(
            self,
            start=0.0,
            name="drag",
            description="drag decelleration factor defined as a = self.drag* v^2 with dimension 1/m",
            causality="parameter",
            variability="fixed",
        )
        Variable(
            self,
            start=0.0,
            name="energy",
            description="Total energy of ball in J",
            causality="output",
            variability="continuous",
        )
        Variable(
            self,
            start=0.0,
            name="period",
            description="Bouncing period of ball",
            causality="output",
            variability="continuous",
        )

    #        self.register_variable( String("mdShort", causality=Fmi2Causality.local))

    def enter_initialization_mode(self):
        return True

    def do_step(self, current_time, step_size):
        return True
