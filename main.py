import argparse
import sys
from pathlib import Path

import twitter


def parse_config(config_file=None):
    if config_file is None:
        config_file = Path.home() / '.twitter.cfg'
    config_text = config_file.read_text()
    lines = config_text.split('\n')
    config_obj = {}
    for line in lines:
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
    parser.add_argument('text')
    args = parser.parse_args()
    config = parse_config(Path(str(args.config)) if args.config else None)
    api = login(config)
    text = args.text
    if not text:
        print('Missing a tweet text', file=sys.stderr)
        sys.exit(1)
    status: twitter.Status = api.PostUpdate(text)
    print(status.AsJsonString())
