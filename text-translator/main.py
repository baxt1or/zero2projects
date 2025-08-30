from fastapi import FastAPI, BackgroundTasks
from schemas import Translation
from tasks import store_translation, run_translation, find_translation


app = FastAPI()


# Route 1: /
# Checking weather if everything is just working
@app.get("/")
async def get_root():
    return {"message":"Hello World!"}


# Route 2: /translate
# Take in a translation request, and store it to db
# Return a translation_id
@app.post("/translate")
async def post_translation(t: Translation, background_tasks : BackgroundTasks):
    
    # store translation
    t_id = store_translation(t=t)
    run_translation(t_id)
    return {"translation" : find_translation(t_id)}




