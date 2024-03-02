Task ouput(images) and description given below:

Level-1_Task-1_Number_Guessing_Game:                   
  This Python code defines a simple number guessing game. Here's a brief description of how it works:
  1.A random number between 1 and 100 is generated using the random.randint(1, 100) function.
  2.The user is prompted to guess the number.
  3.If the user's guess is out of range (less than 1 or greater than 100), a ValueError is raised, and the user is prompted to enter a valid guess again.
  4.If the user's guess is incorrect, the program prints a hint (either "Too low! Try again." or "Too high! Try again.") and prompts the user to guess again.
  5.Once the user's guess matches the randomly generated number, the program prints "Congratulations! You guessed the correct number." and terminates.
    The game is designed to provide feedback and guide the user to the correct answer, making it suitable for educational purposes or casual entertainment. It also demonstrates basic error handling and the use of the random module in Python.
   
   evel-1_Task-1_Number_Guessing_Game OUTPUT:
    ![Level-1_Task-1_Number_Guessing_Game](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/adddc26a-0e3e-4c45-92bb-057b03c3312e)
    
Level-1_Task-2_Countdown_Clock:              
    The code defines a Python function named countdown that takes a single parameter end_datetime. The function continuously calculates and prints the remaining time until end_datetime is reached.
  The provided end_datetime is set to March 2, 2024, at 11:00 PM (23:00).
  The function countdown:
  1.Enters an infinite loop.
  2.Retrieves the current date and time using datetime.datetime.now().
  3.Calculates the remaining time by subtracting the current time from end_datetime.
  4.Prints the remaining time in days, hours, minutes, and seconds.
  5.Pauses the program execution for one second using time.sleep(1) to prevent excessive CPU usage.
  6.Breaks out of the loop and prints "Countdown expired!" if the remaining time is negative (i.e., if the countdown has expired).
  The countdown function can be used to create a countdown timer for various purposes, such as tracking the time remaining until a specific event or deadline. However, it currently only prints the remaining time to the console; additional coding would be needed to integrate it into a GUI or to add other functionalities.
  To use this code, you can change the end_datetime variable to specify a different end date and time for the countdown.
  
  Level-1_Task-2_Countdown_Clock OUTPUT:
  ![Level-1_Task-2_Countdown_Clock](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/d7ef90cd-f1b1-4d3d-a275-925af27154e0)
  
Level-1_Task-3_Quiz_Application:                
   The provided Python code defines a simple quiz program that asks random multiple-choice questions and calculates the user's score based on the correctness of their answers.
   Here's how the code works:
 1.Questions Data: The quiz questions are stored as a list of dictionaries in the questions variable. Each dictionary represents a question and contains the question text, options, and correct answer.
 2.Quiz Execution: The main() function runs the quiz. It initializes the score to 0 and starts a timer to record the total time taken to complete the quiz.
 3.Question Selection: The random.sample() function is used to shuffle the questions list and select questions randomly. This ensures that the questions are asked in random order.
 4.Question Presentation: For each question, the program prints the question text and all the available options. The user is prompted to enter their answer (A, B, C, or D).
 5.Answer Evaluation: If the user's answer matches the correct answer, the program prints "Correct!" and increments the score by 1. Otherwise, it prints the correct answer.
 6.Score Calculation: At the end of the quiz, the program calculates the total time taken and prints the user's score out of the total number of questions, along with the time taken to complete the quiz.
 7.Running the Quiz: The main() function is executed only if the script is run directly (not imported as a module) using the if __name__ == "__main__": construct.
   The user can interact with the quiz by entering their answers to the questions presented. The program provides feedback on the correctness of the answers and gives a final score at the end.
   To use this code, you can customize the questions variable byask adding more questions or modifying the existing ones.
   
   Level-1_Task-3_Quiz_Application OUTPUT:
   ![Level-1_Task-3_Quiz_Application](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/04ba6d5d-9541-40ea-977a-f84ac5c91556)

