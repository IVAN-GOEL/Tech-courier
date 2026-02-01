from timeupdate import GEThour

def Input ():

    print("*********************\n\n")

    print("Welcome to TechNews your personalized source for the latest updates in technology"
          " and allied fields, delivered straight to your Telegram")
    print("\n\n")
    while True:
        try:
            topicno = int(input("how many topics do you wish to stay informed on ??"
             "(we recommend 5-6) topic"))
            if(topicno<=0):
                print("you have entered a negative number,please try again\n")
                continue
            if(topicno>20):
                print("please consider reducing the number of topics you wish to stay in for better results\n")
            break
        except ValueError:
            print("please enter a valid number\n")

    print("What are the 5 major topics you would like to stay Informed on ??\n(please select tech related topics like "
          "\"python,html,hackathons,ai etc\"")
    topics=[]
    i = 1
    while len(topics) < topicno:
        topic = input(f"Please enter topic {i}: ").strip().lower()

        if not topic:
            print("Topic cannot be empty.\nplease try again.\n")

            continue

        if topic in topics:
            print("Topic already added. Please enter a different one.\n")
            continue
        topics.append(topic)
        i += 1

    print("great!,topics saved")
    return topics


def get_telegram_id():
    while True:
        chat_id = input("Please enter your Telegram Chat ID: ").strip()

        if not chat_id:
            print(" Chat ID cannot be empty.Try again.\n")
            continue

        # Chat ids are numeric
        if not (chat_id.lstrip("-").isdigit()):
            print(" Invalid Chat ID. It should be a number.\n")
            continue

        print("Telegram chat id saved!\n")
        return chat_id