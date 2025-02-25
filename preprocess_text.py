import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.schema import SystemMessage, HumanMessage

# Load API keys from .env file
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral model
llm = ChatMistralAI(model="mistral-medium", temperature=0.5, mistral_api_key=api_key)

def summarize_text(text):
    messages = [
        SystemMessage(content="You are an AI that summarizes text concisely."),
        HumanMessage(content=f"Summarize this text:\n{text}")
    ]
    summary = llm.invoke(messages)  # Use invoke() to run the model
    return summary.content

# Test Summarization
if __name__ == "__main__":
    sample_text = "Artificial intelligence is transforming industries by automating processes..."
    print("Summary:", summarize_text(sample_text))
