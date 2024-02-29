import requests
import yaml
import json
import os

class Client:
    def __new__(cls, url, model_type, endpoint, **kwargs):
        if 'yolov5' in model_type.lower():
            return Yolov5Client(url, model_type, endpoint, **kwargs)
        elif 'sd' in model_type.lower():
            return SDClient(url, model_type, endpoint, **kwargs)
        else:
            return BaseModelClient(url, model_type, endpoint, **kwargs)
        
        
class BaseModelClient:
    def __init__(self, url, model_type, endpoint, **kwargs):
        self.url = url
        self.model_type = model_type
        self.endpoint = endpoint

        self.response = self.process(**kwargs)
        
    def load_models_from_yaml(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        yaml_path = os.path.join(script_dir, '..', 'config', 'models_config.yaml')

        with open(yaml_path, 'r') as file:
            models_data = yaml.safe_load(file)

        return models_data.get('models', [])
    
    def find_model_info(self):
        for model_info in self.models:
            if model_info.get('name') == self.model_type:
                return model_info

        return None
    
    def find_function_info(self, model_info):
        for function_info in model_info.get('functions', []):
            if function_info.get('name') == self.endpoint:
                return function_info

        return None
    
    def process(self,**kwargs):
        raise NotImplementedError("process method must be implemented in subclass")

    def send_request(self, function_info, **kwargs):
        raise NotImplementedError("send_request method must be implemented in subclass")

    
    
class Yolov5Client(BaseModelClient):
    def process(self,**kwargs):
        self.models = self.load_models_from_yaml()
        model_info = self.find_model_info()
        function_info = self.find_function_info(model_info)
        if function_info:
            response = self.send_request(function_info, **kwargs)
            if (response.status_code == 200):
                return response
            else:
                print ("Server Error")
                return response
        else:
            print ("Server Error")
            return response

    def send_request(self, function_info, **kwargs):

        if not self.url.startswith('http://') and not self.url.startswith('https://'):
            url, port = self.url.split(':')[0], self.url.split(':')[1]
            url = 'http://' + url
        url = f"{url}:{port}{function_info.get('endpoint', '')}"

        headers = {
            'accept': function_info.get('accept', '')
        }
        
        payload = {}
        
        img_path = kwargs.get('image_path', None)
        files=[('img',(os.path.basename(img_path),open(img_path,'rb'),'image/jpeg'))]
        
        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=payload,
            files=files
        )

        return response
    
class SDClient(BaseModelClient):
    def process(self,**kwargs):
        self.models = self.load_models_from_yaml()
        model_info = self.find_model_info()
        function_info = self.find_function_info(model_info)
        if function_info:
            response = self.send_request(function_info, **kwargs)
            if (response.status_code == 200):
                return response
            else:
                print ("Server Error")
                return response
        else:
            print ("Server Error")
            return response

    def send_request(self, function_info, **kwargs):

        if not self.url.startswith('http://') and not self.url.startswith('https://'):
            url, port = self.url.split(':')[0], self.url.split(':')[1]
            url = 'http://' + url
        url = f"{url}:{port}{function_info.get('endpoint', '')}"

        headers = {
            'accept': function_info.get('accept', '')
        }
        
        if function_info.get('name') == 'txt2img':
            payload = json.dumps({
                "prompt": kwargs.get('prompt', None),
                "negative_prompt": kwargs.get('negative_prompt', None),
                "height": 768,
                "width": 768,
                "num_inference_steps": 50,
                "guidance_scale": 7.5,
                "eta": 0
                })
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=payload
            )
        elif function_info.get('name') == 'img2img':
            payload = {'data': f'''{{
                "prompt" : {kwargs.get('prompt', None)},
                "negative_prompt" : {kwargs.get('negative_prompt', None)},
                "num_inference_steps" : 35,
                "width" : 512,
                "height": 512,
                "guidance_scale" : 7.5,
                "eta" : 0.0
                }}'''}
            
            img_path = kwargs.get('image_path', None)
            files=[('img',(os.path.basename(img_path),open(img_path,'rb'),'image/jpeg'))]
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=payload,
                files=files
            )
            print ('hel')
        else: #for inpaint
            payload = {'data': f'''{{
                "prompt" : {kwargs.get('prompt', None)},
                "negative_prompt" : {kwargs.get('negative_prompt', None)},
                "num_inference_steps" : 35,
                "width" : 512,
                "height": 512,
                "guidance_scale" : 7.5,
                "eta" : 0.0
                }}'''}
            
            img_path = kwargs.get('image_path', None)
            img_mask_path = kwargs.get('image_mask_path', None)
            files=[('img',(os.path.basename(img_path),open(img_path,'rb'),'application/octet-stream')),
                   ('img_mask',(os.path.basename(img_mask_path),open(img_mask_path,'rb'),'application/octet-stream'))]
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=payload,
                files=files
            )
            print ('aas')
        return response
        