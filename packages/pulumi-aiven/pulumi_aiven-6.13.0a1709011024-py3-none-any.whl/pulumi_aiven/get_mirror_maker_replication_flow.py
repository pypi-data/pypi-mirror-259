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
    'GetMirrorMakerReplicationFlowResult',
    'AwaitableGetMirrorMakerReplicationFlowResult',
    'get_mirror_maker_replication_flow',
    'get_mirror_maker_replication_flow_output',
]

@pulumi.output_type
class GetMirrorMakerReplicationFlowResult:
    """
    A collection of values returned by getMirrorMakerReplicationFlow.
    """
    def __init__(__self__, emit_backward_heartbeats_enabled=None, emit_heartbeats_enabled=None, enable=None, id=None, offset_syncs_topic_location=None, project=None, replication_policy_class=None, service_name=None, source_cluster=None, sync_group_offsets_enabled=None, sync_group_offsets_interval_seconds=None, target_cluster=None, topics=None, topics_blacklists=None):
        if emit_backward_heartbeats_enabled and not isinstance(emit_backward_heartbeats_enabled, bool):
            raise TypeError("Expected argument 'emit_backward_heartbeats_enabled' to be a bool")
        pulumi.set(__self__, "emit_backward_heartbeats_enabled", emit_backward_heartbeats_enabled)
        if emit_heartbeats_enabled and not isinstance(emit_heartbeats_enabled, bool):
            raise TypeError("Expected argument 'emit_heartbeats_enabled' to be a bool")
        pulumi.set(__self__, "emit_heartbeats_enabled", emit_heartbeats_enabled)
        if enable and not isinstance(enable, bool):
            raise TypeError("Expected argument 'enable' to be a bool")
        pulumi.set(__self__, "enable", enable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if offset_syncs_topic_location and not isinstance(offset_syncs_topic_location, str):
            raise TypeError("Expected argument 'offset_syncs_topic_location' to be a str")
        pulumi.set(__self__, "offset_syncs_topic_location", offset_syncs_topic_location)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if replication_policy_class and not isinstance(replication_policy_class, str):
            raise TypeError("Expected argument 'replication_policy_class' to be a str")
        pulumi.set(__self__, "replication_policy_class", replication_policy_class)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if source_cluster and not isinstance(source_cluster, str):
            raise TypeError("Expected argument 'source_cluster' to be a str")
        pulumi.set(__self__, "source_cluster", source_cluster)
        if sync_group_offsets_enabled and not isinstance(sync_group_offsets_enabled, bool):
            raise TypeError("Expected argument 'sync_group_offsets_enabled' to be a bool")
        pulumi.set(__self__, "sync_group_offsets_enabled", sync_group_offsets_enabled)
        if sync_group_offsets_interval_seconds and not isinstance(sync_group_offsets_interval_seconds, int):
            raise TypeError("Expected argument 'sync_group_offsets_interval_seconds' to be a int")
        pulumi.set(__self__, "sync_group_offsets_interval_seconds", sync_group_offsets_interval_seconds)
        if target_cluster and not isinstance(target_cluster, str):
            raise TypeError("Expected argument 'target_cluster' to be a str")
        pulumi.set(__self__, "target_cluster", target_cluster)
        if topics and not isinstance(topics, list):
            raise TypeError("Expected argument 'topics' to be a list")
        pulumi.set(__self__, "topics", topics)
        if topics_blacklists and not isinstance(topics_blacklists, list):
            raise TypeError("Expected argument 'topics_blacklists' to be a list")
        pulumi.set(__self__, "topics_blacklists", topics_blacklists)

    @property
    @pulumi.getter(name="emitBackwardHeartbeatsEnabled")
    def emit_backward_heartbeats_enabled(self) -> bool:
        """
        Whether to emit heartbeats to the direction opposite to the flow, i.e. to the source cluster. The default value is `false`.
        """
        return pulumi.get(self, "emit_backward_heartbeats_enabled")

    @property
    @pulumi.getter(name="emitHeartbeatsEnabled")
    def emit_heartbeats_enabled(self) -> bool:
        """
        Whether to emit heartbeats to the target cluster. The default value is `false`.
        """
        return pulumi.get(self, "emit_heartbeats_enabled")

    @property
    @pulumi.getter
    def enable(self) -> bool:
        """
        Enable of disable replication flows for a service.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="offsetSyncsTopicLocation")
    def offset_syncs_topic_location(self) -> str:
        """
        Offset syncs topic location.
        """
        return pulumi.get(self, "offset_syncs_topic_location")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="replicationPolicyClass")
    def replication_policy_class(self) -> str:
        """
        Replication policy class. The possible values are `org.apache.kafka.connect.mirror.DefaultReplicationPolicy` and `org.apache.kafka.connect.mirror.IdentityReplicationPolicy`. The default value is `org.apache.kafka.connect.mirror.DefaultReplicationPolicy`.
        """
        return pulumi.get(self, "replication_policy_class")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="sourceCluster")
    def source_cluster(self) -> str:
        """
        Source cluster alias. Maximum length: `128`.
        """
        return pulumi.get(self, "source_cluster")

    @property
    @pulumi.getter(name="syncGroupOffsetsEnabled")
    def sync_group_offsets_enabled(self) -> bool:
        """
        Sync consumer group offsets. The default value is `false`.
        """
        return pulumi.get(self, "sync_group_offsets_enabled")

    @property
    @pulumi.getter(name="syncGroupOffsetsIntervalSeconds")
    def sync_group_offsets_interval_seconds(self) -> int:
        """
        Frequency of consumer group offset sync. The default value is `1`.
        """
        return pulumi.get(self, "sync_group_offsets_interval_seconds")

    @property
    @pulumi.getter(name="targetCluster")
    def target_cluster(self) -> str:
        """
        Target cluster alias. Maximum length: `128`.
        """
        return pulumi.get(self, "target_cluster")

    @property
    @pulumi.getter
    def topics(self) -> Sequence[str]:
        """
        List of topics and/or regular expressions to replicate
        """
        return pulumi.get(self, "topics")

    @property
    @pulumi.getter(name="topicsBlacklists")
    def topics_blacklists(self) -> Sequence[str]:
        """
        List of topics and/or regular expressions to not replicate.
        """
        return pulumi.get(self, "topics_blacklists")


class AwaitableGetMirrorMakerReplicationFlowResult(GetMirrorMakerReplicationFlowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMirrorMakerReplicationFlowResult(
            emit_backward_heartbeats_enabled=self.emit_backward_heartbeats_enabled,
            emit_heartbeats_enabled=self.emit_heartbeats_enabled,
            enable=self.enable,
            id=self.id,
            offset_syncs_topic_location=self.offset_syncs_topic_location,
            project=self.project,
            replication_policy_class=self.replication_policy_class,
            service_name=self.service_name,
            source_cluster=self.source_cluster,
            sync_group_offsets_enabled=self.sync_group_offsets_enabled,
            sync_group_offsets_interval_seconds=self.sync_group_offsets_interval_seconds,
            target_cluster=self.target_cluster,
            topics=self.topics,
            topics_blacklists=self.topics_blacklists)


def get_mirror_maker_replication_flow(project: Optional[str] = None,
                                      service_name: Optional[str] = None,
                                      source_cluster: Optional[str] = None,
                                      target_cluster: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMirrorMakerReplicationFlowResult:
    """
    The MirrorMaker 2 Replication Flow data source provides information about the existing MirrorMaker 2 Replication Flow on Aiven Cloud.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    f1 = aiven.get_mirror_maker_replication_flow(project=aiven_project["kafka-mm-project1"]["project"],
        service_name=aiven_kafka["mm"]["service_name"],
        source_cluster=aiven_kafka["source"]["service_name"],
        target_cluster=aiven_kafka["target"]["service_name"])
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str source_cluster: Source cluster alias. Maximum length: `128`.
    :param str target_cluster: Target cluster alias. Maximum length: `128`.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['serviceName'] = service_name
    __args__['sourceCluster'] = source_cluster
    __args__['targetCluster'] = target_cluster
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getMirrorMakerReplicationFlow:getMirrorMakerReplicationFlow', __args__, opts=opts, typ=GetMirrorMakerReplicationFlowResult).value

    return AwaitableGetMirrorMakerReplicationFlowResult(
        emit_backward_heartbeats_enabled=pulumi.get(__ret__, 'emit_backward_heartbeats_enabled'),
        emit_heartbeats_enabled=pulumi.get(__ret__, 'emit_heartbeats_enabled'),
        enable=pulumi.get(__ret__, 'enable'),
        id=pulumi.get(__ret__, 'id'),
        offset_syncs_topic_location=pulumi.get(__ret__, 'offset_syncs_topic_location'),
        project=pulumi.get(__ret__, 'project'),
        replication_policy_class=pulumi.get(__ret__, 'replication_policy_class'),
        service_name=pulumi.get(__ret__, 'service_name'),
        source_cluster=pulumi.get(__ret__, 'source_cluster'),
        sync_group_offsets_enabled=pulumi.get(__ret__, 'sync_group_offsets_enabled'),
        sync_group_offsets_interval_seconds=pulumi.get(__ret__, 'sync_group_offsets_interval_seconds'),
        target_cluster=pulumi.get(__ret__, 'target_cluster'),
        topics=pulumi.get(__ret__, 'topics'),
        topics_blacklists=pulumi.get(__ret__, 'topics_blacklists'))


@_utilities.lift_output_func(get_mirror_maker_replication_flow)
def get_mirror_maker_replication_flow_output(project: Optional[pulumi.Input[str]] = None,
                                             service_name: Optional[pulumi.Input[str]] = None,
                                             source_cluster: Optional[pulumi.Input[str]] = None,
                                             target_cluster: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMirrorMakerReplicationFlowResult]:
    """
    The MirrorMaker 2 Replication Flow data source provides information about the existing MirrorMaker 2 Replication Flow on Aiven Cloud.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    f1 = aiven.get_mirror_maker_replication_flow(project=aiven_project["kafka-mm-project1"]["project"],
        service_name=aiven_kafka["mm"]["service_name"],
        source_cluster=aiven_kafka["source"]["service_name"],
        target_cluster=aiven_kafka["target"]["service_name"])
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str source_cluster: Source cluster alias. Maximum length: `128`.
    :param str target_cluster: Target cluster alias. Maximum length: `128`.
    """
    ...
