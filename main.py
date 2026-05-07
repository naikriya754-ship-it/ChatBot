import os
import logging
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, PermissionDenied, GoogleAPIError
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load env variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.warning("GEMINI_API_KEY is not set in the environment. Please create a .env file.")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

system_instruction = (
    "You are a helpful music assistant chatbot. "
    "Be helpful, not paranoid. Answer general music questions with appropriate disclaimers. "
    "Refuse only serious harm or off-topic asks."
)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction=system_instruction
)

@app.get("/")
async def get_index():
    return FileResponse("code.html")

@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        message = data.get("message")
        history = data.get("history", [])
        
        if not message:
            raise HTTPException(status_code=400, detail="Message is required")

        # Build contents from history and current message
        contents = []
        for msg in history:
            role = "model" if msg["role"] == "assistant" else "user"
            contents.append({"role": role, "parts": [msg["content"]]})
        contents.append({"role": "user", "parts": [message]})

        response = model.generate_content(contents)
        
        return {"response": response.text}
    except ResourceExhausted as e:
        logger.error(f"Rate limit exceeded: {e}")
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
    except PermissionDenied as e:
        logger.error(f"Permission Error: {e}")
        return JSONResponse(status_code=403, content={"detail": str(e)})
    except GoogleAPIError as e:
        logger.error(f"API Error: {e}")
        return JSONResponse(status_code=400, content={"detail": str(e)})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(status_code=500, content={"detail": "something went wrong, please retry"})

@app.post("/vision")
async def vision_endpoint(
    image: UploadFile = File(...),
    message: str = Form("Analyze this image relating to music.")
):
    try:
        image_bytes = await image.read()
        
        parts = [
            {"mime_type": image.content_type, "data": image_bytes},
            message
        ]
        
        response = model.generate_content(parts)
        
        return {"response": response.text}
    except ResourceExhausted as e:
        logger.error(f"Rate limit exceeded: {e}")
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
    except PermissionDenied as e:
        logger.error(f"Permission Error: {e}")
        return JSONResponse(status_code=403, content={"detail": str(e)})
    except GoogleAPIError as e:
        logger.error(f"API Error: {e}")
        return JSONResponse(status_code=400, content={"detail": str(e)})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(status_code=500, content={"detail": "something went wrong, please retry"})
