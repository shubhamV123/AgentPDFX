import os
from agentpdfx.agent import create_agent


def main():
    pdf_path = os.path.abspath("data/thai_recipies.pdf")
    print(os.path.abspath('data'))
    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found at {pdf_path}")
        return

    agent = create_agent(pdf_path);
    print("✅ AgentPDFX is ready. Ask your question!")

    while True:
        user_input = input("🧠 You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            break

        agent.print_response(user_input, markdown=True)
        # print("🤖 AgentPDFX:", response)

if __name__ == "__main__":
    main()