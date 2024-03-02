import random
import time

def main():
    questions = [
        {
            'id': 1,
            'question': 'What is 2+2?',
            'options': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
            'answer': 'D'
        },
        {
            'id': 2,
            'question': 'What is the capital of France?',
            'options': ['A. Paris', 'B. London', 'C. Rome', 'D. Berlin'],
            'answer': 'A'
        },
        # Add more questions here
    ]
    
    score = 0
    start_time = time.time()
    
    for question in random.sample(questions, k=len(questions)):
        print(question['question'])
        for option in question['options']:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {question['answer']}.")
        
        print()
    
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print(f"Quiz completed! Your score is {score}/{len(questions)} in {total_time} seconds.")

if __name__ == "__main__":
    main()