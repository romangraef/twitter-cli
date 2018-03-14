# twitter-cli
a simple twitter cli. May add features but you know how side projects go..
Helele, just kidding. :p

## Tweet via commandline
```bash
$ tweet "Hello, World"
# tweets stuff
$ tweet -v "hello, world"
# response dump in json format
```

## Installation
- Clone and run `./install.sh`
- create an application over at [Twitter Apps][twitterapps]
- click on manage keys
- generate access tokens
- copy tokens in the `~/.twitter.cfg`
- important: NO EMPTY LINES. This will likely be changed in future versions but currently it breaks the script
example:
```properties
consumer_key=XXXXXX
consumer_secret=XXXXXX
access_token_key=XXXXXX
access_token_secret=XXXXXX
```



[twitterapps]: https://apps.twitter.com/
