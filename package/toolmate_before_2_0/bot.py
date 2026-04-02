from toolmate.autocaptain import AutoCaptainAgent
from toolmate.autobuild import AutoGenBuilder
from toolmate import print2

def main():
    print2("Welcome to the AI Assistant Bot")
    print("Choose the mode:")
    print("1. Agent Dispatcher (CaptainAgent)")
    print("2. Agent Creator (AgentBuilder)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        bot = AutoCaptainAgent()
        task = input("Enter your task: ")
        bot.getResponse(task)
    elif choice == "2":
        bot = AutoGenBuilder()
        task = input("Enter your task: ")
        bot.getResponse(task, coding=True)
    else:
        print("Invalid choice. Exiting.")

if __name__ == '__main__':
    main()
