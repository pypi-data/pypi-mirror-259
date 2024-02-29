import torch
import logging

from diffusers import DiffusionPipeline, AutoencoderKL

from .types import (
    WonderPipelineType,
    WonderSchedulerType)

from .config import (
    DEVICE,
    PIPELINE_MAP,
    SCHEDULER_MAP,
    WonderDiffusionSdkConfig,
    WonderDiffusionModelConfig)


logger = logging.getLogger(__name__)


class WonderDiffusionSdk:

    def __init__(self, config: WonderDiffusionSdkConfig):
        if config.enable_custom_safety_checker:
            self.initialize_safety_checker()

    def initialize_pipeline(self, model_config: WonderDiffusionModelConfig):
        #
        logger.info(f'DIFFUSION SDK LOG: Initializing pipeline with config: {model_config}')
        kwargs = self._get_pipeline_kwargs(model_config.precision)
        #
        logger.info(f'DIFFUSION SDK LOG: Using kwargs: {kwargs["torch_dtype"]}')
        pipeline = PIPELINE_MAP[model_config.pipeline_type](
            model_config.pretrained_model_name_or_path, **kwargs)
        #
        logger.info(f'DIFFUSION SDK LOG: Pipeline initialized with type: {model_config.pipeline_type}, pipeline class: {type(pipeline)}')

        pipeline.scheduler = SCHEDULER_MAP[model_config.initial_scheduler](
            pipeline.scheduler.config)

        if model_config.use_half_precision_vae:
            self._half_precision_vae(pipeline)

        if model_config.fuse_qkv_projections:
            self._fuse_qkv_projections(pipeline)

        if model_config.use_channels_last:
            self._use_channels_last(pipeline)

        pipeline.to(DEVICE)

        if model_config.use_deep_cache:
            self.enable_deepcache(pipeline)

        return pipeline

    # Optimization functions

    def _get_pipeline_kwargs(self, precision):
        kwargs = {}
        if precision == 'bfloat16':
            kwargs['torch_dtype'] = torch.bfloat16
        elif precision == 'float16':
            kwargs['torch_dtype'] = torch.float16
            kwargs['variant'] = 'fp16'
            kwargs['use_safetensors'] = True
        return kwargs

    def _half_precision_vae(self, pipeline: DiffusionPipeline):
        #
        logger.info('DIFFUSION SDK LOG: Using half precision VAE')
        pipeline.vae = AutoencoderKL.from_pretrained(
            'madebyollin/sdxl-vae-fp16-fix', torch_dtype=torch.bfloat16)

    def _fuse_qkv_projections(self, pipeline: DiffusionPipeline):
        #
        logger.info('DIFFUSION SDK LOG: Fusing QKV projections')
        pipeline.unet.fuse_qkv_projections()
        pipeline.vae.fuse_qkv_projections()

    def _use_channels_last(self, pipeline: DiffusionPipeline):
        #
        logger.info('DIFFUSION SDK LOG: Using channels last')
        pipeline.unet.to(memory_format=torch.channels_last)

    def enable_deepcache(self, pipeline: DiffusionPipeline):
        #
        logger.info('DIFFUSION SDK LOG: Enabling deep cache')
        from .components import enable_deepcache
        self.deepcache_helper = enable_deepcache(pipeline)

    def disable_deepcache(self):
        if hasattr(self, 'deepcache_helper'):
            self.deepcache_helper.disable()

    # Diffusion functions

    def set_scheduler(self, pipeline: DiffusionPipeline, scheduler: WonderSchedulerType):
        if scheduler in SCHEDULER_MAP:
            pipeline.scheduler = SCHEDULER_MAP[scheduler](
                pipeline.scheduler.config)

    def run(self, pipeline: DiffusionPipeline, args: dict):
        return pipeline(**args).images

    # Safety checker

    def initialize_safety_checker(self):
        from transformers import AutoFeatureExtractor
        from .components import StableDiffusionSafetyChecker
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(
            'CompVis/stable-diffusion-safety-checker')
        self.safety_checker = StableDiffusionSafetyChecker.from_pretrained(
            'CompVis/stable-diffusion-safety-checker').to(DEVICE)

    def safety_check(self, images):
        if not hasattr(self, 'safety_checker'):
            self.initialize_safety_checker()

        safety_checker_input = self.feature_extractor(
            images, return_tensors='pt').to(DEVICE)
        images, has_nsfw_concept = self.safety_checker(
            images=images, clip_input=safety_checker_input.pixel_values.to(torch.float16))
        return images, has_nsfw_concept
