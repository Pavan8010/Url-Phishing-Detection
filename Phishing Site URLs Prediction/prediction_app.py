#--------------------------------Updated code with integration of UI-------------------------------#
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the model
phish_model = joblib.load('phishing.pkl')

# ML Aspect
@app.get('/predict/', response_class=HTMLResponse)
async def predict(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/predict/', response_class=HTMLResponse)
async def predict_post(request: Request, features: str = Form(...)):
    X_predict = [features]
    y_Predict = phish_model.predict(X_predict)
    if y_Predict[0] == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"

    return templates.TemplateResponse("index.html", {"request": request, "features": features, "result": result})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)


#-----------------------------------Previous code for reference-----------------------------------#  

# import uvicorn
# from fastapi import FastAPI
# import joblib,os

# app = FastAPI()

# #pkl
# phish_model = open('phishing.pkl','rb')
# phish_model_ls = joblib.load(phish_model)

# # ML Aspect
# @app.get('/predict/{feature}')
# async def predict(features):
# 	X_predict = []
# 	X_predict.append(str(features))
# 	y_Predict = phish_model_ls.predict(X_predict)
# 	if y_Predict == 'bad':
# 		result = "This is a Phishing Site"
# 	else:
# 		result = "This is not a Phishing Site"

# 	return (features, result)
# if __name__ == '__main__':
# 	uvicorn.run(app,host="127.0.0.1",port=8000)