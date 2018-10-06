import argparse
import sys
from pathlib import Path

import twitter
from os import system


def parse_config(config_file=None):
    if config_file is None:
        config_file = Path.home() / '.twitter.cfg'
    config_text = config_file.read_text()
    lines = config_text.split('\n')
    config_obj = {}
    for line in lines:
        if line:
            parts = line.split('=')
            config_obj[parts[0]] = parts[1]
    return config_obj


def login(config):
    api = twitter.Api(
        **config
    )
    api.VerifyCredentials()
    return api


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='tweet')
    parser.add_argument('--config', dest='config', type=argparse.FileType('r'))
    parser.add_argument('--image', dest='image', type=argparse.FileType('rb'))
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true')
    parser.add_argument('text')
    args = parser.parse_args()
    config = parse_config(Path(str(args.config)) if args.config else None)
    api = login(config)
    text = args.text
    img = args.image
    if text.lower() == "tobi69is69gay":
        system('espeak "dance on a pink rainbow with me"')
        sys.exit(69)
    elif text.lower() == "hallo":
        system('espeak "HELLO DARKNESS MY OLD FRIEND!"')
        sys.exit(69)
    if not text:
        print('Missing a tweet text', file=sys.stderr)
        sys.exit(1)
    status: twitter.Status = api.PostUpdate(text, media=img)
    if args.verbose:
        print(status.AsJsonString())
