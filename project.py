import time

def calculate_wpm(start_time, end_time, typed_text):
    # Calculate total time taken in seconds
    total_time = end_time - start_time
    # Split the typed text into words and count them
    word_count = len(typed_text.split())
    # Calculate words per minute (WPM)
    wpm = (word_count / total_time) * 60
    return round(wpm, 2)

def typing_speed_test():
    sample_text = "The quick brown fox jumps over the lazy dog"
    
    print("Welcome to the Typing Speed Test!")
    print("Type the following sentence as quickly and accurately as you can:")
    print("\n" + sample_text + "\n")
    
    # Wait for the user to start typing
    input("Press Enter when you are ready to start...")
    
    # Record the start time
    start_time = time.time()
    
    # User types the sentence
    typed_text = input("\nStart typing here: ")
    
    # Record the end time
    end_time = time.time()
    
    # Calculate WPM
    wpm = calculate_wpm(start_time, end_time, typed_text)
    
    # Display the result
    print(f"\nYou typed: {typed_text}")
    print(f"Your typing speed is: {wpm} words per minute (WPM)")
    
    # Optional: accuracy check (how many words match the sample text)
    accuracy = sum(1 for a, b in zip(typed_text.split(), sample_text.split()) if a == b) / len(sample_text.split()) * 100
    print(f"Your typing accuracy is: {accuracy:.2f}%")
    
if __name__ == "__main__":
    typing_speed_test()
