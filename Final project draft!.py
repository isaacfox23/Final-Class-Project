
#7f65fe02854020d5c4353eef85ea5e2c
#Api key for weather maps

import requests
#Got this from email and registration in week 2 sent from openweathermaps! They have a lot of great content on how to call their API's if you look it up on google by the way! Could be useful for future students!
def get_web_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    apiid = "7f65fe02854020d5c4353eef85ea5e2c"

    # checking for zip/city!
    if zip is not None:
        baseUrl += "&zip="+str(zip)+",us"
    else:
        baseUrl += "&q="+str(city)+",us"
    baseUrl += "&appid="+str(apiid)
    # using request module
    r = requests.get(baseUrl)
    return r

# Switching format to be readable
def display(resp):
    # if this works it means request is all good!
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} weather today!:
        Sky type -- {data['weather'][0]['description']}
        Wind Speed -- {data['wind']['speed']} mph
        Visibility -- {data['visibility']} meters
        Low temperature -- {data['main']['temp_min']} Degrees Farenheit
        High temperature -- {data['main']['temp_max']} Degrees Farenheit
        """)
    else:
        print("Your request has failed, there was an error try again!: ", resp.status_code)


def main():
    while True:
    # Asking for city or zip, I learned how to do this from the garage project! used the \n also from garage project!
        choice = int(
        input("Type 1 if searching by zip, 2 if by city name, 3 to exit! :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))
        #Using try and excepts to weed out possible errors
        if choice == 1:
            try:
                #lets get the zipcode through user input and call the zipcode
                zipcode = int(input("Please enter zip code : "))
                response = get_web_data(zipcode, None)
                display(response)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 2:
            try:
                #Lets get city through user input and call the city name
                cityname = input("Please enter city name : ")
                response = get_web_data(None, cityname)
                display(response)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 3:
            break
        else:
            print("Invalid Choice..\n")


if __name__ == "__main__":
    main()

#Let me know if I can make any adjustments but I feel pretty good about everything!
#DOing that 20 hours on the garage project really helped me out in this one and it
#made me be sharper on my syntax and let me learn how to look up tips for code like the n\ a lot better too!
#Very Fun project especially using an API!!