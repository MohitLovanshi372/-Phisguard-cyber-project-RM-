SETUP:

Backend:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Create .env:
HF_TOKEN=your_token
VT_API_KEY=your_key

Frontend:
cd frontend
npm install
npm start
