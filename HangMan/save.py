""" This is Save """
def main():
    """ save Function"""
    state = 0
    # file = open("catagory/england.json","w")
    # output = ['Aresenal', 'Chelsea', 'Manchester United', 'Manchester City', 'Liverpool',\
    # 'Tottenham Hotspur']

    # file = open("catagory/mcu.json","w")
    # output = ['Iron man', 'Groot', 'Captain America', 'Thanos', 'Black Panther',\
    # 'Spider-man','Thor','Docotor Strange','Ant-man','Captain Marvel','Black Widow','Hawkeye']

    # file = open("catagory/football.json","w")
    # output = ['Eden Hazard', 'Messi', 'Cristiano Ronaldo', 'David de Gea', 'David Beckham',\
    # 'Steven Gerrard','Didier Drogba','Harry Kane','Chanathip Songkrasin','Teerasil Dangda','Kawin Thamsatchanan','Jakub Blaszcykowski',\
    # 'Kepa Arrizabalaga','Cesar Azpilicueta']

    # file = open("catagory/hollywood.json","w")
    # output = ['Robert Downey Jr.', 'Chris Hemsworth', 'Evangeline Lilly', 'Tom Holland', 'Samuel L. Jackson',\
    # 'Scarlet Johansson','Mark Ruffalo','Tom Cruise','Will Smith']

    file = open("catagory/country.json","w")
    output = ['Thailand', 'United States of America', 'Germany', 'Italy', 'Spain',\
    'England']


    for i in output:
        sentense = ""
        rad = [1,3,5,7,9]
        for j in range(len(i)):
            if(j%2==0 and i[j] != " "):
                sentense += chr(ord(i[j])+rad[j%4])
            else:
                sentense += i[j]
        output[state] = sentense
        state += 1
    file.write(str(output))
    file.close()
main()