

# Hangar Documentation

## Tutorial

### Prerequisites
- Atleast Python 3.10.2 installed
- AWS account
- Github account
- Hangar account with an api key

### Setup

1. Install Hangar CLI

```
pip install hangar-cli
```

2. Make a new python file with function named hangar_run

3. Create a new scope

```
from hangar_sdk.base import HangarScope

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
   
```

4. Create a new asset

```
from hangar_sdk.base import HangarScope, Asset, GitHubRepo

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )

```

5. Create a new builder

```

from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )

```

6. Create a new registry

```
from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )

```


7. Create a new container builder

```

from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry, ContainerBuilder

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )
    containerBuilder = ContainerBuilder(
            name="my-container-builder",
            asset=asset,
            builder=builder,
            registry=registry,
        )

```

8. Create a new container and service

```
from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry, ContainerBuilder, Container, Service

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )
    containerBuilder = ContainerBuilder(
            name="my-container-builder",
            asset=asset,
            builder=builder,
            registry=registry,
        )
    container = Container(
            source=registry,
            tag="latest",
        )
    service = Service(
            name="my-service",
            container=container,
        )

```

9. Create a new cluster

```
from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry, ContainerBuilder, Container, Service, Cluster

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )
    containerBuilder = ContainerBuilder(
            name="my-container-builder",
            asset=asset,
            builder=builder,
            registry=registry,
        )
    container = Container(
            source=registry,
            tag="latest",
        )
    service = Service(
            name="my-service",
            container=container,
        )
    cluster = Cluster(
            name="my-cluster",
            services=[service],
        )

```

10. Resolve the cluster and builder

```

from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry, ContainerBuilder, Container, Service, Cluster

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )
    containerBuilder = ContainerBuilder(
            name="my-container-builder",
            asset=asset,
            builder=builder,
            registry=registry,
        )
    container = Container(
            source=registry,
            tag="latest",
        )
    service = Service(
            name="my-service",
            container=container,
        )
    cluster = Cluster(
            name="my-cluster",
            services=[service],
        )
    asyncio.run(containerBuilder.resolve())
    asyncio.run(cluster.resolve())
```

11. Run the hangar cli

```
hangar up <file>
```

12. Trigger a build

```

from hangar_sdk.base import HangarScope, Asset, GitHubRepo, BuildkitBuilder, Registry, ContainerBuilder, Container, Service, Cluster

def hangar_run():
    scope = HangarScope(
        name="my-first-scope",
        region="us-west-2",
        roleAssumptions=[],
    )
    asset = Asset(
            scope=scope,
            name="<your-name>-my-first-bucket",
            source=GitHubRepo(
                scope=scope,
                repo="your-repo",
                branch="main",
                name="my-repo",
            ),
        )
    builder = BuildkitBuilder(
            scope=scope,
            name="my-builder",
        )
    registry = Registry(
            scope=scope,
            name="my-registry",
        )
    containerBuilder = ContainerBuilder(
            name="my-container-builder",
            asset=asset,
            builder=builder,
            registry=registry,
        )
    container = Container(
            source=registry,
            tag="latest",
        )
    service = Service(
            name="my-service",
            container=container,
        )
    cluster = Cluster(
            name="my-cluster",
            services=[service],
        )
    asyncio.run(containerBuilder.resolve())
    asyncio.run(cluster.resolve())


    asset.sync(token="<your-github-token>")
    containerBuilder.build()
```

13. Run the hangar cli to create all the resources

```
hangar up <file>
```

14. Once you are done delete all resources. Note: This doesnt delete all resources immediately but marks them for deletion. The resources will be deleted by hangar in atmost 10 minutes.

```
hangar down <file>
```

