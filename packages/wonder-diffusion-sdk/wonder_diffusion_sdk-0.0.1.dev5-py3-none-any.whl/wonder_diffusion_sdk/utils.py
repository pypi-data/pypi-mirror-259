from random import randint
import json

"""
def get_config_keys_from_storage(self):
    try:
        self.keyValue = json.loads(self.sdk.download_from_bucket(
            self.config.private_bucket_name, 'config_keys.json', download_as_text=True))
    except Exception as e:
        self.sdk.logger.error(
            f'Could not download config_keys, using the local file. Error: {e}')
        f = open('config_keys.json', 'r')
        self.keyValue = json.load(f)
        f.close()
    self.sdk.logger.debug(f'config_keys: {self.keyValue}')

def process_prompt(sdk, keyValue, prompt, style, language_code):
    style = keyValue[style] if style in keyValue else style

    translated_prompt = prompt

    if language_code != 'en':
        translated_prompt = sdk.translate_text(
            translated_prompt, target_language='en')

    if '<<prompt>>' in style:
        translated_prompt = style.replace('<<prompt>>', translated_prompt)
    else:
        translated_prompt = f'{translated_prompt}, {style}' if style != '' and style != None else translated_prompt
    translated_prompt = translated_prompt.strip()

    sdk.logger.info(f'Proccessed prompt: {translated_prompt}')
    return translated_prompt

def parse_arguments(self, data: dict):
    self.args = {}
    for arg in self.config.expected_arguments.keys():
        self.args[arg] = data.get(arg, self.config.expected_arguments[arg])

    self.args = dotdict(self.args)
    self.sdk.logger.debug(f'Parsed arguments: {self.args}')

    if 'doc_id' not in self.args and 'imageId' in self.args:
        self.args.doc_id = self.args.imageId

    return self.args.doc_id

def generator(self):
    if self.args.seed == None or self.args.seed < 0:
        self.args.seed = randint(0, 2**32-1)
    return torch.Generator(device=DEVICE).manual_seed(self.args.seed)
"""