import boto3 
import urllib2
import ast
from datetime import date

region = 'us-east-1'
source_account = 'XXXXXXXXXXXX'

route53 = boto3.client('route53')
s3 = boto3.resource('s3')

zones = route53.list_hosted_zones()['HostedZones']

for zone in zones:        
    zone_name = zone['Name']
    print zone_name
    print "========="
    zone_id = route53.get_hosted_zone(Id=zone['Id'])
    newzone = zone_id['HostedZone']['Id']
    all_rrs = [];
    zone_rr = route53.list_resource_record_sets(HostedZoneId=newzone)
    next_record = None

    for rr in zone_rr['ResourceRecordSets']:
        all_rrs.append(rr)
        print rr

    while zone_rr['IsTruncated'] == True:
        next_record = zone_rr['NextRecordName']
        print next_record
        zone_rr = route53.list_resource_record_sets(HostedZoneId=newzone,StartRecordName=next_record)

        for rr in zone_rr['ResourceRecordSets']:
            all_rrs.append(rr)
            print rr
            #print rr['Name']

    

