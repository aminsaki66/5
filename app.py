import pybase64
import requests

def decode_base64(encoded):
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded).decode(encoding)
            break
        except:
            pass
    return decoded

def generate_v2ray_configs(decoded_data):

    configs = []

    for i, data in enumerate(decoded_data):
        config = data
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs

def decode_links(links):
    decoded_data = []

    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)

    sorted_configs = generate_v2ray_configs(decoded_data)

    return sorted_configs

def decode_dir_links(dir_links):
    decoded_dir_links = []

    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)

    return decoded_dir_links

links = [
    'https://sub.EndOfTheLine.cloud/subscribe?tkn=fd82ce20d1c10d1e204fab31c',
    'https://hero.wlf.beauty/api/v1/client/subscribe?token=e06ee2e5fc3f37afe2b44fd4c845be12'
]
dir_links = [
    'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config'
]
decoded_links = decode_links(links)
decoded_dir_links = decode_dir_links(dir_links)
merged_configs = decoded_links + decoded_dir_links
with open("configs.txt", "w") as f:
    f.write(", ".join(merged_configs))
