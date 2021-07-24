import os
image_name = "myfirstdockerimage"

os.environ["INSTANCE_NAME"] = f"instance-{image_name}-1"
os.environ["INSTANCE_TYPE"] = "e2-small"
os.environ["ZONE"] = "us-central1-a"
os.environ["PROJECT"] = "<project>"
os.environ["DOCKER_IMAGE"] = "<image path>"


command = """gcloud compute instances create-with-container $INSTANCE_NAME \
            --project=$PROJECT \
            --zone=$ZONE \
            --service-account=$SERVICE_ACCUNT \
            --machine-type=$INSTANCE_TYPE \
            --container-restart-policy=never \
            --scopes=https://www.googleapis.com/auth/cloud-platform \
            --container-image=$DOCKER_IMAGE \
            --container-env=gce_zone=$ZONE,gce_project_id=$PROJECT
"""

os.system(command)
