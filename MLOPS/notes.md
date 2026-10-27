Step 1: Create virtual environment
python -m venv kiet-cse

Step 2: Activate virtual environment
kiet-cse\scripts\activate

Step 3: Create project strcutres
mkdir mlops-first-pipeline
cd malops-first-pipeline

Step 4: Install required packages
 pip install -r requirements.txt

 Step 5: Train and save model
 python train.py

Step 6: Create and start fast api
uvicorn main:app --reload

-----------------------------------
Phase -2: Dockerize ML Application
-----------------------------------
Traditional ML flow:
Dataset->Train->Model Evalutation-> Prediction

Production Ready ML Application
Saved Model -> Python App -> REST API -> Automated Test -> Docker Container -> CI/CD
Can be tested, deployed, accessed by clients and maintained consistently

why do we need docker??
- Imagine right now ML application is working on your mackbook, but fails on another engineer laptop that run it on a linux/windows server

Possiible reasons of failure
-Diffrent Python Versions
-Diffrent versions of scikit learn/fast api/any other packages
-Missing packages of python
-Diffrent Os dependencies

Docker helps packages your application code,runtime,dependencies, and startup instructions into a standardized image

4 major requirements
-Docker file -> Instrutctions for packaaging the ML applications
-Image -> Packaged reusable application artifacts
-Container -> Running instaces of that images
-Port Mapping -> Makes the api inside the container accessible from your system

Commands for docker
1. docker ps = print all running commands
2. docker ps -a = print all active/non-acctive containers
3. docker build -t cse-mlops .
= build docker image
-t = tag = name of the image
4. docker images = List locally avaialable docker images
5. Start the container:
    docker run -d --name iris-ml-api -p 8000:8000 cse-mlops


------------------------------------------------------------------
Phase -3 : Automated Testing and CI/CD pipeline and Github actions
------------------------------------------------------------------

what's our Goal?
Developer pushes cpde to github
Github actions start the workflow
Triggered by a push or pull request

Run tests:
Validate model API behavior
Build image
Verify Docker Packaging

What is CI/CD?
    - CI - Continuous Integration: Automatically validates code changes through tests and build checks
    - CD - Continuous Delivery: Keeps changes ready for release, with production release potentially requiring approval
    - CD - Continuous Deployement: AUtomatically release changes to production when all required checks pass

Automated Testing
    -Automated testing catches issues before a changes move to production
    -pytest + fastapi test client + github actions

Update the project structure
 -mlops-first-pipeline
 ------tests
 -----------test_api.py
 ------.github
 -----------workflows
 ----------------ci.yml

Now install 2 new pacakges:
-httpx: fast api test client uses HTTPx tosimulate http request to your application
-pytest: it discovers and run automated tests, report failures, and returns non zero exit status when test fails

pip install httpx pytest

Run test Locally:
    python -m pytest -v


Now Create a github action workflow

   push the project to the Github
   Commands:- 
   git init
   git add .
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/Xxierrr/mlops-first-pipeline.git
   git push -u origin main

   Progress so far :
   Train model and create Fast API application - Done 
   Conatinerize the application with Docker - Done 
   Automated tests with Github CI - Done 
   Experiment tracking and model registery with MLFlow - Next Step 
   Container registery and cloud deployment
   Production monitoring and drift detection
   Automated traning and model prediction

=========================================================
PHASE 4: MLFlow - Experiment Tracking and Model Registery 
=========================================================
why do we need MLFlow?
- Imagine you train a model multiple times, changing the parameters or data version
- Without experiment tracking you might end up with files like model_v1.joblib, model_v2.joblib, model_final.joblib
- MLFlow helps us maintain that record

Training experiments
-Model paramenters, dataset details and evalutation result

MLFlow Tracking
-Records parameters, metrics, run information and model artifacts

MLFlow Model Registry
-Organize model versions, metadata and lifecycle management

Deployment pipeline
-Select , validate and deploy approved model version

4 major concepts:
-Experiment -> collection of related training runs
-Run -> one execution of training with specific parameters and results
-Artifacts -> saved file produced by a run, such as trained model or evaluation report
-Model Registry -> maanged catalog

Install mflow
-pip install mlflow

Evaluate and promote model versions
-We will add a validation gate that check model quality before allowing a model version to be considered for deployement 

Promote a validated model using champion alias
-OUr fastapi application loads a model from a local file
-this works for demo purpose but becomes harder to manage when you have a multiple model versions

-Instead of hardcoding a file path or version, we can assign the alias champion to the model version we want out application to use