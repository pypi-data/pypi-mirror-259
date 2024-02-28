import os
from enum import Enum


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class WonderSchedulerType(Enum):
    DDIM = 'ddim'
    DDPM = 'ddpm'
    DEIS_MULTISTEP = 'deis_multistep'
    DPM_SOLVER_MULTISTEP = 'dpm_solver_multistep'
    DPM_SOLVER_SINGLESTEP = 'dpm_solver_singlestep'
    EULER_ANCESTRAL_DISCRETE = 'euler_ancestral_discrete'
    EULER_DISCRETE = 'euler_discrete'
    HEUN_DISCRETE = 'heun_discrete'
    KDPM2_ANCESTRAL_DISCRETE = 'kdpm2_ancestral_discrete'
    KDPM2_DISCRETE = 'kdpm2_discrete'
    LMS_DISCRETE = 'lms_discrete'
    PNDM = 'pndm'
    UNI_PC_MULTISTEP = 'uni_pc_multistep'


class WonderPipelineType(Enum):
    STABLE_DIFFUSION_XL = 'stable_diffusion_xl'
    STABLE_DIFFUSION_XL_IMG2IMG = 'stable_diffusion_xl_img2img'
    STABLE_DIFFUSION_XL_INPAINT = 'stable_diffusion_xl_inpaint'


class WonderDiffusionModelConfig:

    def __init__(
        self,
        pipeline_type: WonderPipelineType | str,
        pretrained_model_name_or_path: str | os.PathLike,
        initial_scheduler: WonderSchedulerType | str,
        **kwargs
    ):
        self.pipeline_type = pipeline_type if type(pipeline_type) == WonderPipelineType else WonderPipelineType(pipeline_type)
        self.initial_scheduler = initial_scheduler if type(initial_scheduler) == WonderSchedulerType else WonderSchedulerType(initial_scheduler)
        self.pretrained_model_name_or_path = pretrained_model_name_or_path
        self.kwargs = kwargs


class WonderDiffusionSdkConfig:

    def __init__(
        self,
        model_config: WonderDiffusionModelConfig,
        enable_custom_safety_checker: bool = False
    ):
        self.model_config = model_config
        self.enable_custom_safety_checker = enable_custom_safety_checker
