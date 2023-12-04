# Diabetes REST API

REST API dapat dengan bebas digunakan. Dibuat menggunakan python dan library sebagai berikut:

-   FastAPI
-   Uvicorn
-   Gunicorn
-   Pydantic
-   Pandas
-   Chefboost

---

Endpoint: https://rizky-restapi.vercel.app/  
Method: POST  
Request Body:

-   `Age` as `int`
-   `Gender` as `"Male" | "Female"`
-   `Polyuria` as `"Yes" | "No`
-   `Polydipsia` as `"Yes" | "No`
-   `SuddenWeightLoss` as `"Yes" | "No`
-   `Weakness` as `"Yes" | "No`
-   `Polypaghia` as `"Yes" | "No`
-   `GenitalThrush` as `"Yes" | "No`
-   `VisualBlurring` as `"Yes" | "No`
-   `Itching` as `"Yes" | "No`
-   `Irritability` as `"Yes" | "No`
-   `DelayedHealing` as `"Yes" | "No`
-   `PartialParesis` as `"Yes" | "No`
-   `MuscleStiffnes` as `"Yes" | "No`
-   `Alopecia` as `"Yes" | "No`
-   `Obesity` as `"Yes" | "No`

Example:

```json
{
    "Age": 0,
    "Gender": "Male",
    "Polyuria": "Yes",
    "Polydipsia": "Yes",
    "SuddenWeightLoss": "Yes",
    "Weakness": "Yes",
    "Polypaghia": "Yes",
    "GenitalThrush": "Yes",
    "VisualBlurring": "Yes",
    "Itching": "Yes",
    "Irritability": "Yes",
    "DelayedHealing": "Yes",
    "PartialParesis": "Yes",
    "MuscleStiffnes": "Yes",
    "Alopecia": "Yes",
    "Obesity": "Yes"
}
```

Response:

```json
{
    "data": {
        "Age": 0,
        "Gender": "Male",
        "Polyuria": "Yes",
        "Polydipsia": "Yes",
        "SuddenWeightLoss": "Yes",
        "Weakness": "Yes",
        "Polypaghia": "Yes",
        "GenitalThrush": "Yes",
        "VisualBlurring": "Yes",
        "Itching": "Yes",
        "Irritability": "Yes",
        "DelayedHealing": "Yes",
        "PartialParesis": "Yes",
        "MuscleStiffnes": "Yes",
        "Alopecia": "Yes",
        "Obesity": "Yes"
    },
    "prediction": "Positive"
}
```

Muhammad Rizky Fadhillah &copy; 2023
