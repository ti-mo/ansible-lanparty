# lp-prometheus
Deploys a prometheus server with a complimentrary alertmanager

## Config
At this moment not everything is automated, but I provided a full prometheus.yml template
in which you can edit the things you want/don't need.

Needed in inventory based on the template:

```
[docker]
# docker_hosts with docker_exporters installed on them - provides container metrics

[monitoring:children]
prometheus
alertmanager

[prometheus]
# Prometheus hosts - get all metrics from all prometheus hosts in the network

[alertmanager]
# Alertmanager hosts - get all metrics from all alertmanager hosts in the network

[network-devices] # devices on the network
# All devices you wanna ping to, requires blackbox_exporter

[ping-targets]    # sites to ping to
# Additional outside websites, seperate because they can also be used by other blackbox
# modules

[snmp-targets]
# Hosts you want snmp from - requires that snmp_exporter is running somewhere

[nodes]
# Machines with node_exporter running on them
```
