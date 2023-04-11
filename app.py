import pybase64
import requests
import binascii


def decode_base64(encoded):
    """
    Decode base64-encoded string to text.

    Args:
        encoded (str): The base64-encoded string to decode.

    Returns:
        str: The decoded text.
    """
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded


def generate_v2ray_configs(decoded_data):
    """
    Sorts V2Ray configs in alphabetical order.

    Args:
        decoded_data (List[str]): A list of V2Ray configs.

    Returns:
        List[str]: A sorted list of V2Ray configs.
    """

    configs = []

    for config in decoded_data:
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs


def decode_links(links):
    """
    Fetches V2Ray subscription links and decodes the contents.

    Args:
        links (List[str]): A list of V2Ray subscription links.

    Returns:
        List[str]: A list of decoded V2Ray configs.
    """

    decoded_data = []

    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)

    sorted_configs = generate_v2ray_configs(decoded_data)

    return sorted_configs


def decode_dir_links(dir_links):
    """
    Fetches V2Ray config files from URLs and returns their contents.

    Args:
        dir_links (List[str]): A list of URLs pointing to V2Ray config files.

    Returns:
        List[str]: A list of V2Ray configs.
    """

    decoded_dir_links = []

    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)

    return decoded_dir_links


def save_merged_configs_to_file(merged_configs, filename):
    """
    Saves merged V2Ray configs to a file.

    Args:
        merged_configs (List[str]): A list of merged V2Ray configs.
        filename (str): The name of the file to save the configs to.
    """

    with open(filename, "w") as f:
        f.write(", ".join(merged_configs))


def main():
    links = [
        'https://raw.githubusercontent.com/Goodbyefiltering/Subscribelinks/main/V2ray%20%20Subscribe/Goodbyefiltering.txt'
    ]
    dir_links = [
        'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
        'https://mrpooya.xyz/api/sansorchi.php',
        'https://mrpooya.xyz/api/shenzo.php',
        'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/vmess.txt',
        'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/trojan.txt',
        'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/ss.txt',
        'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/ssr.txt'
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    merged_configs = decoded_links + decoded_dir_links
    save_merged_configs_to_file(merged_configs, "configs.txt")


if __name__ == "__main__":
    main()