Level-2_Task-1_Credit_Card_Validator:          
   The provided Python code defines a function named validate_credit_card that uses the Luhn algorithm to validate a credit card number. The Luhn algorithm is a checksum formula used to validate a variety of identification numbers, such as credit card numbers.
   Here's a breakdown of how the code works:
   1.Input Validation: The input card_number is processed using re.sub(r'\D', '', card_number), which removes all non-numeric characters from the input.
   2.Length and Digits Check: The function checks if the length of the card_number is 16 digits and if the card number contains only digits using len(card_number) != 16 and not card_number.isdigit().
   3.Luhn Algorithm Implementation: The Luhn algorithm is applied to the card_number using the following steps:
    ~Reverse the card_number and iterate over each digit, starting from the right.
    ~For each digit, double the value if it's in an odd position (i.e., i % 2 == 0).
    ~If the doubled value is greater than 9, subtract 9 from it.
    ~Add the resulting values to a total variable.
    ~If the sum of all values modulo 10 equals 0, the credit card number is valid.
  4.Output: The function returns True if the credit card number is valid according to the Luhn algorithm and False otherwise.
  5.User Input and Result Display: The user is prompted to enter a credit card number. The validate_credit_card function is called to validate the input, and the result is printed as either "Valid credit card number!" or "Invalid credit card number."
   This code can be used to quickly validate a credit card number based on the Luhn algorithm. It is a simple implementation and doesn't include additional checks such as the card's issuer or expiration date.  
    
     Level-2_Task-1_Credit_Card_Validator OUTPUT:
    ![Level-2_Task-1_Credit_Card_Validator](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/c8b298c6-73bc-4f27-8096-686d0337db23)

Level-2_Task-2_Location_Finder:        
   This code defines a Python function named get_user_location that uses the Nominatim class from the geopy.geocoders module to get the GPS coordinates of a user's location based on their input (e.g., city, country). Here's a summary of the code's functionality:
   1.Importing Necessary Libraries: The code imports the Nominatim class from the geopy.geocoders module.
   2.Function Definition: The get_user_location function is defined to fetch the user's GPS coordinates. Within this function:
     ~A Nominatim object named geolocator is created with a user-defined user agent ("location_app").
     ~A while loop is used to continuously prompt the user to enter their location until a valid location is provided.
     ~Inside the loop, the user is asked to enter their location (e.g., city, country), and the geolocator.geocode method is used to get the GPS coordinates based on this input.
     ~If an error occurs during the geocoding process, the exception is caught, and an error message is displayed. The user is then prompted to enter their location again.
     ~When a valid location is entered, the GPS coordinates (latitude and longitude) are printed to the console.
   3.Main Function Call: The if __name__ == "__main__": block is used to call the get_user_location function when the script is executed directly. This ensures that the code inside the if block is executed only when the script is run as the main program. 
   Overall, this code provides a simple way to obtain the GPS coordinates of a user's location using the geopy library. The user is prompted to input their location, and the script returns the latitude and longitude.
  
   Level-2_Task-2_Location_Finder OUTPUT:
  ![Level-2_Task-2_Location_Finder](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/56506103-6d91-4c39-accb-754e10483ad5)

Level-2_Task-3_Document_Scanner:              
  This Python code is designed to perform basic document scanning and edge detection using the OpenCV library. Here's a breakdown of the code's functionality:
  1.Library Import: The code imports the necessary libraries, including cv2 for image processing and numpy for numerical operations.
  2.Image Capture or Loading: The cv2.imread function is used to load an existing image named 'level3.jpg'. Alternatively, you can use a webcam to capture an image.
  3.Image Processing: The loaded image is processed to enhance document visibility. The color image is converted to grayscale using cv2.cvtColor, and then Gaussian blurring is applied using cv2.GaussianBlur. Finally, Canny edge detection is performed using cv2.Canny.
  4.Document Edge Detection: The contours of the document edges are detected using cv2.findContours. The contours are sorted by area in descending order, and the largest contour is selected as the document boundary. The boundary is drawn on the original image using cv2.drawContours.
  5.Saving the Scanned Document: The scanned document is saved as an image using cv2.imwrite. You can change the file format or name as needed.
  6.Displaying the Scanned Document: The scanned document is displayed in a window named 'Scanned Document' using cv2.imshow. The window remains open until a key is pressed (cv2.waitKey), after which it is closed using cv2.destroyAllWindows.
    This code provides a basic document scanning and edge detection functionality using OpenCV, which can be further extended and customized based on specific requirements.

   Level-2_Task-3_Document_Scanner OUTPUT:
  ![Level-2_Task-3_Document_Scanner](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/da328821-c0c1-4cbe-a775-af7fe4cfe438)

Level-3_Task-2_Payment_application:                  
  This Python code defines a process_payment function that simulates processing a payment of a specified amount. 
  The main function prompts the user to enter a payment amount. If the entered amount is not a positive number, a ValueError is raised, and the payment fails. Otherwise, the payment is successfully processed.

   Level-3_Task-2_Payment_application OUTPUT:
  ![level-3_Task-2_Payment_Application](https://github.com/Charansaiponugoti/TAI-IP/assets/160638909/d693d3ac-be80-40bb-ac42-e0aa2a983218)











  






    







   










  






