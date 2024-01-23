from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    age: int
    weight: float
    sugar_level: float
    cholesterol_level: float
    time_of_day: str

all_diabetic_friendly_foods = [
    {
        "name": "Grilled Salmon",
        "age_range": (30, 60),
        "weight_range": (60, 90),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (100, 180),
        "nutritional_info": {
            "calories": 200,
            "protein": 25,
            "carbohydrates": 0,
            "fiber": 0,
        }
    },
    {
        "name": "Turkey and Vegetable Skewers",
        "age_range": (25, 55),
        "weight_range": (55, 80),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (90, 160),
        "nutritional_info": {
            "calories": 160,
            "protein": 20,
            "carbohydrates": 5,
            "fiber": 3,
            # Add more nutritional information as needed
        }
    },
    {
        "name": "Spinach and Mushroom Omelette",
        "age_range": (20, 50),
        "weight_range": (50, 75),
        "sugar_level_range": (80, 110),
        "cholesterol_range": (80, 140),
        "nutritional_info": {
            "calories": 150,
            "protein": 12,
            "carbohydrates": 5,
            "fiber": 2,
            # Add more nutritional information as needed
        }
    },
    {
        "name": "Grilled Asparagus",
        "age_range": (25, 60),
        "weight_range": (55, 85),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (80, 150),
        "nutritional_info": {
            "calories": 30,
            "protein": 3,
            "carbohydrates": 5,
            "fiber": 3,
            # Add more nutritional information as needed
        }
    },
    {
        "name": "Cauliflower Rice Stir-Fry",
        "age_range": (30, 65),
        "weight_range": (60, 90),
        "sugar_level_range": (75, 120),
        "cholesterol_range": (90, 160),
        "nutritional_info": {
            "calories": 120,
            "protein": 5,
            "carbohydrates": 15,
            "fiber": 5,
            # Add more nutritional information as needed
        }
    },
    {
        "name": "Greek Salad with Chicken",
        "age_range": (25, 55),
        "weight_range": (55, 80),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (90, 160),
        "nutritional_info": {
            "calories": 180,
            "protein": 18,
            "carbohydrates": 10,
            "fiber": 4,
            # Add more nutritional information as needed
        }
    },
    # Add more foods as needed
]

def get_diabetic_friendly_suggestions(user_data):
    suggestions = []

    for food in all_diabetic_friendly_foods:
        if (
            food["age_range"][0] <= user_data.age <= food["age_range"][1] and
            food["weight_range"][0] <= user_data.weight <= food["weight_range"][1] and
            food["sugar_level_range"][0] <= user_data.sugar_level <= food["sugar_level_range"][1] and
            food["cholesterol_range"][0] <= user_data.cholesterol_level <= food["cholesterol_range"][1]
        ):
            suggestions.append(food["name"])

    return suggestions

@app.post("/recommend")
async def recommend_food(user_data: UserInput):
    suggestions = get_diabetic_friendly_suggestions(user_data)
    
    if not suggestions:
        raise HTTPException(status_code=404, detail="No suitable food suggestions found for the provided user data")

    return {"suggestions": suggestions}
