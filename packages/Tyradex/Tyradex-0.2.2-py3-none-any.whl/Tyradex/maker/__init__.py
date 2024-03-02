import json
import os
import pathlib
import platform
import sys

import requests
from PIL import Image

from Tyradex.errors import DataNotFoundError, ServerError

BASE_API = "https://tyradex.tech/api/v1/"


def call(endpoint: str, *, force=False, **params: str) -> dict:
    def request():
        clean_params = {key: value for key, value in params.items() if value is not ...}
        url = (
                BASE_API +
                endpoint +
                (
                    "?" + "&".join([
                        f"{key}={value}"
                        for key, value in clean_params.items()
                    ])
                    if len(clean_params) > 0 else
                    ""
                )
        )
        req = requests.get(
            url,
            headers={
                "User-Agent": f"Tyradex/2.0 ("
                              f"{platform.uname().system} "
                              f"{platform.uname().release} "
                              f"{platform.uname().version}; "
                              f"{platform.uname().machine}"
                              f") "
                              f"Python/{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} "
                              f"Node/{platform.uname().node}"
            }
        )
        save(req)
        return req.json()

    dir_cache = os.path.expanduser('~').replace('\\', '/') + "/Tyradex/.cache/json"

    path = pathlib.Path(dir_cache, endpoint + '.json')
    if not path.exists():
        data = request()
    else:
        with open(path) as fp:
            data = json.load(fp)
    match data:
        case {'status': int, 'message': str}:
            raise DataNotFoundError(data['message'])
        case {'message': str}:
            raise ServerError(data['message'])
        case _:
            return data


def call_image(endpoint: str, *, force=False) -> Image.Image:
    base = "https://raw.githubusercontent.com/Yarkis01/TyraDex/images/"

    def request():
        save(requests.get(
            base + endpoint,
            headers={
                "User-Agent": f"Tyradex/2.0 ("
                              f"{platform.uname().system} "
                              f"{platform.uname().release} "
                              f"{platform.uname().version}; "
                              f"{platform.uname().machine}"
                              f") "
                              f"Python/{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} "
                              f"Node/{platform.uname().node}"
            })
        )

    if endpoint.startswith(base):
        endpoint = endpoint.removeprefix(base)

    if not endpoint.endswith('.png'):
        endpoint += '.png'

    dir_cache = os.path.expanduser('~').replace('\\', '/') + "/Tyradex/.cache/images"

    path = pathlib.Path(dir_cache, endpoint)
    if not path.exists() or force:
        request()
    with Image.open(path) as IMG:
        img = IMG.copy()
    return img


def special_call_image(endpoint1: str, endpoint2: str, *, force=False) -> Image:
    base = "https://raw.githubusercontent.com/Yarkis01/TyraDex/images/"

    endpoint = '/'.join(endpoint1.split('/')[:-1])
    if endpoint.startswith(base):
        endpoint = endpoint.removeprefix(base)

    dir_cache = os.path.expanduser('~').replace('\\', '/') + "/Tyradex/.cache/images"

    name = endpoint1.split('/')[-1].split('.')[0] + '_' + endpoint2.split('/')[-1].split('.')[0]

    target_image = pathlib.Path(dir_cache, endpoint, name + '.png')

    if not target_image.exists() or force:
        return concat(call_image(endpoint1), call_image(endpoint2), name, void=0.15)
    with Image.open(target_image) as IMG:
        img = IMG.copy()
    return img


def save(response: requests.Response):
    directory = os.path.expanduser('~').replace('\\', '/')
    path = "/Tyradex/.cache"
    if response.url.endswith('.png'):
        path += response.url.removeprefix("https://raw.githubusercontent.com/Yarkis01/TyraDex")
        pathlib.Path(directory + path).parent.mkdir(parents=True, exist_ok=True)
        with open(directory + path, 'wb') as fp:
            fp.write(response.content)

    else:
        match response.json():
            case {'status': int, 'message': str}:
                pass
            case {'message': str}:
                pass
            case _:
                path += "/json/" + response.url.removeprefix(BASE_API) + '.json'
                pathlib.Path(directory + path).parent.mkdir(parents=True, exist_ok=True)
                with open(directory + path, 'w') as fp:
                    json.dump(response.json(), fp, indent=2)

    return directory + path


def concat(image1, image2, filename, *, save_it=True, void: float = 0):
    """Concatenate two images using PIL.Image

    :param image1: First image.
    :type image1: Image.Image
    :param image2: Second image.
    :type image2: Image.Image
    :param filename: Filename to save the concatenated
    :type filename: str
    :param save_it: Do you want save it? (default: True)
    :type save_it: bool
    :param void: The percentage of length of the void between the two image
    
    :return: The two images concatenated
    :rtype: Image.Image
    """
    void_length = round(((image1.width + image2.width) // 2) * void)

    image3 = Image.new("RGBA", (
        image1.width + image2.width + void_length,
        image1.height
    ))

    for x in range(image1.size[0]):
        for y in range(image1.size[1]):
            image3.putpixel((x, y), image1.getpixel((x, y)))

    for x in range(image2.size[0]):
        for y in range(image2.size[1]):
            image3.putpixel((image1.width + void_length + x, y), image2.getpixel((x, y)))

    if save_it:
        image3.save(f"C:/Users/Picsel/Tyradex/.cache/images/types/{filename}.png")
    return image3
