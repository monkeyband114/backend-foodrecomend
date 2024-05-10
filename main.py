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
        "name": "Turkey and Vegetable Skewers",
        "age_range": (25, 55),
        "weight_range": (55, 80),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (70, 160),
        "nutritional_info": {
            "calories": 160,
            "protein": 20,
            "carbohydrates": 5,
            "fiber": 3,
        }
    },
    {
        "name": "Greek Salad with Chicken",
        "age_range": (25, 55),
        "weight_range": (55, 80),
        "sugar_level_range": (70, 120),
        "cholesterol_range": (70, 95),
        "nutritional_info": {
            "calories": 180,
            "protein": 18,
            "carbohydrates": 10,
            "fiber": 4,
            
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
            
        }
    },
    {
        "name": "Fruit Salad",
        "age_range": (0, 100),
        "weight_range": (80, 200),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (78, 94),  # Assume fruits are cholesterol-free
        "nutritional_info": {
            "calories": 120,
            "protein": 2,
            "carbohydrates": 30,
            "fiber": 5,
            
        }
    },
    {
        "name": " Jollof Rice",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (60, 80),
        "cholesterol_range": (75, 94),  # Assume  Jollof Rice is cholesterol-free
        "nutritional_info": {
            "calories": 250,
            "protein": 6,
            "carbohydrates": 45,
            "fiber": 2,
            
        }
    },
    {
        "name": "Apple",
        "age_range": (0, 100),
        "weight_range": (0, 500),
        "sugar_level_range": (5, 60),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 95,
            "protein": 1,
            "carbohydrates": 25,
            "fiber": 4,
        }
    },
    {
        "name": "Banana",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 105,
            "protein": 1,
            "carbohydrates": 27,
            "fiber": 3,
        }
    },
    {
        "name": "Orange",
        "age_range": (0, 100),
        "weight_range": (0, 300),
        "sugar_level_range": (8, 12),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 62,
            "protein": 1,
            "carbohydrates": 15,
            "fiber": 3,
        }
    },
    {
        "name": "Pineapple",
        "age_range": (0, 100),
        "weight_range": (0, 2000),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 50,
            "protein": 0,
            "carbohydrates": 13,
            "fiber": 1,
        }
    },
    {
        "name": "Watermelon",
        "age_range": (0, 100),
        "weight_range": (0, 10000),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 30,
            "protein": 1,
            "carbohydrates": 8,
            "fiber": 1,
        }
    },
    {
        "name": "Mango",
        "age_range": (0, 100),
        "weight_range": (0, 500),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 135,
            "protein": 1,
            "carbohydrates": 35,
            "fiber": 5,
        }
    },
    {
        "name": "Papaya",
        "age_range": (0, 100),
        "weight_range": (0, 500),
        "sugar_level_range": (20, 55),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 60,
            "protein": 1,
            "carbohydrates": 15,
            "fiber": 3,
        }
    },
    {
        "name": "Guava",
        "age_range": (0, 100),
        "weight_range": (0, 500),
        "sugar_level_range": (5, 12),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 38,
            "protein": 1,
            "carbohydrates": 9,
            "fiber": 4,
        }
    },
    {
        "name": " Pounded Yam and Egusi Soup",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (1, 15),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 450,
            "protein": 10,
            "carbohydrates": 70,
            "fiber": 5,
        }
    },
    {
        "name": " Suya",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (1, 10),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 350,
            "protein": 20,
            "carbohydrates": 5,
            "fiber": 1,
        }
    },
    {
        "name": " Moi Moi",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (50, 94),
        "nutritional_info": {
            "calories": 100,
            "protein": 8,
            "carbohydrates": 15,
            "fiber": 4,
        }
    },
    {
        "name": " Puff Puff",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (60, 94),
        "nutritional_info": {
            "calories": 90,
            "protein": 2,
            "carbohydrates": 15,
            "fiber": 1,
        }
    },
    {
        "name": " Akara",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (75, 94),
        "nutritional_info": {
            "calories": 150,
            "protein": 8,
            "carbohydrates": 10,
            "fiber": 2,
        }
    },
    {
        "name": " Fried Plantain",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 200,
            "protein": 1,
            "carbohydrates": 50,
            "fiber": 3,
        }
    },
    {
        "name": " Efo Riro",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (18, 80),
        "cholesterol_range": (30, 94),
        "nutritional_info": {
            "calories": 300,
            "protein": 10,
            "carbohydrates": 20,
            "fiber": 4,
        }
    },
    {
        "name": " Boli",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (70, 94),
        "nutritional_info": {
            "calories": 250,
            "protein": 2,
            "carbohydrates": 40,
            "fiber": 3,
        }
    },
    {
        "name": " Amala and Ewedu Soup",
        "age_range": (0, 100),
        "weight_range": (0, 200),
        "sugar_level_range": (20, 80),
        "cholesterol_range": (30, 59),
        "nutritional_info": {
            "calories": 400,
            "protein": 10,
            "carbohydrates": 60,
            "fiber": 5,
        }
    }

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
