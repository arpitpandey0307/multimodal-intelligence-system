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