# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetServiceIntegrationResult',
    'AwaitableGetServiceIntegrationResult',
    'get_service_integration',
    'get_service_integration_output',
]

@pulumi.output_type
class GetServiceIntegrationResult:
    """
    A collection of values returned by getServiceIntegration.
    """
    def __init__(__self__, clickhouse_kafka_user_configs=None, clickhouse_postgresql_user_configs=None, datadog_user_configs=None, destination_endpoint_id=None, destination_service_name=None, external_aws_cloudwatch_metrics_user_configs=None, id=None, integration_id=None, integration_type=None, kafka_connect_user_configs=None, kafka_logs_user_configs=None, kafka_mirrormaker_user_configs=None, logs_user_configs=None, metrics_user_configs=None, project=None, source_endpoint_id=None, source_service_name=None):
        if clickhouse_kafka_user_configs and not isinstance(clickhouse_kafka_user_configs, list):
            raise TypeError("Expected argument 'clickhouse_kafka_user_configs' to be a list")
        pulumi.set(__self__, "clickhouse_kafka_user_configs", clickhouse_kafka_user_configs)
        if clickhouse_postgresql_user_configs and not isinstance(clickhouse_postgresql_user_configs, list):
            raise TypeError("Expected argument 'clickhouse_postgresql_user_configs' to be a list")
        pulumi.set(__self__, "clickhouse_postgresql_user_configs", clickhouse_postgresql_user_configs)
        if datadog_user_configs and not isinstance(datadog_user_configs, list):
            raise TypeError("Expected argument 'datadog_user_configs' to be a list")
        pulumi.set(__self__, "datadog_user_configs", datadog_user_configs)
        if destination_endpoint_id and not isinstance(destination_endpoint_id, str):
            raise TypeError("Expected argument 'destination_endpoint_id' to be a str")
        pulumi.set(__self__, "destination_endpoint_id", destination_endpoint_id)
        if destination_service_name and not isinstance(destination_service_name, str):
            raise TypeError("Expected argument 'destination_service_name' to be a str")
        pulumi.set(__self__, "destination_service_name", destination_service_name)
        if external_aws_cloudwatch_metrics_user_configs and not isinstance(external_aws_cloudwatch_metrics_user_configs, list):
            raise TypeError("Expected argument 'external_aws_cloudwatch_metrics_user_configs' to be a list")
        pulumi.set(__self__, "external_aws_cloudwatch_metrics_user_configs", external_aws_cloudwatch_metrics_user_configs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if integration_id and not isinstance(integration_id, str):
            raise TypeError("Expected argument 'integration_id' to be a str")
        pulumi.set(__self__, "integration_id", integration_id)
        if integration_type and not isinstance(integration_type, str):
            raise TypeError("Expected argument 'integration_type' to be a str")
        pulumi.set(__self__, "integration_type", integration_type)
        if kafka_connect_user_configs and not isinstance(kafka_connect_user_configs, list):
            raise TypeError("Expected argument 'kafka_connect_user_configs' to be a list")
        pulumi.set(__self__, "kafka_connect_user_configs", kafka_connect_user_configs)
        if kafka_logs_user_configs and not isinstance(kafka_logs_user_configs, list):
            raise TypeError("Expected argument 'kafka_logs_user_configs' to be a list")
        pulumi.set(__self__, "kafka_logs_user_configs", kafka_logs_user_configs)
        if kafka_mirrormaker_user_configs and not isinstance(kafka_mirrormaker_user_configs, list):
            raise TypeError("Expected argument 'kafka_mirrormaker_user_configs' to be a list")
        pulumi.set(__self__, "kafka_mirrormaker_user_configs", kafka_mirrormaker_user_configs)
        if logs_user_configs and not isinstance(logs_user_configs, list):
            raise TypeError("Expected argument 'logs_user_configs' to be a list")
        pulumi.set(__self__, "logs_user_configs", logs_user_configs)
        if metrics_user_configs and not isinstance(metrics_user_configs, list):
            raise TypeError("Expected argument 'metrics_user_configs' to be a list")
        pulumi.set(__self__, "metrics_user_configs", metrics_user_configs)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if source_endpoint_id and not isinstance(source_endpoint_id, str):
            raise TypeError("Expected argument 'source_endpoint_id' to be a str")
        pulumi.set(__self__, "source_endpoint_id", source_endpoint_id)
        if source_service_name and not isinstance(source_service_name, str):
            raise TypeError("Expected argument 'source_service_name' to be a str")
        pulumi.set(__self__, "source_service_name", source_service_name)

    @property
    @pulumi.getter(name="clickhouseKafkaUserConfigs")
    def clickhouse_kafka_user_configs(self) -> Sequence['outputs.GetServiceIntegrationClickhouseKafkaUserConfigResult']:
        """
        ClickhouseKafka user configurable settings
        """
        return pulumi.get(self, "clickhouse_kafka_user_configs")

    @property
    @pulumi.getter(name="clickhousePostgresqlUserConfigs")
    def clickhouse_postgresql_user_configs(self) -> Sequence['outputs.GetServiceIntegrationClickhousePostgresqlUserConfigResult']:
        """
        ClickhousePostgresql user configurable settings
        """
        return pulumi.get(self, "clickhouse_postgresql_user_configs")

    @property
    @pulumi.getter(name="datadogUserConfigs")
    def datadog_user_configs(self) -> Sequence['outputs.GetServiceIntegrationDatadogUserConfigResult']:
        """
        Datadog user configurable settings
        """
        return pulumi.get(self, "datadog_user_configs")

    @property
    @pulumi.getter(name="destinationEndpointId")
    def destination_endpoint_id(self) -> str:
        """
        Destination endpoint for the integration (if any)
        """
        return pulumi.get(self, "destination_endpoint_id")

    @property
    @pulumi.getter(name="destinationServiceName")
    def destination_service_name(self) -> str:
        """
        Destination service for the integration (if any)
        """
        return pulumi.get(self, "destination_service_name")

    @property
    @pulumi.getter(name="externalAwsCloudwatchMetricsUserConfigs")
    def external_aws_cloudwatch_metrics_user_configs(self) -> Sequence['outputs.GetServiceIntegrationExternalAwsCloudwatchMetricsUserConfigResult']:
        """
        ExternalAwsCloudwatchMetrics user configurable settings
        """
        return pulumi.get(self, "external_aws_cloudwatch_metrics_user_configs")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> str:
        """
        Service Integration Id at aiven
        """
        return pulumi.get(self, "integration_id")

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> str:
        """
        Type of the service integration. Possible values: `alertmanager`, `cassandra_cross_service_cluster`, `clickhouse_kafka`, `clickhouse_postgresql`, `dashboard`, `datadog`, `datasource`, `external_aws_cloudwatch_logs`, `external_aws_cloudwatch_metrics`, `external_elasticsearch_logs`, `external_google_cloud_logging`, `external_opensearch_logs`, `flink`, `internal_connectivity`, `jolokia`, `kafka_connect`, `kafka_logs`, `kafka_mirrormaker`, `logs`, `m3aggregator`, `m3coordinator`, `metrics`, `opensearch_cross_cluster_replication`, `opensearch_cross_cluster_search`, `prometheus`, `read_replica`, `rsyslog`, `schema_registry_proxy`
        """
        return pulumi.get(self, "integration_type")

    @property
    @pulumi.getter(name="kafkaConnectUserConfigs")
    def kafka_connect_user_configs(self) -> Sequence['outputs.GetServiceIntegrationKafkaConnectUserConfigResult']:
        """
        KafkaConnect user configurable settings
        """
        return pulumi.get(self, "kafka_connect_user_configs")

    @property
    @pulumi.getter(name="kafkaLogsUserConfigs")
    def kafka_logs_user_configs(self) -> Sequence['outputs.GetServiceIntegrationKafkaLogsUserConfigResult']:
        """
        KafkaLogs user configurable settings
        """
        return pulumi.get(self, "kafka_logs_user_configs")

    @property
    @pulumi.getter(name="kafkaMirrormakerUserConfigs")
    def kafka_mirrormaker_user_configs(self) -> Sequence['outputs.GetServiceIntegrationKafkaMirrormakerUserConfigResult']:
        """
        KafkaMirrormaker user configurable settings
        """
        return pulumi.get(self, "kafka_mirrormaker_user_configs")

    @property
    @pulumi.getter(name="logsUserConfigs")
    def logs_user_configs(self) -> Sequence['outputs.GetServiceIntegrationLogsUserConfigResult']:
        """
        Logs user configurable settings
        """
        return pulumi.get(self, "logs_user_configs")

    @property
    @pulumi.getter(name="metricsUserConfigs")
    def metrics_user_configs(self) -> Sequence['outputs.GetServiceIntegrationMetricsUserConfigResult']:
        """
        Metrics user configurable settings
        """
        return pulumi.get(self, "metrics_user_configs")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Project the integration belongs to
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="sourceEndpointId")
    def source_endpoint_id(self) -> str:
        """
        Source endpoint for the integration (if any)
        """
        return pulumi.get(self, "source_endpoint_id")

    @property
    @pulumi.getter(name="sourceServiceName")
    def source_service_name(self) -> str:
        """
        Source service for the integration (if any)
        """
        return pulumi.get(self, "source_service_name")


