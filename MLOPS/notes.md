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