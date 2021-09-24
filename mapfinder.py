import requests
import urllib3
# //# sourceMappingURL=yourFileName.min.js.map
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
with open('rezMAP.log', 'w') as f:
    f.write("")
    f.close()
host = 'https://pornhub.com'
req = requests.get(host, timeout=7)
list_res = []
temp_text = req.text

while True :

    pos = temp_text.find('src=')
    if (pos == -1):
        break
    temp = temp_text[pos:pos+150]
    finded_end = temp.find('.js')
    if (finded_end != -1):
        rez = temp[:finded_end + 3]
        rez = rez.replace('src="', '')
        rez = rez.replace('src=\'', "")
        rez = rez.replace('src=\n', "")
        list_res.append(rez)

    temp_text = temp_text[pos + 1:]

print(list_res)

l = len(list_res)
t = 0
while t != l:
    # deleting google from the World
    try:
        if list_res[t].find("google") != -1:
            list_res.remove(list_res[t])
        if list_res[t].find("google") == -1:
            t = t + 1
    except:
        break

print(list_res)
list_res_2 = []
for j in list_res:

    try:
        req = requests.get(host + j, timeout=7)
        temp_text = req.text

        while True:

            pos = temp_text.find('src=')
            if (pos == -1):
                break
            temp = temp_text[pos:pos + 150]
            finded_end = temp.find('.js')
            if (finded_end != -1):
                rez = temp[:finded_end + 3]
                rez = rez.replace('src="', '')
                rez = rez.replace('src=\'', "")
                rez = rez.replace('src=\n', "")
                rez = rez.replace('src=', '')
                list_res_2.append(rez)

            temp_text = temp_text[pos + 1:]
    except:
        print("Cannot connect to " + host + j)
list_res.extend(list_res_2)

l = len(list_res)
for j in list_res:
    # j = j.replace('//','/')
    try:
        print("> Checking " + j)
        try:
            req_js = requests.get(j, timeout=7)
        except:
            if j[0] == "/":
                req_js = requests.get(host + j, timeout=7)
            else:
                req_js = requests.get(host + "/" + j, timeout=7)

        print("Response: " + str(req_js.status_code) + "\n")
        print("> Checking " + j + ".map")


        try:
            req_js_with_map = requests.get(j + ".map", timeout=7)
        except:
            if j[0] == "/":
                req_js_with_map = requests.get(host + j + ".map", timeout=7)
            else:
                req_js_with_map = requests.get(host + "/" + j + ".map", timeout=7)

        if req_js_with_map.status_code == 200:
            print(">>>>>>>>>>>>>>>> YES! Map File Founded! <<<<<<<<<<<<<<<<<<<<")
            with open('rezMAP.log', 'a') as f:
                f.write(
                    "===========================================START=" + j + "=START===========================> \n\n")
                f.write(req_js_with_map.text)
                f.write("\n\n=======================END===" + j + "===END==========================> \n\n ")
                f.close()


    except:
        print("Something wrong! Sorry! It is lazy to do something here")


req = requests.get(host, timeout=7)
temp_text = req.text
finded = temp_text.find('sourceMappingURL=')
if finded != -1:
    print('There is map file inside!\n\n')
    temp = temp_text.text[finded:]
    finded_end = temp.find('.map')
    rez = temp[:finded_end + 4]
    print(rez)

    rez = rez.replace('sourceMappingURL=', '')
    print("> Getting map file\n\n")
    print("> CHECK MAP INSIDE rezMAP.log")
    print("Try to connect to " + rez + '.map')
    map_load = requests.get(host + rez + '.map')

    with open('rezMAP.log', 'a') as f:
        f.write("===========================================START=" + rez + "=START===========================> \n\n")
        f.write(map_load.text)
        f.write("\n\n=======================END===" + rez + "===END==========================> \n\n ")
        f.close()
        # print(map_load.text)
else:
    print("There is no map file inside main page " + host + " continue...")
    # exit()


print("CHECK rezMAP.log for results!")
