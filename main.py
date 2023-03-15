import sys
import json, requests
code = str(input("Enter the code: "))
f = open("/media/ritankar/01D7B108A6C349F0/my_work/PythonProjects/WETAR/city_code.json")
codes = json.load(f)
base_url = "https://api.openweathermap.org/data/2.5/weather?"
app_id = "<your api key here>"

res = list(filter(lambda codes: codes['code'] == code, codes))
if 	len(res) == 0:
    print("No codes found")
    sys.exit(1)
city = res[0]['city']
country = res[0]['country']

complete_url = base_url + "q=" + city + "," + country + "&appid=" + app_id

response = requests.get(complete_url)

resp = response.json()

if resp['cod'] != "404":
    c_wet = resp["weather"][0]["id"]
    if c_wet in [200,201,202,210,211,212,221,230,231,232]:
        wet_cd = "TS"
    elif c_wet in [300,301,302,310,311,312,313,314,321]:
        wet_cd = "DZ"
    elif c_wet in [500,501,502,503,504,511,520,521,522,531]:
        wet_cd = "RA"
    elif c_wet in [600,601,602,611,612,613,615,616,620,621,622]:
        wet_cd = "BLSN"
    elif c_wet == 701:
        wet_cd = "BR"
    elif c_wet == 711:
        wet_cd = "FU"
    elif c_wet == 721:
        wet_cd = "HZ"
    elif c_wet in [731,761]:
        wet_cd = "DU"
    elif c_wet == 741:
        wet_cd = "BR"
    elif c_wet == 751:
        wet_cd = "SA"
    elif c_wet == 762:
        wet_cd = "VA"
    elif c_wet == 771:
        wet_cd = "SQ"
    elif c_wet == 781:
        wet_cd = "FC"
    elif c_wet == 800:
        wet_cd = "CLR"
    elif c_wet == 801:
        wet_cd = "FEW"
    elif c_wet == 802:
        wet_cd = "SCT"
    elif c_wet == 803:
        wet_cd = "BKN"
    elif c_wet == 804:
        wet_cd = "OVC"
    else:
        print("Weather id not found: %s" % c_wet)
        sys.exit(1)
    
    c_temp = round(resp["main"]["temp"] - 273)
    

    c_temp_min = resp["main"]["temp_min"]

    c_temp_max = resp["main"]["temp_max"]

    c_pressure = resp["main"]["pressure"]

    c_humidity = resp["main"]["humidity"]

    c_wind_speed = resp["wind"]["speed"]
    c_wind_speed = str(round(c_wind_speed*1.944)) #* from m/s to kt
    c_wind_speed = c_wind_speed.zfill(2)

    c_wind_deg = str(resp["wind"]["deg"])
    c_wind_deg = c_wind_deg.zfill(3)

    c_visibility = resp["visibility"]

    report = f"WETAR {code} {c_wind_deg}{c_wind_speed}KT {wet_cd} {c_temp} Q{c_pressure} "
    print(report)








