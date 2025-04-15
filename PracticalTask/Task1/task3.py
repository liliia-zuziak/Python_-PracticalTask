import re
from collections import Counter

def extract_user_agents(file_path):
    user_agents = []

    try:
        with open(file_path, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                match = re.findall(r'"(.*?)"', line)
                if match:
                    user_agent = match[-1]
                    user_agents.append(user_agent)

        return user_agents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    print("Access Log User-Agent Analyzer")

    file_path = input("Enter the path to the access.log file: ").strip()

    user_agents = extract_user_agents(file_path)

    if user_agents is not None:
        count = Counter(user_agents)
        print(f"\nTotal unique User-Agents: {len(count)}\n")

        print("Request count per User-Agent:")
        for agent, num in count.most_common():
            print(f"• {agent} — {num} request(s)")
