.PHONY: cert curl describe-cert server

cert:
	openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

describe-cert:
	openssl x509 -in cert.pem -text -noout

curl:
	curl -v --cacert cert.pem --resolve website.localhost:8000:127.0.0.1 https://website.localhost:8000

server:
	python3 server.py
