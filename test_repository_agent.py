from agents.repository_agent import RepositoryAgent

agent = RepositoryAgent()

result = agent.analyze(
    "https://github.com/langchain-ai/langgraph"
)

print(result)