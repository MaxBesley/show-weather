#  File   : show_weather.py
#  Author : Max Besley
#  Purpose: Shows you the weather through the command line

import json
import requests
from pprint import pprint
from argparse import ArgumentParser

# constants
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
COUNTRY_DATA_FILENAME = 'countries.json'
#countries = [{"Code":"AF","Name":"Afghanistan"},{"Code":"AX","Name":"ÅlandIslands"},{"Code":"AL","Name":"Albania"},{"Code":"DZ","Name":"Algeria"},{"Code":"AS","Name":"AmericanSamoa"},{"Code":"AD","Name":"Andorra"},{"Code":"AO","Name":"Angola"},{"Code":"AI","Name":"Anguilla"},{"Code":"AQ","Name":"Antarctica"},{"Code":"AG","Name":"AntiguaandBarbuda"},{"Code":"AR","Name":"Argentina"},{"Code":"AM","Name":"Armenia"},{"Code":"AW","Name":"Aruba"},{"Code":"AU","Name":"Australia"},{"Code":"AT","Name":"Austria"},{"Code":"AZ","Name":"Azerbaijan"},{"Code":"BS","Name":"Bahamas"},{"Code":"BH","Name":"Bahrain"},{"Code":"BD","Name":"Bangladesh"},{"Code":"BB","Name":"Barbados"},{"Code":"BY","Name":"Belarus"},{"Code":"BE","Name":"Belgium"},{"Code":"BZ","Name":"Belize"},{"Code":"BJ","Name":"Benin"},{"Code":"BM","Name":"Bermuda"},{"Code":"BT","Name":"Bhutan"},{"Code":"BO","Name":"Bolivia,PlurinationalStateof"},{"Code":"BQ","Name":"Bonaire,SintEustatiusandSaba"},{"Code":"BA","Name":"BosniaandHerzegovina"},{"Code":"BW","Name":"Botswana"},{"Code":"BV","Name":"BouvetIsland"},{"Code":"BR","Name":"Brazil"},{"Code":"IO","Name":"BritishIndianOceanTerritory"},{"Code":"BN","Name":"BruneiDarussalam"},{"Code":"BG","Name":"Bulgaria"},{"Code":"BF","Name":"BurkinaFaso"},{"Code":"BI","Name":"Burundi"},{"Code":"KH","Name":"Cambodia"},{"Code":"CM","Name":"Cameroon"},{"Code":"CA","Name":"Canada"},{"Code":"CV","Name":"CapeVerde"},{"Code":"KY","Name":"CaymanIslands"},{"Code":"CF","Name":"CentralAfricanRepublic"},{"Code":"TD","Name":"Chad"},{"Code":"CL","Name":"Chile"},{"Code":"CN","Name":"China"},{"Code":"CX","Name":"ChristmasIsland"},{"Code":"CC","Name":"Cocos(Keeling)Islands"},{"Code":"CO","Name":"Colombia"},{"Code":"KM","Name":"Comoros"},{"Code":"CG","Name":"Congo"},{"Code":"CD","Name":"Congo,theDemocraticRepublicofthe"},{"Code":"CK","Name":"CookIslands"},{"Code":"CR","Name":"CostaRica"},{"Code":"CI","Name":"C\u00f4ted'Ivoire"},{"Code":"HR","Name":"Croatia"},{"Code":"CU","Name":"Cuba"},{"Code":"CW","Name":"Cura\u00e7ao"},{"Code":"CY","Name":"Cyprus"},{"Code":"CZ","Name":"CzechRepublic"},{"Code":"DK","Name":"Denmark"},{"Code":"DJ","Name":"Djibouti"},{"Code":"DM","Name":"Dominica"},{"Code":"DO","Name":"DominicanRepublic"},{"Code":"EC","Name":"Ecuador"},{"Code":"EG","Name":"Egypt"},{"Code":"SV","Name":"ElSalvador"},{"Code":"GQ","Name":"EquatorialGuinea"},{"Code":"ER","Name":"Eritrea"},{"Code":"EE","Name":"Estonia"},{"Code":"ET","Name":"Ethiopia"},{"Code":"FK","Name":"FalklandIslands(Malvinas)"},{"Code":"FO","Name":"FaroeIslands"},{"Code":"FJ","Name":"Fiji"},{"Code":"FI","Name":"Finland"},{"Code":"FR","Name":"France"},{"Code":"GF","Name":"FrenchGuiana"},{"Code":"PF","Name":"FrenchPolynesia"},{"Code":"TF","Name":"FrenchSouthernTerritories"},{"Code":"GA","Name":"Gabon"},{"Code":"GM","Name":"Gambia"},{"Code":"GE","Name":"Georgia"},{"Code":"DE","Name":"Germany"},{"Code":"GH","Name":"Ghana"},{"Code":"GI","Name":"Gibraltar"},{"Code":"GR","Name":"Greece"},{"Code":"GL","Name":"Greenland"},{"Code":"GD","Name":"Grenada"},{"Code":"GP","Name":"Guadeloupe"},{"Code":"GU","Name":"Guam"},{"Code":"GT","Name":"Guatemala"},{"Code":"GG","Name":"Guernsey"},{"Code":"GN","Name":"Guinea"},{"Code":"GW","Name":"Guinea-Bissau"},{"Code":"GY","Name":"Guyana"},{"Code":"HT","Name":"Haiti"},{"Code":"HM","Name":"HeardIslandandMcDonaldIslands"},{"Code":"VA","Name":"HolySee(VaticanCityState)"},{"Code":"HN","Name":"Honduras"},{"Code":"HK","Name":"HongKong"},{"Code":"HU","Name":"Hungary"},{"Code":"IS","Name":"Iceland"},{"Code":"IN","Name":"India"},{"Code":"ID","Name":"Indonesia"},{"Code":"IR","Name":"Iran,IslamicRepublicof"},{"Code":"IQ","Name":"Iraq"},{"Code":"IE","Name":"Ireland"},{"Code":"IM","Name":"IsleofMan"},{"Code":"IL","Name":"Israel"},{"Code":"IT","Name":"Italy"},{"Code":"JM","Name":"Jamaica"},{"Code":"JP","Name":"Japan"},{"Code":"JE","Name":"Jersey"},{"Code":"JO","Name":"Jordan"},{"Code":"KZ","Name":"Kazakhstan"},{"Code":"KE","Name":"Kenya"},{"Code":"KI","Name":"Kiribati"},{"Code":"KP","Name":"Korea,DemocraticPeople'sRepublicof"},{"Code":"KR","Name":"Korea,Republicof"},{"Code":"KW","Name":"Kuwait"},{"Code":"KG","Name":"Kyrgyzstan"},{"Code":"LA","Name":"LaoPeople'sDemocraticRepublic"},{"Code":"LV","Name":"Latvia"},{"Code":"LB","Name":"Lebanon"},{"Code":"LS","Name":"Lesotho"},{"Code":"LR","Name":"Liberia"},{"Code":"LY","Name":"Libya"},{"Code":"LI","Name":"Liechtenstein"},{"Code":"LT","Name":"Lithuania"},{"Code":"LU","Name":"Luxembourg"},{"Code":"MO","Name":"Macao"},{"Code":"MK","Name":"Macedonia,theFormerYugoslavRepublicof"},{"Code":"MG","Name":"Madagascar"},{"Code":"MW","Name":"Malawi"},{"Code":"MY","Name":"Malaysia"},{"Code":"MV","Name":"Maldives"},{"Code":"ML","Name":"Mali"},{"Code":"MT","Name":"Malta"},{"Code":"MH","Name":"MarshallIslands"},{"Code":"MQ","Name":"Martinique"},{"Code":"MR","Name":"Mauritania"},{"Code":"MU","Name":"Mauritius"},{"Code":"YT","Name":"Mayotte"},{"Code":"MX","Name":"Mexico"},{"Code":"FM","Name":"Micronesia,FederatedStatesof"},{"Code":"MD","Name":"Moldova,Republicof"},{"Code":"MC","Name":"Monaco"},{"Code":"MN","Name":"Mongolia"},{"Code":"ME","Name":"Montenegro"},{"Code":"MS","Name":"Montserrat"},{"Code":"MA","Name":"Morocco"},{"Code":"MZ","Name":"Mozambique"},{"Code":"MM","Name":"Myanmar"},{"Code":"NA","Name":"Namibia"},{"Code":"NR","Name":"Nauru"},{"Code":"NP","Name":"Nepal"},{"Code":"NL","Name":"Netherlands"},{"Code":"NC","Name":"NewCaledonia"},{"Code":"NZ","Name":"NewZealand"},{"Code":"NI","Name":"Nicaragua"},{"Code":"NE","Name":"Niger"},{"Code":"NG","Name":"Nigeria"},{"Code":"NU","Name":"Niue"},{"Code":"NF","Name":"NorfolkIsland"},{"Code":"MP","Name":"NorthernMarianaIslands"},{"Code":"NO","Name":"Norway"},{"Code":"OM","Name":"Oman"},{"Code":"PK","Name":"Pakistan"},{"Code":"PW","Name":"Palau"},{"Code":"PS","Name":"Palestine,Stateof"},{"Code":"PA","Name":"Panama"},{"Code":"PG","Name":"PapuaNewGuinea"},{"Code":"PY","Name":"Paraguay"},{"Code":"PE","Name":"Peru"},{"Code":"PH","Name":"Philippines"},{"Code":"PN","Name":"Pitcairn"},{"Code":"PL","Name":"Poland"},{"Code":"PT","Name":"Portugal"},{"Code":"PR","Name":"PuertoRico"},{"Code":"QA","Name":"Qatar"},{"Code":"RE","Name":"R\u00e9union"},{"Code":"RO","Name":"Romania"},{"Code":"RU","Name":"RussianFederation"},{"Code":"RW","Name":"Rwanda"},{"Code":"BL","Name":"SaintBarth\u00e9lemy"},{"Code":"SH","Name":"SaintHelena,AscensionandTristandaCunha"},{"Code":"KN","Name":"SaintKittsandNevis"},{"Code":"LC","Name":"SaintLucia"},{"Code":"MF","Name":"SaintMartin(Frenchpart)"},{"Code":"PM","Name":"SaintPierreandMiquelon"},{"Code":"VC","Name":"SaintVincentandtheGrenadines"},{"Code":"WS","Name":"Samoa"},{"Code":"SM","Name":"SanMarino"},{"Code":"ST","Name":"SaoTomeandPrincipe"},{"Code":"SA","Name":"SaudiArabia"},{"Code":"SN","Name":"Senegal"},{"Code":"RS","Name":"Serbia"},{"Code":"SC","Name":"Seychelles"},{"Code":"SL","Name":"SierraLeone"},{"Code":"SG","Name":"Singapore"},{"Code":"SX","Name":"SintMaarten(Dutchpart)"},{"Code":"SK","Name":"Slovakia"},{"Code":"SI","Name":"Slovenia"},{"Code":"SB","Name":"SolomonIslands"},{"Code":"SO","Name":"Somalia"},{"Code":"ZA","Name":"SouthAfrica"},{"Code":"GS","Name":"SouthGeorgiaandtheSouthSandwichIslands"},{"Code":"SS","Name":"SouthSudan"},{"Code":"ES","Name":"Spain"},{"Code":"LK","Name":"SriLanka"},{"Code":"SD","Name":"Sudan"},{"Code":"SR","Name":"Suriname"},{"Code":"SJ","Name":"SvalbardandJanMayen"},{"Code":"SZ","Name":"Swaziland"},{"Code":"SE","Name":"Sweden"},{"Code":"CH","Name":"Switzerland"},{"Code":"SY","Name":"SyrianArabRepublic"},{"Code":"TW","Name":"Taiwan,ProvinceofChina"},{"Code":"TJ","Name":"Tajikistan"},{"Code":"TZ","Name":"Tanzania,UnitedRepublicof"},{"Code":"TH","Name":"Thailand"},{"Code":"TL","Name":"Timor-Leste"},{"Code":"TG","Name":"Togo"},{"Code":"TK","Name":"Tokelau"},{"Code":"TO","Name":"Tonga"},{"Code":"TT","Name":"TrinidadandTobago"},{"Code":"TN","Name":"Tunisia"},{"Code":"TR","Name":"Turkey"},{"Code":"TM","Name":"Turkmenistan"},{"Code":"TC","Name":"TurksandCaicosIslands"},{"Code":"TV","Name":"Tuvalu"},{"Code":"UG","Name":"Uganda"},{"Code":"UA","Name":"Ukraine"},{"Code":"AE","Name":"UnitedArabEmirates"},{"Code":"GB","Name":"UnitedKingdom"},{"Code":"US","Name":"UnitedStates"},{"Code":"UM","Name":"UnitedStatesMinorOutlyingIslands"},{"Code":"UY","Name":"Uruguay"},{"Code":"UZ","Name":"Uzbekistan"},{"Code":"VU","Name":"Vanuatu"},{"Code":"VE","Name":"Venezuela,BolivarianRepublicof"},{"Code":"VN","Name":"VietNam"},{"Code":"VG","Name":"VirginIslands,British"},{"Code":"VI","Name":"VirginIslands,U.S."},{"Code":"WF","Name":"WallisandFutuna"},{"Code":"EH","Name":"WesternSahara"},{"Code":"YE","Name":"Yemen"},{"Code":"ZM","Name":"Zambia"},{"Code":"ZW","Name":"Zimbabwe"}]


