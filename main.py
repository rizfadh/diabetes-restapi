from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chefboost import Chefboost as chef

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    Age: int
    Gender: Literal['Male', 'Female']
    Polyuria: Literal['Yes', 'No']
    Polydipsia: Literal['Yes', 'No']
    SuddenWeightLoss: Literal['Yes', 'No']
    Weakness: Literal['Yes', 'No']
    Polypaghia: Literal['Yes', 'No']
    GenitalThrush: Literal['Yes', 'No']
    VisualBlurring: Literal['Yes', 'No']
    Itching: Literal['Yes', 'No']
    Irritability: Literal['Yes', 'No']
    DelayedHealing: Literal['Yes', 'No']
    PartialParesis: Literal['Yes', 'No']
    MuscleStiffnes: Literal['Yes', 'No']
    Alopecia: Literal['Yes', 'No']
    Obesity: Literal['Yes', 'No']


model = chef.load_model('model.pkl')

@app.post('/')
async def diabetes_pred(item : model_input):
    input = item.model_dump().values()
    prediction = chef.predict(model, list(input))
    return {
        'data': item.model_dump(),
        'prediction': str(prediction),
    }
