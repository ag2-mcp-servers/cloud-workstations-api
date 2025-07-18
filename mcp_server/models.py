# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:10:08+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class LogType(Enum):
    LOG_TYPE_UNSPECIFIED = 'LOG_TYPE_UNSPECIFIED'
    ADMIN_READ = 'ADMIN_READ'
    DATA_WRITE = 'DATA_WRITE'
    DATA_READ = 'DATA_READ'


class AuditLogConfig(BaseModel):
    exemptedMembers: Optional[List[str]] = Field(
        None,
        description='Specifies the identities that do not cause logging for this type of permission. Follows the same format of Binding.members.',
    )
    logType: Optional[LogType] = Field(
        None, description='The log type that this config enables.'
    )


class CancelOperationRequest(BaseModel):
    pass


class Container(BaseModel):
    args: Optional[List[str]] = Field(
        None, description='Arguments passed to the entrypoint.'
    )
    command: Optional[List[str]] = Field(
        None,
        description='If set, overrides the default ENTRYPOINT specified by the image.',
    )
    env: Optional[Dict[str, str]] = Field(
        None, description='Environment variables passed to the container.'
    )
    image: Optional[str] = Field(
        None,
        description="Docker image defining the container. This image must be accessible by the config's service account.",
    )
    runAsUser: Optional[int] = Field(
        None,
        description='If set, overrides the USER specified in the image with the given uid.',
    )
    workingDir: Optional[str] = Field(
        None, description='If set, overrides the default DIR specified by the image.'
    )


class CustomerEncryptionKey(BaseModel):
    kmsKey: Optional[str] = Field(
        None,
        description='Immutable. The name of the Google Cloud KMS encryption key. For example, `projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`.',
    )
    kmsKeyServiceAccount: Optional[str] = Field(
        None,
        description='Immutable. The service account to use with the specified KMS key. We recommend that you use a separate service account and follow KMS best practices. For more information, see [Separation of duties](https://cloud.google.com/kms/docs/separation-of-duties) and `gcloud kms keys add-iam-policy-binding` [`--member`](https://cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding#--member).',
    )


class Expr(BaseModel):
    description: Optional[str] = Field(
        None,
        description='Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.',
    )
    expression: Optional[str] = Field(
        None,
        description='Textual representation of an expression in Common Expression Language syntax.',
    )
    location: Optional[str] = Field(
        None,
        description='Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.',
    )
    title: Optional[str] = Field(
        None,
        description='Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.',
    )


class GceConfidentialInstanceConfig(BaseModel):
    enableConfidentialCompute: Optional[bool] = Field(
        None, description='Whether the instance has confidential compute enabled.'
    )


class ReclaimPolicy(Enum):
    RECLAIM_POLICY_UNSPECIFIED = 'RECLAIM_POLICY_UNSPECIFIED'
    DELETE = 'DELETE'
    RETAIN = 'RETAIN'


class GceRegionalPersistentDisk(BaseModel):
    diskType: Optional[str] = Field(
        None, description='Type of the disk to use. Defaults to pd-standard.'
    )
    fsType: Optional[str] = Field(
        None,
        description='Type of file system that the disk should be formatted with. The workstation image must support this file system type. Must be empty if source_snapshot is set. Defaults to ext4.',
    )
    reclaimPolicy: Optional[ReclaimPolicy] = Field(
        None,
        description='What should happen to the disk after the workstation is deleted. Defaults to DELETE.',
    )
    sizeGb: Optional[int] = Field(
        None,
        description='Size of the disk in GB. Must be empty if source_snapshot is set. Defaults to 200.',
    )
    sourceSnapshot: Optional[str] = Field(
        None,
        description='Name of the snapshot to use as the source for the disk. If set, size_gb and fs_type must be empty.',
    )


class GceShieldedInstanceConfig(BaseModel):
    enableIntegrityMonitoring: Optional[bool] = Field(
        None, description='Whether the instance has integrity monitoring enabled.'
    )
    enableSecureBoot: Optional[bool] = Field(
        None, description='Whether the instance has Secure Boot enabled.'
    )
    enableVtpm: Optional[bool] = Field(
        None, description='Whether the instance has the vTPM enabled.'
    )


class GenerateAccessTokenRequest(BaseModel):
    expireTime: Optional[str] = Field(
        None,
        description="Desired expiration time of the access token. This value must be at most 24 hours in the future. If a value is not specified, the token's expiration time will be set to a default value of 1 hour in the future.",
    )
    ttl: Optional[str] = Field(
        None,
        description="Desired lifetime duration of the access token. This value must be at most 24 hours. If a value is not specified, the token's lifetime will be set to a default value of 1 hour.",
    )


