user_data = {
    "Name": "Mr Ali Ahmed",
    "Age": 30,
    "Email": "aliahmed@gmail.com",
    "Creator": "Feras Hussien Farouq"
}

username = "aliahmed"
password = "12345678"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Please Enter username: ")
    pass_input = input("Please Enter password: ")

    if user_input == username and pass_input == password:
        print(f"\nWelcome, {user_data['Name']}!")
        print("Here is your requested data:")
        print("this program was written by Feras Hussein Farouq")
        print("Thank you for using!")
        for key, value in user_data.items():
            print(f"{key}: {value}")
        break
    else:
        attempts += 1
        print(f"Incorrect username/password. Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        user_data.clear()
        print("\nSorry!, Attempt Limit Exceeded!. All data has been deleted!")