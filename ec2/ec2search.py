#!/usr/bin/python

import os.path 
import sys
import boto.ec2

if len(sys.argv) < 2: 
    print "Usage %s <query -> instance_name or app> <env>" % os.path.split(sys.argv[0])[1]
    raise SystemExit

busqueda=sys.argv[1]
environment=""
if len(sys.argv)>2:
    environment=sys.argv[2]

print "searching %s in env: %s" % (busqueda, environment or "none")
conn = boto.ec2.connect_to_region('us-east-1')

#get the instances 
instances = [x for y in conn.get_all_instances() for x in y.instances]

#get the result
pre_res = [x for x in instances if busqueda in x.id or busqueda in x.tags.get('Name','') or busqueda in x.tags.get('app','')]

#check the environment
if environment:
    res = [x for x in pre_res if x.tags.get('Environment') == environment]
else:
    res = pre_res

if res and len(res):
    for instance in res:
        print "%s %s %s app->%s env->%s" % (	instance.id, instance.private_ip_address,
                                                    instance.tags.get('Name',' '),
                                                    instance.tags.get('app','No APP'),
                                                    instance.tags.get('Environment', 'No Env') )
else:
    print "nothing match"


