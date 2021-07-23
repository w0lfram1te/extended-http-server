# Extended Python Server

This extends the basic functionalities of the basic Python3 `http.server` module.

Currently supported methods: `GET`, `HEAD`, and `PUT`.

## Usage

```
usage: ehttpserver.py [-h] [-b BIND] [-p PORT] [port]

Extended HTTP Server by w0lfram1te

positional arguments:
  port                  listening port

optional arguments:
  -h, --help            show this help message and exit
  -b BIND, --bind BIND  bind address
  -p PORT, --port PORT  listening port
```

Quick usage: This will download the file and launch the server on port 8000 and will listen on all interfaces by default.

```bash
wget https://raw.githubusercontent.com/w0lfram1te/extended-http-server/main/ehttpserver.py
python3 ehttpserver.py
```
