import torch
from wonder_sdk import WonderSdk

from diffusers import (
    StableDiffusionXLPipeline,
    StableDiffusionXLImg2ImgPipeline,
    StableDiffusionXLInpaintPipeline)

from diffusers import (
    DDIMScheduler,
    DDPMScheduler,
    DEISMultistepScheduler,
    DPMSolverMultistepScheduler,
    DPMSolverSinglestepScheduler,
    EulerAncestralDiscreteScheduler,
    EulerDiscreteScheduler,
    HeunDiscreteScheduler,
    KDPM2AncestralDiscreteScheduler,
    KDPM2DiscreteScheduler,
    LMSDiscreteScheduler,
    PNDMScheduler,
    UniPCMultistepScheduler)

from .config import (
    WonderPipelineType,
    WonderSchedulerType,
    WonderDiffusionModelConfig,
    WonderDiffusionSdkConfig)

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

PIPELINE_MAP = {
    WonderPipelineType.STABLE_DIFFUSION_XL: lambda pretrained_model_name_or_path, **kwargs: StableDiffusionXLPipeline.from_pretrained(pretrained_model_name_or_path, **kwargs),
    WonderPipelineType.STABLE_DIFFUSION_XL_IMG2IMG: lambda pretrained_model_name_or_path, **kwargs: StableDiffusionXLImg2ImgPipeline.from_pretrained(pretrained_model_name_or_path, **kwargs),
    WonderPipelineType.STABLE_DIFFUSION_XL_INPAINT: lambda pretrained_model_name_or_path, **kwargs: StableDiffusionXLInpaintPipeline.from_pretrained(pretrained_model_name_or_path, **kwargs),
}

SCHEDULER_MAP = {
    WonderSchedulerType.DDIM: lambda config: DDIMScheduler.from_config(config),
    WonderSchedulerType.DDPM: lambda config: DDPMScheduler.from_config(config),
    WonderSchedulerType.DEIS_MULTISTEP: lambda config: DEISMultistepScheduler.from_config(config),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP: lambda config: DPMSolverMultistepScheduler.from_config(config),
    WonderSchedulerType.DPM_SOLVER_SINGLESTEP: lambda config: DPMSolverSinglestepScheduler.from_config(config),
    WonderSchedulerType.EULER_ANCESTRAL_DISCRETE: lambda config: EulerAncestralDiscreteScheduler.from_config(config),
    WonderSchedulerType.EULER_DISCRETE: lambda config: EulerDiscreteScheduler.from_config(config),
    WonderSchedulerType.HEUN_DISCRETE: lambda config: HeunDiscreteScheduler.from_config(config),
    WonderSchedulerType.KDPM2_ANCESTRAL_DISCRETE: lambda config: KDPM2AncestralDiscreteScheduler.from_config(config),
    WonderSchedulerType.KDPM2_DISCRETE: lambda config: KDPM2DiscreteScheduler.from_config(config),
    WonderSchedulerType.LMS_DISCRETE: lambda config: LMSDiscreteScheduler.from_config(config),
    WonderSchedulerType.PNDM: lambda config: PNDMScheduler.from_config(config),
    WonderSchedulerType.UNI_PC_MULTISTEP: lambda config: UniPCMultistepScheduler.from_config(config),
}

# TODO:
# - scheduler initializtionlar degisken olabiliyor, algorithm tarzi parametreler alabiliyor
# - imageId yi docId diye degistir (cloud functionlarda)


class WonderDiffusionSdk:

    def __init__(self, sdk: WonderSdk, config: WonderDiffusionSdkConfig):
        self.sdk = sdk
        self.config = config

        self.initialize_pipeline(config.model_config)
        if config.enable_custom_safety_checker:
            self.initialize_safety_checker()

    def initialize_pipeline(self, model_config: WonderDiffusionModelConfig):
        self.pipeline = PIPELINE_MAP[model_config.pipeline_type](
            model_config.pretrained_model_name_or_path, **model_config.kwargs)
        self.pipeline.to(DEVICE)

        self.pipeline.scheduler = SCHEDULER_MAP[model_config.initial_scheduler](
            self.pipeline.scheduler.config)
        self.current_scheduler = model_config.initial_scheduler

    def initialize_safety_checker(self):
        from transformers import AutoFeatureExtractor
        from .safety_checker import StableDiffusionSafetyChecker
        self.feature_extractor = AutoFeatureExtractor.from_pretrained('CompVis/stable-diffusion-safety-checker')
        self.safety_checker = StableDiffusionSafetyChecker.from_pretrained('CompVis/stable-diffusion-safety-checker').to('cuda')

    def run(self, data: dict):
        self.change_scheduler_if_needed(data.get('scheduler', None))
        images = self.pipeline(**data).images

        if self.config.enable_custom_safety_checker:
            images, has_nsfw_concept = self.safety_check(images)
            return images, has_nsfw_concept
        else:
            return images

    def change_scheduler_if_needed(self, scheduler: WonderSchedulerType):
        if scheduler != self.current_scheduler and scheduler in SCHEDULER_MAP:
            self.pipeline.scheduler = SCHEDULER_MAP[scheduler](
                self.pipeline.scheduler.config)
            self.current_scheduler = scheduler

    def safety_check(self, images):
        safety_checker_input = self.feature_extractor(images, return_tensors="pt").to('cuda')
        images, has_nsfw_concept = self.safety_checker(images=images, clip_input=safety_checker_input.pixel_values.to(torch.float16))
        return images, has_nsfw_concept