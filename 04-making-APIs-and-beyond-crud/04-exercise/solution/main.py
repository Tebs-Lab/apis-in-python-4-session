import json
import pathlib
import shutil

from fastapi import FastAPI, HTTPException, Body, Response

import reddit
import github

# Some setup code to standardize serialization locations
# and make them if they don't already exist
JUDGEMENTS_DIR = pathlib.Path(__file__).parent / 'judgements'
JUDGEMENTS_DIR.mkdir(exist_ok=True)
MOST_WHOLESOME = JUDGEMENTS_DIR / 'current_most_wholesome'
MOST_WHOLESOME.touch()

app = FastAPI()

@app.get("/serialize_todays_aholes")
def serialize_todays_aholes():
    reddit.save_todays_aholes(JUDGEMENTS_DIR)
    return Response(status_code=200)

@app.get("/refresh_most_wholesome")
def refresh_most_wholesome():
    best_ratio = 0
    most_wholesome = None
    output_dir = pathlib.Path(__file__).parent / 'judgments'
    for judgement in output_dir.iterdir():
        if judgement == MOST_WHOLESOME: 
            continue

        with open(judgement, 'r') as f:
            votes = json.load(f)
            ratio = reddit.compute_NTA_ratio(votes)
        
        if ratio > best_ratio:
            most_wholesome = judgement

    shutil.copy(most_wholesome, MOST_WHOLESOME)

    return Response(status_code=200)


@app.get("/current_most_wholesome")
def get_most_wholesome():
    with open(MOST_WHOLESOME, 'r') as f:
        votes = json.load(f)

    return votes


@app.get("/update_wholesome_gist")
def update_wholesome_gist():
    with open(MOST_WHOLESOME, 'r') as f:
        votes = f.read()

    # For fun, I decided to return the github response.
    # helps with debugging sometimes.
    github_response = github.upload_to_gist(votes)
    return github_response

@app.post('/judgements')
def manually_create_judgement(filename: str = Body(), situation: str = Body(), YTA: int = Body(), NTA: int = Body(), NAH: int = Body(), ESH: int = Body()):
    votes = {
        'situation': situation,
        'YTA': YTA,
        'NTA': NTA,
        'ESH': ESH,
        'NAH': NAH
    }
    
    with open(JUDGEMENTS_DIR / filename, 'w') as f:
        json.dump(votes, f)

    return Response(votes, status_code=201)

@app.delete('/judgements')
def delete_judgements():
    for judgement in JUDGEMENTS_DIR.iterdir():
        judgement.unlink()

    return Response(status_code=200)
    