def main():
    # handle CLI arguments
    parser = ArgumentParser(prog='show_weather',
                            description='Shows you the weather through the command line')
    parser.add_argument(
        'api_key', help='your personal OpenWeather API key')
    parser.add_argument(
        'city', help='the name of the city to lookup')
    parser.add_argument(
        '-a', '--all', action='store_true', help='print out all the weather information')
    parser.add_argument(
        '-d', '--description', action='store_true', help='include description in output')
    parser.add_argument(
        '-f', '--fahrenheit', action='store_true', help='give temperature in fahrenheit')

    args = parser.parse_args()
    api_key = args.api_key
    city_name = args.city.capitalize()

    # get weather data over the network
    final_url = f"{BASE_URL}appid={api_key}&q={city_name}"
    response = requests.get(final_url)
    weather_data = response.json()

    # extract from the JSON data
    klvn = weather_data['main']['temp']  # in kelvin
    temp = kelvin_to_fahrenheit(klvn) if args.fahrenheit else kelvin_to_celsius(klvn)
    country_code = weather_data['sys']['country']
    country_name = country_code_to_name(country_code)

    # print to stdout
    print('----------------------------------------------------------------\n')

    print(f"      Place:    {city_name}")
    print(f"    Country:    {country_name}")
    print(f"Temperature:    {temp:.1f}\xb0{'F' if args.fahrenheit else 'C'}")

    if args.description:
        description = weather_data['weather'][0]['description']
        print(f"Description:    '{description}'")

    if args.all:
        print('\n*** All the raw data from the API response ***')
        pprint(weather_data, indent=4)

    print('\n----------------------------------------------------------------')


def kelvin_to_fahrenheit(k):
    return 1.8 * k - 459.67


def kelvin_to_celsius(k):
    return k - 273.15


def country_code_to_name(country_code):
    """
    Converts an 'ISO 3166-1 alpha-2' country
    code to the corresponding country name.
    """
    with open(COUNTRY_DATA_FILENAME) as json_file:
        countries = json.load(json_file)

    for country in countries:
        if country['Code'] == country_code:
            country_name = country['Name']
            break

    return country_name


# program entry point
if __name__ == '__main__':
    main()
