

import json
import random

def load(filename='flashcards.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(data, filename='flashcards.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_flashcard():
    flashcards = load()
    ques = input("Enter the question: ").strip()
    ans = input("Enter the answer: ").strip()

    if not ques or not ans:
        print("Both question and answer are required!")
        return

    flashcard = {
        "question": ques,
        "answer": ans
    }

    flashcards.append(flashcard)
    save(flashcards)
    print("Flashcard added!")

def view():
    fcards = load()
    if not fcards:
        print("No flashcards available!")
        return

    for idx, card in enumerate(fcards, 1):
        print(f"\n Flashcard {idx}")
        print(f"Question: {card['question']}")
        print(f"Answer: {card['answer']}")

def quiz():
    fc = load()
    if not fc:
        print("No flashcards available!")
        return

    random.shuffle(fc)
    correct = 0

    for card in fc:
        print(f"\n {card['question']}")
        user_answer = input("Your Answer: ")

        if user_answer.strip().lower() == card['answer'].strip().lower():
            print("Correct answer!")
            correct += 1
        else:
            print(f" Wrong. Correct Answer: {card['answer']}")

    print(f"\n Quiz Completed! You scored {correct}/{len(fc)}.")

def main():
    while True:
        print("\n Flashcard App Menu:")
        print("1️ Add Flashcard")
        print("2️ View Flashcards")
        print("3️ Quiz Mode")
        print("4️ Exit")

        opt = input("Select an option between 1-4: ").strip()
        if opt == '1':
            add_flashcard()
        elif opt == '2':
            view()
        elif opt == '3':
            quiz()
        elif opt == '4':
            print("Exiting!!")
            break
        else:
            print("Invalid option chosen. Please select between 1-4.")

if __name__ == "__main__":
    main()
