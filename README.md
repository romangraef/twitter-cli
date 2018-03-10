# twitter-cli
a simple twitter cli. may add features but you know how side projects go..

## Tweet via commandline
```bash
$ tweet "Hello, World"
# tweets stuff
$ tweet -v "hello, world"
# response dump in json format
```

## Installation
- Clone and run `./install.sh`
- create an application over at [twitter apps][twitterapps]
- click on manage keys
- generate access tokens
- copy tokens in the `~/.twitter.cfg`
- important: NO EMPTY LINES. this will likely be changed in feature versions but currently breaks stuff
example:
```properties
consumer_key=XXXXXX
consumer_secret=XXXXXX
access_token_key=XXXXXX
access_token_secret=XXXXXX
```



[twitterapps]: https://apps.twitter.com/
