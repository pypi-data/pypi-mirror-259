# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetCloudBackupSnapshotRestoreJobResult',
    'AwaitableGetCloudBackupSnapshotRestoreJobResult',
    'get_cloud_backup_snapshot_restore_job',
    'get_cloud_backup_snapshot_restore_job_output',
]

@pulumi.output_type
class GetCloudBackupSnapshotRestoreJobResult:
    """
    A collection of values returned by getCloudBackupSnapshotRestoreJob.
    """
    def __init__(__self__, cancelled=None, cluster_name=None, created_at=None, delivery_type=None, delivery_urls=None, expired=None, expires_at=None, finished_at=None, id=None, job_id=None, oplog_inc=None, oplog_ts=None, point_in_time_utc_seconds=None, project_id=None, snapshot_id=None, target_cluster_name=None, target_project_id=None, timestamp=None):
        if cancelled and not isinstance(cancelled, bool):
            raise TypeError("Expected argument 'cancelled' to be a bool")
        pulumi.set(__self__, "cancelled", cancelled)
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if delivery_type and not isinstance(delivery_type, str):
            raise TypeError("Expected argument 'delivery_type' to be a str")
        pulumi.set(__self__, "delivery_type", delivery_type)
        if delivery_urls and not isinstance(delivery_urls, list):
            raise TypeError("Expected argument 'delivery_urls' to be a list")
        pulumi.set(__self__, "delivery_urls", delivery_urls)
        if expired and not isinstance(expired, bool):
            raise TypeError("Expected argument 'expired' to be a bool")
        pulumi.set(__self__, "expired", expired)
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        pulumi.set(__self__, "expires_at", expires_at)
        if finished_at and not isinstance(finished_at, str):
            raise TypeError("Expected argument 'finished_at' to be a str")
        pulumi.set(__self__, "finished_at", finished_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if job_id and not isinstance(job_id, str):
            raise TypeError("Expected argument 'job_id' to be a str")
        pulumi.set(__self__, "job_id", job_id)
        if oplog_inc and not isinstance(oplog_inc, int):
            raise TypeError("Expected argument 'oplog_inc' to be a int")
        pulumi.set(__self__, "oplog_inc", oplog_inc)
        if oplog_ts and not isinstance(oplog_ts, int):
            raise TypeError("Expected argument 'oplog_ts' to be a int")
        pulumi.set(__self__, "oplog_ts", oplog_ts)
        if point_in_time_utc_seconds and not isinstance(point_in_time_utc_seconds, int):
            raise TypeError("Expected argument 'point_in_time_utc_seconds' to be a int")
        pulumi.set(__self__, "point_in_time_utc_seconds", point_in_time_utc_seconds)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if target_cluster_name and not isinstance(target_cluster_name, str):
            raise TypeError("Expected argument 'target_cluster_name' to be a str")
        pulumi.set(__self__, "target_cluster_name", target_cluster_name)
        if target_project_id and not isinstance(target_project_id, str):
            raise TypeError("Expected argument 'target_project_id' to be a str")
        pulumi.set(__self__, "target_project_id", target_project_id)
        if timestamp and not isinstance(timestamp, str):
            raise TypeError("Expected argument 'timestamp' to be a str")
        pulumi.set(__self__, "timestamp", timestamp)

    @property
    @pulumi.getter
    def cancelled(self) -> bool:
        """
        Indicates whether the restore job was canceled.
        """
        return pulumi.get(self, "cancelled")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        UTC ISO 8601 formatted point in time when Atlas created the restore job.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deliveryType")
    def delivery_type(self) -> str:
        """
        Type of restore job to create. Possible values are: automated and download.
        """
        return pulumi.get(self, "delivery_type")

    @property
    @pulumi.getter(name="deliveryUrls")
    def delivery_urls(self) -> Sequence[str]:
        """
        One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.
        """
        return pulumi.get(self, "delivery_urls")

    @property
    @pulumi.getter
    def expired(self) -> bool:
        """
        Indicates whether the restore job expired.
        """
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> str:
        """
        UTC ISO 8601 formatted point in time when the restore job expires.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> str:
        """
        UTC ISO 8601 formatted point in time when the restore job completed.
        """
        return pulumi.get(self, "finished_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> str:
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter(name="oplogInc")
    def oplog_inc(self) -> int:
        return pulumi.get(self, "oplog_inc")

    @property
    @pulumi.getter(name="oplogTs")
    def oplog_ts(self) -> int:
        return pulumi.get(self, "oplog_ts")

    @property
    @pulumi.getter(name="pointInTimeUtcSeconds")
    def point_in_time_utc_seconds(self) -> int:
        return pulumi.get(self, "point_in_time_utc_seconds")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> str:
        """
        Unique identifier of the source snapshot ID of the restore job.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="targetClusterName")
    def target_cluster_name(self) -> str:
        """
        Name of the target Atlas cluster to which the restore job restores the snapshot. Only visible if deliveryType is automated.
        """
        return pulumi.get(self, "target_cluster_name")

    @property
    @pulumi.getter(name="targetProjectId")
    def target_project_id(self) -> str:
        """
        Name of the target Atlas project of the restore job. Only visible if deliveryType is automated.
        """
        return pulumi.get(self, "target_project_id")

    @property
    @pulumi.getter
    def timestamp(self) -> str:
        """
        Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.
        """
        return pulumi.get(self, "timestamp")


