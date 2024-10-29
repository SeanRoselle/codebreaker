import random

def generate_guess():
    return f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

def get_feedback(guess, secret_code):
    if guess == secret_code:
        return "Correct!"
    else:
        correct_digits = sum(1 for g, s in zip(guess, secret_code) if g == s)
        return f"{correct_digits} digit(s) are correct."

def main():
    secret_code = input("Enter a 3-digit code for me to guess (don't tell me!): ")
    
    attempts = 0
    while True:
        guess = generate_guess()
        attempts += 1
        print(f"Attempt {attempts}: My guess is {guess}")
        
        feedback = get_feedback(guess, secret_code)
        print(feedback)
        
        if feedback == "Correct!":
            print(f"I guessed the code {secret_code} in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()