#CREATE a chatbot that will interact with the browser using the playwright mcp server
import os
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient


async def run_memory_chat():
    #load env variables for API keys
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    # configure the file path - change this to your config file
    config_file = "browser_mcp.json"
    print("Initializing chat...")

    # create mcp client and agent with memory enable
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="llama3-8b-8192")

    # create agent with memory_enabled=True
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("\n==== Interactive MCP Chat ====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear history")
    print("==================================\n")
    # main chat loop
    try:
        while True:
            #get user input
            user_input = input("\nYou: ")
            #check for exti command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation!")
                break
            
            #check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared!")
                continue

            #get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                #run the agent with the user input
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()
    
if __name__ == "__main__":
    asyncio.run(run_memory_chat())