class GenerateAccessTokenResponse(BaseModel):
    accessToken: Optional[str] = Field(
        None,
        description="The generated bearer access token. To use this token, include it in an Authorization header of an HTTP request sent to the associated workstation's hostname, for example, `Authorization: Bearer `.",
    )
    expireTime: Optional[str] = Field(
        None, description='Time at which the generated token will expire.'
    )


class GoogleProtobufEmpty(BaseModel):
    pass


class OperationMetadata(BaseModel):
    apiVersion: Optional[str] = Field(
        None, description='Output only. API version used to start the operation.'
    )
    createTime: Optional[str] = Field(
        None, description='Output only. Time that the operation was created.'
    )
    endTime: Optional[str] = Field(
        None, description='Output only. Time that the operation finished running.'
    )
    requestedCancellation: Optional[bool] = Field(
        None,
        description='Output only. Identifies whether the user has requested cancellation of the operation.',
    )
    statusMessage: Optional[str] = Field(
        None, description='Output only. Human-readable status of the operation, if any.'
    )
    target: Optional[str] = Field(
        None,
        description='Output only. Server-defined resource path for the target of the operation.',
    )
    verb: Optional[str] = Field(
        None, description='Output only. Name of the verb executed by the operation.'
    )


class PersistentDirectory(BaseModel):
    gcePd: Optional[GceRegionalPersistentDisk] = Field(
        None,
        description='A PersistentDirectory backed by a Compute Engine persistent disk.',
    )
    mountPath: Optional[str] = Field(
        None, description='Location of this directory in the running workstation.'
    )


class PrivateClusterConfig(BaseModel):
    allowedProjects: Optional[List[str]] = Field(
        None,
        description="Additional projects that are allowed to attach to the workstation cluster's service attachment. By default, the workstation cluster's project and the VPC host project (if different) are allowed.",
    )
    clusterHostname: Optional[str] = Field(
        None,
        description='Output only. Hostname for the workstation cluster. This field will be populated only when private endpoint is enabled. To access workstations in the cluster, create a new DNS zone mapping this domain name to an internal IP address and a forwarding rule mapping that address to the service attachment.',
    )
    enablePrivateEndpoint: Optional[bool] = Field(
        None, description='Immutable. Whether Workstations endpoint is private.'
    )
    serviceAttachmentUri: Optional[str] = Field(
        None,
        description='Output only. Service attachment URI for the workstation cluster. The service attachemnt is created when private endpoint is enabled. To access workstations in the cluster, configure access to the managed service using [Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-services).',
    )


class StartWorkstationRequest(BaseModel):
    etag: Optional[str] = Field(
        None,
        description='If set, the request will be rejected if the latest version of the workstation on the server does not have this etag.',
    )
    validateOnly: Optional[bool] = Field(
        None,
        description='If set, validate the request and preview the review, but do not actually apply it.',
    )


class Status(BaseModel):
    code: Optional[int] = Field(
        None,
        description='The status code, which should be an enum value of google.rpc.Code.',
    )
    details: Optional[List[Dict[str, Any]]] = Field(
        None,
        description='A list of messages that carry the error details. There is a common set of message types for APIs to use.',
    )
    message: Optional[str] = Field(
        None,
        description='A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.',
    )


class StopWorkstationRequest(BaseModel):
    etag: Optional[str] = Field(
        None,
        description='If set, the request will be rejected if the latest version of the workstation on the server does not have this etag.',
    )
    validateOnly: Optional[bool] = Field(
        None,
        description='If set, validate the request and preview the review, but do not actually apply it.',
    )


class TestIamPermissionsRequest(BaseModel):
    permissions: Optional[List[str]] = Field(
        None,
        description='The set of permissions to check for the `resource`. Permissions with wildcards (such as `*` or `storage.*`) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).',
    )


class TestIamPermissionsResponse(BaseModel):
    permissions: Optional[List[str]] = Field(
        None,
        description='A subset of `TestPermissionsRequest.permissions` that the caller is allowed.',
    )


class State(Enum):
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'
    STATE_STARTING = 'STATE_STARTING'
    STATE_RUNNING = 'STATE_RUNNING'
    STATE_STOPPING = 'STATE_STOPPING'
    STATE_STOPPED = 'STATE_STOPPED'


