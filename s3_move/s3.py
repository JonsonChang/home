# from boto import boto
import boto
import boto.s3.connection
from boto.exception import *

access_key = 'IPXVTM9H632ADEBDQ644'
secret_key = 'q0xfxbBEjS+Xn4oTyY7e/fPg7Ns6vsIa+UN3NZ/1'

conn = boto.s3.connection.S3Connection(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    host='arkflex1',
    port=8080,
    #     debug=1,
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)


dist_access_key = 'SGDX73GMJVRM0888MJ76'
dist_secret_key = 'GtXd3mNF8J0rRytQzahlLOLGnt/VHMnJYc/iXVcI'

dist_conn = boto.s3.connection.S3Connection(
    aws_access_key_id=dist_access_key,
    aws_secret_access_key=dist_secret_key,
    host='arkflex2',
    port=8080,
    #     debug=1,
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)


def mycb(so_far, total):
    print '\t%d bytes transferred out of %d' % (so_far, total)


def createBucket(aconn, bucketName):
    bucket = None
    bucketName = "dist_" + bucketName
#     print "createBucket : {0} {1}".format(aconn, bucketName)
    try:
        bucket = aconn.create_bucket(bucketName)
    except S3CreateError:
        print "bucket name already exist"
    return bucket

for bucket in conn.get_all_buckets():
    print "{name}\t\t\t\t{created}".format(
        name=bucket.name,
        created=bucket.creation_date,
    )
    dist_bucket = createBucket(dist_conn, bucket.name)

    if dist_bucket:
        for key in bucket.list():
            print "{name}\t{size}\t{modified}".format(
                name=key.name.encode('utf-8'),
                size=key.size,
                modified=key.last_modified,
            )
            print "\t downloading"
            key.BufferSize = 20480
            key.get_contents_to_filename("/tmp/a", cb=mycb, num_cb=10)
            print "\t uploading"
            dist_key = dist_bucket.new_key(key.name.encode('utf-8'))
            dist_key.BufferSize = 20480
            dist_key.set_contents_from_filename(filename="/tmp/a", replace=True, cb=mycb, num_cb=10)
            print "\t done"


print "==============="
