
* Terraform is an open source tool by HashiCorp used for provisioning infrastructure resources using Infrastructure-as-a-code paradigms.
* Terraform has a state based approach for tracking resource allocation.

* A service account has restricted permissions and is used for configuring a specific
service to use the resources on a project on the cloud. A service could be something like a data pipeline or a web server. It gives us credentials that belong to a specific service. You dont need the owners or admin's account for resource interaction, and it has limited permissions.

* Google SDK will be needed to interact with the service account and for authenticating services.

* Oauth is one way of authenticating.It involves a browser. If you are working on an instance where you do not have access to your browser, you wont be able to use oauth for authenticating.


## Creating Infrastructure with Terraform.

We will be creating two resources in the google environment:
* Cloud storage (data lake) - A bucket where you can store data in the format of flat files.
* BigQuery (data warehouse)


* Go into IAM to grant access to the service account so that Terraform can perform the necessary functions. We will be assigning the following two roles:
    * Storage Admin - Grants full control of buckets and objects.
    * Storage Object Admin - Grants full control over objects, including listing, creating, viewing and deleting objects.
    * BigQuery Admin


* Enable the following APIs
   *  Identity and Access Management (IAM) API
  *   IAM Service Account Credentials API



## Terraform Execution Steps
* `terraform init` - Initialize and install
* `terraform plan` - Make changes against the previous state
* `terraform apply` - Apply changes to cloud
* `terraform destroy` - Remove your stack from the cloud