class Workstation(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None, description='Client-specified annotations.'
    )
    createTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was created.'
    )
    deleteTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was soft-deleted.'
    )
    displayName: Optional[str] = Field(
        None, description='Human-readable name for this resource.'
    )
    env: Optional[Dict[str, str]] = Field(
        None, description='Environment variables passed to the workstation container.'
    )
    etag: Optional[str] = Field(
        None,
        description='Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.',
    )
    host: Optional[str] = Field(
        None,
        description='Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format `{port}-{host}`.',
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.',
    )
    name: Optional[str] = Field(None, description='Full name of this resource.')
    reconciling: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether this resource is currently being updated to match its intended state.',
    )
    state: Optional[State] = Field(
        None, description='Output only. Current state of the workstation.'
    )
    uid: Optional[str] = Field(
        None,
        description='Output only. A system-assigned unique identified for this resource.',
    )
    updateTime: Optional[str] = Field(
        None,
        description='Output only. Time when this resource was most recently updated.',
    )


class WorkstationCluster(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None, description='Client-specified annotations.'
    )
    conditions: Optional[List[Status]] = Field(
        None,
        description='Output only. Status conditions describing the current resource state.',
    )
    controlPlaneIp: Optional[str] = Field(
        None,
        description='Output only. The private IP address of the control plane for this cluster. Workstation VMs need access to this IP address to work with the service, so please ensure your firewall rules allow egress from the Workstation VMs to this address.',
    )
    createTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was created.'
    )
    degraded: Optional[bool] = Field(
        None,
        description='Output only. Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field.',
    )
    deleteTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was soft-deleted.'
    )
    displayName: Optional[str] = Field(
        None, description='Human-readable name for this resource.'
    )
    etag: Optional[str] = Field(
        None,
        description='Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.',
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.',
    )
    name: Optional[str] = Field(None, description='Full name of this resource.')
    network: Optional[str] = Field(
        None,
        description='Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created.',
    )
    privateClusterConfig: Optional[PrivateClusterConfig] = Field(
        None, description='Configuration for private cluster.'
    )
    reconciling: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether this resource is currently being updated to match its intended state.',
    )
    subnetwork: Optional[str] = Field(
        None,
        description='Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster.',
    )
    uid: Optional[str] = Field(
        None,
        description='Output only. A system-assigned unique identified for this resource.',
    )
    updateTime: Optional[str] = Field(
        None,
        description='Output only. Time when this resource was most recently updated.',
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class AuditConfig(BaseModel):
    auditLogConfigs: Optional[List[AuditLogConfig]] = Field(
        None, description='The configuration for logging of each type of permission.'
    )
    service: Optional[str] = Field(
        None,
        description='Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.',
    )


class Binding(BaseModel):
    condition: Optional[Expr] = Field(
        None,
        description='The condition that is associated with this binding. If the condition evaluates to `true`, then this binding applies to the current request. If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).',
    )
    members: Optional[List[str]] = Field(
        None,
        description='Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values: * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account. * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. Does not include identities that come from external identity providers (IdPs) through identity federation. * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` . * `serviceAccount:{emailid}`: An email address that represents a Google service account. For example, `my-other-app@appspot.gserviceaccount.com`. * `serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]`: An identifier for a [Kubernetes service account](https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts). For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`. * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`. * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`. * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding. * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.',
    )
    role: Optional[str] = Field(
        None,
        description='Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.',
    )


class GceInstance(BaseModel):
    bootDiskSizeGb: Optional[int] = Field(
        None, description='Size of the boot disk in GB. Defaults to 50.'
    )
    confidentialInstanceConfig: Optional[GceConfidentialInstanceConfig] = Field(
        None, description='A set of Compute Engine Confidential VM instance options.'
    )
    disablePublicIpAddresses: Optional[bool] = Field(
        None, description='Whether instances have no public IP address.'
    )
    machineType: Optional[str] = Field(
        None, description='The name of a Compute Engine machine type.'
    )
    poolSize: Optional[int] = Field(
        None, description='Number of instances to pool for faster workstation starup.'
    )
    serviceAccount: Optional[str] = Field(
        None,
        description='Email address of the service account that will be used on VM instances used to support this config. If not set, VMs will run with a Google-managed service account. This service account must have permission to pull the specified container image, otherwise the image must be publicly accessible.',
    )
    shieldedInstanceConfig: Optional[GceShieldedInstanceConfig] = Field(
        None, description='A set of Compute Engine Shielded instance options.'
    )
    tags: Optional[List[str]] = Field(
        None,
        description='Network tags to add to the Compute Engine machines backing the Workstations.',
    )


class Host(BaseModel):
    gceInstance: Optional[GceInstance] = Field(
        None, description='Specifies a Compute Engine instance as the host.'
    )


class ListUsableWorkstationsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='Token to retrieve the next page of results, or empty if there are no more results in the list.',
    )
    unreachable: Optional[List[str]] = Field(None, description='Unreachable resources.')
    workstations: Optional[List[Workstation]] = Field(
        None, description='The requested workstations.'
    )


class ListWorkstationClustersResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='Token to retrieve the next page of results, or empty if there are no more results in the list.',
    )
    unreachable: Optional[List[str]] = Field(None, description='Unreachable resources.')
    workstationClusters: Optional[List[WorkstationCluster]] = Field(
        None, description='The requested workstation clusters.'
    )


class ListWorkstationsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='Token to retrieve the next page of results, or empty if there are no more results in the list.',
    )
    unreachable: Optional[List[str]] = Field(None, description='Unreachable resources.')
    workstations: Optional[List[Workstation]] = Field(
        None, description='The requested workstations.'
    )


class Operation(BaseModel):
    done: Optional[bool] = Field(
        None,
        description='If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.',
    )
    error: Optional[Status] = Field(
        None,
        description='The error result of the operation in case of failure or cancellation.',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description='Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.',
    )
    name: Optional[str] = Field(
        None,
        description='The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.',
    )
    response: Optional[Dict[str, Any]] = Field(
        None,
        description='The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.',
    )


class Policy(BaseModel):
    auditConfigs: Optional[List[AuditConfig]] = Field(
        None, description='Specifies cloud audit logging configuration for this policy.'
    )
    bindings: Optional[List[Binding]] = Field(
        None,
        description='Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal. The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`.',
    )
    etag: Optional[str] = Field(
        None,
        description='`etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy. **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.',
    )
    version: Optional[int] = Field(
        None,
        description='Specifies the format of the policy. Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected. Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations: * Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).',
    )


class SetIamPolicyRequest(BaseModel):
    policy: Optional[Policy] = Field(
        None,
        description='REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.',
    )
    updateMask: Optional[str] = Field(
        None,
        description='OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used: `paths: "bindings, etag"`',
    )


class WorkstationConfig(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None, description='Client-specified annotations.'
    )
    conditions: Optional[List[Status]] = Field(
        None,
        description='Output only. Status conditions describing the current resource state.',
    )
    container: Optional[Container] = Field(
        None,
        description='Container that will be run for each workstation using this configuration when that workstation is started.',
    )
    createTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was created.'
    )
    degraded: Optional[bool] = Field(
        None,
        description='Output only. Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field.',
    )
    deleteTime: Optional[str] = Field(
        None, description='Output only. Time when this resource was soft-deleted.'
    )
    displayName: Optional[str] = Field(
        None, description='Human-readable name for this resource.'
    )
    enableAuditAgent: Optional[bool] = Field(
        None,
        description='Whether to enable linux auditd logging on the workstation. When enabled, a service account must also be specified that has logging.buckets.write permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging).',
    )
    encryptionKey: Optional[CustomerEncryptionKey] = Field(
        None,
        description='Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key. If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata. If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk will be lost. If the encryption key is revoked, the workstation session will automatically be stopped within 7 hours. Immutable after workstation config is created.',
    )
    etag: Optional[str] = Field(
        None,
        description='Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.',
    )
    host: Optional[Host] = Field(None, description='Runtime host for the workstation.')
    idleTimeout: Optional[str] = Field(
        None,
        description="How long to wait before automatically stopping an instance that hasn't received any user traffic. A value of 0 indicates that this instance should never time out due to idleness. Defaults to 20 minutes.",
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.',
    )
    name: Optional[str] = Field(None, description='Full name of this resource.')
    persistentDirectories: Optional[List[PersistentDirectory]] = Field(
        None, description='Directories to persist across workstation sessions.'
    )
    reconciling: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether this resource is currently being updated to match its intended state.',
    )
    runningTimeout: Optional[str] = Field(
        None,
        description='How long to wait before automatically stopping a workstation after it started. A value of 0 indicates that workstations using this configuration should never time out. Must be greater than 0 and less than 24 hours if encryption_key is set. Defaults to 12 hours.',
    )
    uid: Optional[str] = Field(
        None,
        description='Output only. A system-assigned unique identified for this resource.',
    )
    updateTime: Optional[str] = Field(
        None,
        description='Output only. Time when this resource was most recently updated.',
    )


class ListOperationsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None, description='The standard List next-page token.'
    )
    operations: Optional[List[Operation]] = Field(
        None,
        description='A list of operations that matches the specified filter in the request.',
    )


class ListUsableWorkstationConfigsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='Token to retrieve the next page of results, or empty if there are no more results in the list.',
    )
    unreachable: Optional[List[str]] = Field(None, description='Unreachable resources.')
    workstationConfigs: Optional[List[WorkstationConfig]] = Field(
        None, description='The requested configs.'
    )


class ListWorkstationConfigsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='Token to retrieve the next page of results, or empty if there are no more results in the list.',
    )
    unreachable: Optional[List[str]] = Field(None, description='Unreachable resources.')
    workstationConfigs: Optional[List[WorkstationConfig]] = Field(
        None, description='The requested configs.'
    )
