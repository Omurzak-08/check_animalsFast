import requests
import io
from fastapi import HTTPException
from config import config


async def get_prediction(image_bytes: bytes):
    try:
        print('Roboflow кошулду')
        url = config.ROBOFLOW_URL
        files ={
            'file': ('image.jpg', io.BytesIO(image_bytes), 'image.jpg')
        }
        response = requests.post(url, files=files)

        print(response.text)

        if response.status_code == 403:
            raise HTTPException(status_code=403, detail='Roboflow: Доступ запрещен. Проверь API ключ и URL.')

        # if response.status_code != 200:
        #     raise HTTPException(status_code=500, detail='ошибка')

        return {'time answer': response.json()['time'],
                'class': response.json()['predictions'][0]['class'],
                'confidence': response.json()['predictions'][0]['confidence']* 100}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))