class AwaitableGetCloudBackupSnapshotRestoreJobResult(GetCloudBackupSnapshotRestoreJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudBackupSnapshotRestoreJobResult(
            cancelled=self.cancelled,
            cluster_name=self.cluster_name,
            created_at=self.created_at,
            delivery_type=self.delivery_type,
            delivery_urls=self.delivery_urls,
            expired=self.expired,
            expires_at=self.expires_at,
            finished_at=self.finished_at,
            id=self.id,
            job_id=self.job_id,
            oplog_inc=self.oplog_inc,
            oplog_ts=self.oplog_ts,
            point_in_time_utc_seconds=self.point_in_time_utc_seconds,
            project_id=self.project_id,
            snapshot_id=self.snapshot_id,
            target_cluster_name=self.target_cluster_name,
            target_project_id=self.target_project_id,
            timestamp=self.timestamp)


def get_cloud_backup_snapshot_restore_job(cluster_name: Optional[str] = None,
                                          job_id: Optional[str] = None,
                                          project_id: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudBackupSnapshotRestoreJobResult:
    """
    `CloudBackupSnapshotRestoreJob` provides a Cloud Backup Snapshot Restore Job datasource. Gets all the cloud backup snapshot restore jobs for the specified cluster.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.


    :param str cluster_name: The name of the Atlas cluster for which you want to retrieve the restore job.
    :param str job_id: The unique identifier of the restore job to retrieve.
    :param str project_id: The unique identifier of the project for the Atlas cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['jobId'] = job_id
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getCloudBackupSnapshotRestoreJob:getCloudBackupSnapshotRestoreJob', __args__, opts=opts, typ=GetCloudBackupSnapshotRestoreJobResult).value

    return AwaitableGetCloudBackupSnapshotRestoreJobResult(
        cancelled=pulumi.get(__ret__, 'cancelled'),
        cluster_name=pulumi.get(__ret__, 'cluster_name'),
        created_at=pulumi.get(__ret__, 'created_at'),
        delivery_type=pulumi.get(__ret__, 'delivery_type'),
        delivery_urls=pulumi.get(__ret__, 'delivery_urls'),
        expired=pulumi.get(__ret__, 'expired'),
        expires_at=pulumi.get(__ret__, 'expires_at'),
        finished_at=pulumi.get(__ret__, 'finished_at'),
        id=pulumi.get(__ret__, 'id'),
        job_id=pulumi.get(__ret__, 'job_id'),
        oplog_inc=pulumi.get(__ret__, 'oplog_inc'),
        oplog_ts=pulumi.get(__ret__, 'oplog_ts'),
        point_in_time_utc_seconds=pulumi.get(__ret__, 'point_in_time_utc_seconds'),
        project_id=pulumi.get(__ret__, 'project_id'),
        snapshot_id=pulumi.get(__ret__, 'snapshot_id'),
        target_cluster_name=pulumi.get(__ret__, 'target_cluster_name'),
        target_project_id=pulumi.get(__ret__, 'target_project_id'),
        timestamp=pulumi.get(__ret__, 'timestamp'))


@_utilities.lift_output_func(get_cloud_backup_snapshot_restore_job)
def get_cloud_backup_snapshot_restore_job_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                                 job_id: Optional[pulumi.Input[str]] = None,
                                                 project_id: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudBackupSnapshotRestoreJobResult]:
    """
    `CloudBackupSnapshotRestoreJob` provides a Cloud Backup Snapshot Restore Job datasource. Gets all the cloud backup snapshot restore jobs for the specified cluster.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.


    :param str cluster_name: The name of the Atlas cluster for which you want to retrieve the restore job.
    :param str job_id: The unique identifier of the restore job to retrieve.
    :param str project_id: The unique identifier of the project for the Atlas cluster.
    """
    ...
