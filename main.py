import pandas as pd
import numpy as np
def questions_input():
    questions = ["What major are you?",
    "How often do you read?",
    "What kind of books do you read?",
    "Through what medium do you prefer to read?",
    "Do you want to read more?",
    "Why do you like to read?",
    "What stops you from reading if you want to?",
    "Would you prefer to read alone or in a book club / community?",
    "Would you like to discuss the contents of the book? If yes, while or after reading?",
    "Do you have any ideas for what would help you to read more?"]
    results = []
    for q in questions:
        val = input(q)
        results.append(val)
    return results
def questions_toframe(results_list):
    question_frame = pd.DataFrame([],columns=list(range(1,11)))
    for res in results_list:
        question_frame = pd.concat([question_frame,pd.DataFrame([res],columns=list(range(1,11)))],axis=0)
    return question_frame
def export_tocsv(question_frame):
    return question_frame.to_csv("questions.csv",index=False)
def create_answers():
    results = []
    tracker = 0
    while (True):
        tracker += 1
        val = input(f"Please load answers #{tracker}, type 'yes' to begin or type 'quit' to exit")
        if val == "quit":
            break;
        results.append(questions_input())
    export_tocsv(questions_toframe(results))
    print("Save Successfully. Check your folder")
    return
def main():
	create_answers()
if __name__ == "__main__":
	main()
print("SCRIPT RUN LIKE RIVER!")