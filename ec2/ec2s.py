#!/usr/bin/env python
# coding=utf-8

import argparse
import boto.ec2


def connect_aws(profile, ec2_region):
    return boto.ec2.connect_to_region(profile_name=profile, region_name=ec2_region)


def instance_get_ip(instance):
    return instance.private_ip_address if instance.private_ip_address else instance.ip_address


def print_instances(connect, search):
    instances = connect.get_only_instances(instance_ids=None,
                                           filters={'tag:Name': search, 'instance-state-name': "running"})
    for instance in instances:
        ip = instance_get_ip(instance)
        print "%-30s %-20s" % (instance.tags["Name"], ip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('account', help='Your account credentials (from ~/.aws/credentials)')
    parser.add_argument('regions', help='Comma separated regions to look for')
    parser.add_argument('--search', help='Comma separated regions to look for', default='*')
    args = parser.parse_args()

    regions = args.regions.split(',')

    for region in regions:
        print '☂  ' + region.upper() + ' SERVERS ------------------------------'
print_instances(connect_aws(args.account, region), args.search)
