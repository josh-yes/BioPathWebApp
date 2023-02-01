"""This script file will be used for deploying to AWS while our github actions are down
    
  To run this file: python3 local_deploy.py <options>
  
  Options include flags for what you want to be run:
    --images-to-ecr 
        will build, tag and push the projects images to ECR
    --deploy-infra 
        will deploy the AWS infrastructure stacks to AWS
    
  NOTE: The default run with no flags will run everything, if you include one flag
        only the specified job will be run"""


import os
import sys
import csv

# repository information 
# get updated info by command ""
# current info
#     "repository": {
#         "repositoryArn": "arn:aws:ecr:us-west-2:219085571562:repository/biopath-repo",
#         "registryId": "219085571562",
#         "repositoryName": "biopath-repo",
#         "repositoryUri": "219085571562.dkr.ecr.us-west-2.amazonaws.com/biopath-repo",
#         "createdAt": "2022-10-18T13:34:25-07:00",
#         "imageTagMutability": "MUTABLE",
#         "imageScanningConfiguration": {
#             "scanOnPush": false
#         },
#         "encryptionConfiguration": {
#             "encryptionType": "AES256"
#         }
#     }


# constants
REGION_NAME = "us-west-2"
ECR_REPO_URI = "219085571562.dkr.ecr.us-west-2.amazonaws.com/biopath-repo"
BACKEND_IMG_NAME = "biopath_backend"
BACKEND_TAG = "backend_latest" # TODO: change how we are doing tag versioning
FRONTEND_IMG_NAME = "biopath_frontend"
FRONTEND_TAG = "frontend_latest"

# file paths

#TODO: check if path to backend/frontend exist and can be reached
#TODO: path better
BACKEND_PATH = os.path.join("../", "backend/")
FRONTEND_PATH = os.path.join("../", "frontend/")
INFRA_PATH = os.path.join("infrastructure/")

# credentials for deployment
# import credentials file from credentials_<name>.txt
AWS_CRED_FILE_NAME = "aws_credentials.csv"


def console_job(job_title="", command="", desc=""):
  print("-----------------------------------------------------")
  print("     " + job_title)
  print("-----------------------------------------------------")

  if desc != "":
    print(desc)

  os.system(command)

  print("-----------------------done--------------------------", end="\n\n")


def create_aws_credentials():
  """
  If the credentials file is missing, enter in requested info and it will make it for you
  """
  column_names = ["User Name", "Account ID", "Access Key ID", "Secret Access Key", "Password"]
  print()
  print("Before signing into AWS, you will need to make a credentials file")
  print("Information needed: " + str(column_names))
  with open(AWS_CRED_FILE_NAME, "w") as csv_cred_file:
    writer = csv.writer(csv_cred_file)

    # write in column names
    writer.writerow(column_names)

    column_values = [input("Please enter your {}: ".format(item)) for item in column_names]
    writer.writerow(column_values)

def read_credentials():
  """
  Reads in the credentials from the credential file
  """

  cred_cols = []
  cred_vals = []

  with open(AWS_CRED_FILE_NAME, "r") as csv_cred_file:
    reader = csv.reader(csv_cred_file)

    try:
      cred_cols = next(reader)
      cred_vals = next(reader)
    except:
      print("Error: credentials file not well formed")
      return -1

  return cred_cols, cred_vals


def login_to_aws():
  """
  Logs you in to AWS, if the required credentials file for the user is missing
  you will be forwarded to a cred file build function
  """

  # first check if credentials file exists
  if not os.path.isfile(AWS_CRED_FILE_NAME):
    print("You are missing credentials file")
    create_aws_credentials()

  cred_cols, cred_vals = read_credentials()
    
  acct_id_index = cred_cols.index("Account ID")
  acct_id = cred_vals[acct_id_index]
  

  """aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/p4x5m2c9"""
  # login to AWS
  console_job("Logging Into AWS",
              f"""aws ecr get-login-password --region {REGION_NAME} \
                | docker login \
                  --username AWS \
                  --password-stdin {acct_id}.dkr.ecr.{REGION_NAME}.amazonaws.com""",
              "Using information fielded from aws_credentials.csv, Logging you into AWS console")


def images_to_ecr():
  """
  Builds, tags, and then pushes all images used in the project to AWS' ECR for containerization 
  on our VPC
  """

  # build the frontend and backend images
  console_job(
    "Building Frontend Docker Image", 
    f"docker build -t {FRONTEND_IMG_NAME}:{FRONTEND_TAG} {FRONTEND_PATH}"
  )
  console_job(
    "Building Backend Docker Image", 
    f"docker build -t {BACKEND_IMG_NAME}:{BACKEND_TAG} {BACKEND_PATH}"
  )

  # tag the images 
  console_job(
    "Tagging Frontend Image",
    f"docker tag {FRONTEND_IMG_NAME}:{FRONTEND_TAG} {ECR_REPO_URI}:{FRONTEND_TAG}"
  )
  console_job( 
    "Tagging Backend Image",
    f"docker tag {BACKEND_IMG_NAME}:{BACKEND_TAG} {ECR_REPO_URI}:{BACKEND_TAG}"
  )

  # push the images to ECR
  console_job(
    "Push Frontend Image to ECR",
    f"docker push {ECR_REPO_URI}:{FRONTEND_TAG}"
  )
  console_job(
    "Push Backend Image to ECR",
    f"docker push {ECR_REPO_URI}:{BACKEND_TAG}"
  )


  #TODO: clean up locally built images
  console_job(
    "Clean up Locally Built Frontend Image",
    f"docker rmi {FRONTEND_IMG_NAME}:{FRONTEND_TAG}"
  )
  console_job(
    "Clean up Locally Built Frontend Image",
    f"docker rmi {BACKEND_IMG_NAME}:{BACKEND_TAG}"
  )

def deploy_aws_infrastructure():
  """
  This function will deploy the .yaml files which are stored in the infrastructure dir
  When deployed AWS will create a stack for each of them
  """

  # deploy VPC stack to AWS
  console_job(
    "Deploy VPC Stack to Console",
    f"aws cloudformation create-stack --stack-name vpc --template-body file://{INFRA_PATH}VPC.yaml"
  )
  # deploy the credentials (IAM-Roles) stack
  console_job(
    "Deploy IAM Roles Stack",
    f"aws cloudformation create-stack --stack-name iam --template-body file://{INFRA_PATH}IAM-Roles.yaml --capabilities CAPABILITY_IAM"
  )
  # deploy the cluster
  console_job(
    "Deploy Cluster Stack",
    f"aws cloudformation create-stack --stack-name cluster --template-body file://{INFRA_PATH}Cluster.yaml"
  )
  # deploy the container stack
  console_job(
    "Deploy Container Stack",
    f"aws cloudformation create-stack --stack-name containers --template-body file://{INFRA_PATH}Containers.yaml"
  )


def main():
  """Main driver for the local deploy script"""
  flags = []

  if len(sys.argv) - 1 > 0:
    # there are flags that need to be handled
    flags = sys.argv[1:]

  #TODO: might need to change where this is placed depending on job, for now everything requires that you be signed in
  login_to_aws()
  

  for flag in flags:
    if flag == "--images-to-ecr":
      images_to_ecr()
      pass
    elif flag == "--deploy-infra":
      deploy_aws_infrastructure()
    else:
      print("Error: unregcognized flag {}".format(flag))
      return -1
  
  if len(flags) == 0:
    images_to_ecr()
    deploy_aws_infrastructure()



if __name__ == "__main__":
  main()