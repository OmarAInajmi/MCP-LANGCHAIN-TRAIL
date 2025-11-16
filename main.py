import asyncio
from dotenv import load_dotenv ,dotenv_values
import os
load_dotenv()  
print(os.getenv('OPENAI_API_KEY'))
async def main():
    print("Hello from mcpserver-trail!")


if __name__ == "__main__":
    asyncio.run(main())
