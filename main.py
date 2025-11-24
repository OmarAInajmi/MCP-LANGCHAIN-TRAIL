import asyncio
from dotenv import load_dotenv ,dotenv_values
from mcp import ClientSession , StdioServerParameters
import os
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

load_dotenv()  
llm = ChatOpenAI()
#How to run the mcp server 
stdio_server_params = StdioServerParameters(
    command="python",
    args=["server/math_server.py"],
)
#Line 1: wires connected
#Line 2: phone app opens
#Line 3: call starts
#After line 3: ALL talking goes through the phone app
async def main():
    async with stdio_client(stdio_server_params) as (read,write): # its like running the  python math_server.py and sayig htos is the client 
        async with ClientSession(read_stream=read, write_stream=write)as session:
            await session.initialize()
            print('MCP init')
            tools=await load_mcp_tools(session)
            print(tools)
            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke({
                "messages": [HumanMessage(content="What is 54 + 2*3?")]
            })

            print(result["messages"][-1].content)




if __name__ == "__main__":
    asyncio.run(main())
