# Workflow-Flask-GCPContainerRegistry


## What's the Google Cloud Container Registry(GCR)?

Container Registry is a single place for your team to manage Docker images, perform vulnerability analysis, and decide who can access what with fine-grained access control.

## What's the Github Actions Workflow?

A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

## What's the Google Kubernetes Engine(GKE)?

Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure.


## What's the Workflow-Flask-GCPContainerRegistry?

If you commit and push any changes on the Flask project;

- A new build is created and automatically hidden.
- The automatically tagged image is pushed to the Google Cloud Container Registry.
- The Flask project deployed on GKE is automatically updated with the newly tagged image.

![Alt text](New_Arch.png?raw=true "Title")