You can view your constructs, logs and other data in the hangar cloud console [here](https://console.tryhangar.com/).

## Hangar CLI

Hangar CLI is a command line tool that allows you to interact with Hangar. It allows you to create and manage scopes, assets, and constructs. It also allows you to trigger builds on constructs.


### Installation

```
pip install hangar-cli
```


## HangarScope

```
HangarScope(
        region: str,
        name: str,
        roleAssumptions: list = [],
        api_key: str | None = None,
        endpoint: str = None,
    )
```

Hangar constructs or resources are grouped into scopes. A scope contains the configuration of where the resources will be deployed.  The region provided to scope will be used as the aws region where all resources in that scope will be deployed to. The name provided to scope will be used as the name of the scope. The name of the scope is used to create a unique namespace for all resources in that scope. The roleAssumptions is a list of role arns that hangar will assume successively to create resources in that scope. The api_key is the hangar api key used to authenticate with hangar. The endpoint is the hangar api endpoint. If not provided, it will default to the hangar cloud endpoint.



## Constructs

Cloud resources are created and represented by constructs. Unlike constructs in terraform, CDK and pulumi, constructs in Hangar not just create the resource but also allow you to interact with it. For example, the code build construct not only creates a code build instance but also allows you to trigger a build on it. Another difference hangar will reconcile any configuration drift in cloud resources from your definition. For example, if soemone else changes the configuration of a code build instance, hangar will reconcile it back to your definition. To actually create a construct you need to call the resolve method. Not every construct needs to be reolved only those that are not depended by any other contruct.

### Actions

Actions are methods on constructs that allow you to interact with those cloud resources. For example, the build action on the code build construct allows you to trigger a build on the code build instance.

### Asset

```
Asset(
    scope : HangarScope,
    name : str,
    source : SourceInterface
)
```
Actions:
```
asset = Asset(...)
asset.sync(token : str)
```
Any type of source code is an Asset. The Asset contsruct is used to define an asset which can then be consumed by other constructs. Currently the only type of Asset supported is a GitHub Repo. Support for local directories will be added soon. 

The construct supports the sync action. If the source is a public github repo not onboarded to hangar, then sync requires you to pass a github token. If the source is a private github repo onboarded to hangar, then sync does not require a github token. The sync action pulls the source code from the source and stores it in an S3 bucket. The sync action is idempotent. If the source code has not changed, then the sync action will not do anything.

## GithubRepo 

```
GitHubRepo(
    scope : HangarScope,
    name : str,
    repo : str,
    branch : str,
)

(implements source interface)
```

To reference your private Github Repo make sure you have onboarded your github repo [here](https://docs.tryhangar.com/quickstart/import-sources). For any public repo, when using the sync action on asset, make sure to pass your github token.

## BuildKit Builder

```
BuildkitBuilder(
    scope : HangarScope,
    name : str
)
```


This construct defines a BuildKit container used to build Docker images consumed by ContainerBuilder construct.


## Registry

```
Registry(
    scope : HangarScope,
    name : str
)

(implements the registry interface)

```

Refers to an ECR registry container registry. Stores docker images.

## Container Builder
```
ContainerBuilder(
    name: str,
    asset: Asset,
    builder: BuilderInterface,
    registry: RegistryInterface,
)
```
Actions:
```
containerBuilder = ContainerBuilder(...)
containerBuilder.build()
```

Creates a CodeBuild instance that consumes an asset, builder and a registry. When triggered using the 'build' action, it pulls the asset, builds it using the builder, and pushes image to registry.

The construct supports the build action. The build action triggers a build on the code build instance. The build action is idempotent. If the source code has not changed, then the build action will not do anything.

## Container
```
class PortMappings(BaseModel):
    containerPort: int
    hostPort: int

Container(
    source: Registry
    tag: str
    startCommand: str [optional]
    portMappings: List[PortMappings] [optional])
```
Creates a container itself from an image in a registry. Can override the start command, best and port mappings.

## Service
```
Service(
    name: str,
    container: Container,
    envVars: Dict[str, str] [optional]
)
```
Creates an ECS service. Consists of a container that it runs as part of the service. Also allos definition of env vars for the service.

## Cluster
```
Cluster(
    name: str,
    services: List[Service],
)
```
Creates an ECS cluster. Consists of a list of services that run as part of the cluster.

## Security Group

```
class Ingress(BaseModel):
    fromPort: int
    toPort: int
    protocol: str
    cidrIp: List[str]

class Egress(BaseModel):
    fromPort: int
    toPort: int
    protocol: str
    cidrIp: List[str]


SecurityGroup(
    scope: HangarScope,
    name: str,
    ingresses: List[Ingress],
    egresses: List[Egress],
)
```

Creates a security group. Consists of a list of ingress and egress rules. An ingress rule specifies what traffic is allowed through the security group. An egress rule specifies what traffic is allowed out of the security group.


## Instance

```
Instance(
    scope: HangarScope,
    name: str,
    instanceType: str,
    securityGroups: List[SecurityGroup],
    path_to_key: str,
)
```
Actions:
```
instance = Instance(...)
output = instance.run_command(<command>)
print(output)
 {
    "stdout": <stdout>,
    "stderr": <stderr>,
    "command": <command>
 }

for output in instance.run_commands():
    print(output)
    {
        "stdout": <stdout>,
        "stderr": <stderr>,
        "command": <command>
    }
```
Creates an EC2 instance or a VM with ubuntu. Consists of an instance type, security groups and a path to a key pair. The instance type specifies the type of instance to create. The security groups specify what traffic is allowed through the instance. The path to key pair specifies the path to the key pair used to ssh into the instance. If the ssh variable is set to true, the the security group will have an ingress rule that allows ssh traffic through the instance even if it is not specified in the security groups. The instance will also have a public ip address.

The construct supports the run_command and run_commands actions. These actions ssh into the instance and execute the given shell commands. The run_command action runs a single command on the instance. The run_commands action runs a list of commands on the instance. The run_command and run_commands actions are not idempotent. WARNING: These commands could lead to different outputs everytime.