import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snap in snapshots:
        snapshot_id = snap['SnapshotId']
        volume_id = snap.get('VolumeId')

        if not volume_id:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id} (no volume attached).")
            continue
        try:
            volume_info = ec2.describe_volumes(VolumeIds=[volume_id])
            attachments = volume_info['Volumes'][0].get('Attachments',[])

            if not attachments:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id} (volume {volume_id} not attached).)")

        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id} (volume {volume_id} not found).)")

                


