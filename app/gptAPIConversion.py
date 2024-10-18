from fastapi import FastAPI, HTTPException
from mangum import Mangum

from gptImplementation import MAX_INPUT_LENGTH, getBrandingSnippet, getKeywords

app = FastAPI()

handler = Mangum(app)

#testing if deploy working right 

# there are two paths that recieves requests "/" and "/items/{item_id}"
# both paths do GET HTTP Method 
# Things to note is the /items/ endpoint can be int with "item_id" or a string with "q"

@app.get("/snippet_only")
def getSnippetOnly(msg: str):
  validateInputLength(msg)
  snippet = getBrandingSnippet(msg)
  return {"snippet": snippet, "keywords": []}


@app.get("/keywords_only")
def getKeywordsOnly(msg: str):
  validateInputLength(msg)
  snippet = getBrandingSnippet(msg)
  keywords = getKeywords(snippet)
  return {"snippet": None, "keywords": keywords}


@app.get("/snippet_keywords")
def getSnippetKeywords(msg: str):
  validateInputLength(msg)
  snippet = getBrandingSnippet(msg)
  keywords = getKeywords(snippet)
  return {"snippet": snippet, "keywords": keywords}



# Has its own validate input length, keeping related things together. The chat gpt validation might be redundant but we will look at that later
def validateInputLength(input: str):
  if (len(input) > MAX_INPUT_LENGTH):
    raise HTTPException(status_code = 400, detail=f"Input length is over {MAX_INPUT_LENGTH}")
  return True
