#/bin/bash

for zone in $(aws route53 list-hosted-zones|jq .HostedZones[].Id|cut -d / -f3|tr -d '"'); do aws route53 list-resource-record-sets --hosted-zone-id $zone; done > /tmp/tempdns

cat /tmp/tempdns | jq -r '.ResourceRecordSets[] | [.Name, .Type, (.ResourceRecords[]? | .Value), .AliasTarget.DNSName?] | @tsv'