class AwaitableGetServiceIntegrationResult(GetServiceIntegrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceIntegrationResult(
            clickhouse_kafka_user_configs=self.clickhouse_kafka_user_configs,
            clickhouse_postgresql_user_configs=self.clickhouse_postgresql_user_configs,
            datadog_user_configs=self.datadog_user_configs,
            destination_endpoint_id=self.destination_endpoint_id,
            destination_service_name=self.destination_service_name,
            external_aws_cloudwatch_metrics_user_configs=self.external_aws_cloudwatch_metrics_user_configs,
            id=self.id,
            integration_id=self.integration_id,
            integration_type=self.integration_type,
            kafka_connect_user_configs=self.kafka_connect_user_configs,
            kafka_logs_user_configs=self.kafka_logs_user_configs,
            kafka_mirrormaker_user_configs=self.kafka_mirrormaker_user_configs,
            logs_user_configs=self.logs_user_configs,
            metrics_user_configs=self.metrics_user_configs,
            project=self.project,
            source_endpoint_id=self.source_endpoint_id,
            source_service_name=self.source_service_name)


def get_service_integration(destination_service_name: Optional[str] = None,
                            integration_type: Optional[str] = None,
                            project: Optional[str] = None,
                            source_service_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceIntegrationResult:
    """
    The Service Integration data source provides information about the existing Aiven Service Integration.

    Service Integration defines an integration between two Aiven services or between Aiven service and an external
    integration endpoint. Integration could be for example sending metrics from Kafka service to an M3DB service,
    getting metrics from an M3Db service to a Grafana service to show dashboards, sending logs from any service to
    OpenSearch, etc.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    myintegration = aiven.get_service_integration(project=aiven_project["myproject"]["project"],
        destination_service_name="<DESTINATION_SERVICE_NAME>",
        integration_type="datadog",
        source_service_name="<SOURCE_SERVICE_NAME>")
    ```


    :param str destination_service_name: Destination service for the integration (if any)
    :param str integration_type: Type of the service integration. Possible values: `alertmanager`, `cassandra_cross_service_cluster`, `clickhouse_kafka`, `clickhouse_postgresql`, `dashboard`, `datadog`, `datasource`, `external_aws_cloudwatch_logs`, `external_aws_cloudwatch_metrics`, `external_elasticsearch_logs`, `external_google_cloud_logging`, `external_opensearch_logs`, `flink`, `internal_connectivity`, `jolokia`, `kafka_connect`, `kafka_logs`, `kafka_mirrormaker`, `logs`, `m3aggregator`, `m3coordinator`, `metrics`, `opensearch_cross_cluster_replication`, `opensearch_cross_cluster_search`, `prometheus`, `read_replica`, `rsyslog`, `schema_registry_proxy`
    :param str project: Project the integration belongs to
    :param str source_service_name: Source service for the integration (if any)
    """
    __args__ = dict()
    __args__['destinationServiceName'] = destination_service_name
    __args__['integrationType'] = integration_type
    __args__['project'] = project
    __args__['sourceServiceName'] = source_service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getServiceIntegration:getServiceIntegration', __args__, opts=opts, typ=GetServiceIntegrationResult).value

    return AwaitableGetServiceIntegrationResult(
        clickhouse_kafka_user_configs=pulumi.get(__ret__, 'clickhouse_kafka_user_configs'),
        clickhouse_postgresql_user_configs=pulumi.get(__ret__, 'clickhouse_postgresql_user_configs'),
        datadog_user_configs=pulumi.get(__ret__, 'datadog_user_configs'),
        destination_endpoint_id=pulumi.get(__ret__, 'destination_endpoint_id'),
        destination_service_name=pulumi.get(__ret__, 'destination_service_name'),
        external_aws_cloudwatch_metrics_user_configs=pulumi.get(__ret__, 'external_aws_cloudwatch_metrics_user_configs'),
        id=pulumi.get(__ret__, 'id'),
        integration_id=pulumi.get(__ret__, 'integration_id'),
        integration_type=pulumi.get(__ret__, 'integration_type'),
        kafka_connect_user_configs=pulumi.get(__ret__, 'kafka_connect_user_configs'),
        kafka_logs_user_configs=pulumi.get(__ret__, 'kafka_logs_user_configs'),
        kafka_mirrormaker_user_configs=pulumi.get(__ret__, 'kafka_mirrormaker_user_configs'),
        logs_user_configs=pulumi.get(__ret__, 'logs_user_configs'),
        metrics_user_configs=pulumi.get(__ret__, 'metrics_user_configs'),
        project=pulumi.get(__ret__, 'project'),
        source_endpoint_id=pulumi.get(__ret__, 'source_endpoint_id'),
        source_service_name=pulumi.get(__ret__, 'source_service_name'))


@_utilities.lift_output_func(get_service_integration)
def get_service_integration_output(destination_service_name: Optional[pulumi.Input[str]] = None,
                                   integration_type: Optional[pulumi.Input[str]] = None,
                                   project: Optional[pulumi.Input[str]] = None,
                                   source_service_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceIntegrationResult]:
    """
    The Service Integration data source provides information about the existing Aiven Service Integration.

    Service Integration defines an integration between two Aiven services or between Aiven service and an external
    integration endpoint. Integration could be for example sending metrics from Kafka service to an M3DB service,
    getting metrics from an M3Db service to a Grafana service to show dashboards, sending logs from any service to
    OpenSearch, etc.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    myintegration = aiven.get_service_integration(project=aiven_project["myproject"]["project"],
        destination_service_name="<DESTINATION_SERVICE_NAME>",
        integration_type="datadog",
        source_service_name="<SOURCE_SERVICE_NAME>")
    ```


    :param str destination_service_name: Destination service for the integration (if any)
    :param str integration_type: Type of the service integration. Possible values: `alertmanager`, `cassandra_cross_service_cluster`, `clickhouse_kafka`, `clickhouse_postgresql`, `dashboard`, `datadog`, `datasource`, `external_aws_cloudwatch_logs`, `external_aws_cloudwatch_metrics`, `external_elasticsearch_logs`, `external_google_cloud_logging`, `external_opensearch_logs`, `flink`, `internal_connectivity`, `jolokia`, `kafka_connect`, `kafka_logs`, `kafka_mirrormaker`, `logs`, `m3aggregator`, `m3coordinator`, `metrics`, `opensearch_cross_cluster_replication`, `opensearch_cross_cluster_search`, `prometheus`, `read_replica`, `rsyslog`, `schema_registry_proxy`
    :param str project: Project the integration belongs to
    :param str source_service_name: Source service for the integration (if any)
    """
    ...
