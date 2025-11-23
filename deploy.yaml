steps:
  - id: "Build and Push Docker Image"
    name: "gcr.io/cloud-builders/docker"
    entrypoint: "sh"
    args:
    - -c
    - |
      echo "==== Building Docker Image ===="
      docker build -t ${_REGION}-docker.pkg.dev/${_PROJECT_ID}/${_REPO_NAME}/backend-motor-busqueda:latest .

      echo "==== Pushing Docker Image ===="
      docker push ${_REGION}-docker.pkg.dev/${_PROJECT_ID}/${_REPO_NAME}/backend-motor-busqueda:latest

  - id: "Activar Cloud Build B"
    name: gcr.io/cloud-builders/git
    entrypoint: "sh"
    args:
      - -c
      - |
        gcloud builds triggers run "deploy-backend-motor-busqueda-dev" \
          --region=us-east4 \
          --branch="$BRANCH_NAME" 

options:
  logging: CLOUD_LOGGING_ONLY

substitutions:
  _PROJECT_ID: "data-engineer-410822"
  _REGION: "us-east4"
  _REPO_NAME: "backend-motor-busqueda"