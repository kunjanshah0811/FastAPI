from fastapi import FastAPI

app=FastAPI()
@app.get("/predicttt")
#decorator

def product_model(age:int,sex:str):
    #below is a rule-based demo model. 
    if  age<15 or sex=='F':
        return{'survived':1}
    else :
        return{'survived':0}
