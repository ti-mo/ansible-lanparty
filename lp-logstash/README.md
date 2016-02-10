lp-logstash
===========

LogStash Book
-------------
- [Extremely useful documentation](http://www.logstashbook.com/TheLogstashBook_sample.pdf)
- [Advanced LogStash Setup](http://www.networkassassin.com/elk-for-network-operations)
- [Grok Patterns](http://alfredocambera.blogspot.be/2013/02/logstash-grok-patterns-and-nginx-access.html)
- [LogStash Indexes](https://ruin.io/2015/multiple-elasticsearch-indices-logstash/)
- [DigitalOcean - ELK Part 1](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-4-on-ubuntu-14-04)
- [DigitalOcean - ELK Part 2](https://www.digitalocean.com/community/tutorials/adding-logstash-filters-to-improve-centralized-logging)
- [GeoIP Usage in LogStash](https://www.digitalocean.com/community/tutorials/how-to-map-user-location-with-geoip-and-elk-elasticsearch-logstash-and-kibana)

Generating SSL Certs
--------------------
SSL is mandatory for logstash-forwarder. In `files/keys/logstash`:

```
openssl req -subj '/CN=zl-log.zanzi.lan/' -x509 -days 3650 -batch -nodes -newkey rsa:2048 -keyout logstash-forwarder.key -out logstash-forwarder.crt
```
