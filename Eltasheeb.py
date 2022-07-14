from bs4 import BeautifulSoup
import requests

f1 = open("CS&ST.txt","w")
f1.write('شعبة احصاء وحاسب \n\n')
f2 = open("CS&MATH.txt","w")
f2.write('شعبة رياضة وحاسب \n\n')
f3 = open("CS&PH.txt","w")
f3.write('شعبة فيزياء وحاسب \n\n')
f4 = open("MATH.txt","w")
f4.write('شعبة رياضة \n\n')
f5 = open("PH.txt","w")
f5.write('شعبة فيزياء \n\n')
f6 = open("AS.txt","w")
f6.write('شعبة فضاء \n\n')
f7 = open("Problems.txt","w")
f7.write('أرقام الجلوس التى لم يتم التعرف علي شعبتها \n')
f8 = open("arrangement.txt","w")
f8.write('الاسم : الترتيب : النسبة \n\n')
arrange = []
print("it's working be patient.")

url = 'https://hufossortingresults.codexeg.net/results/'
for i in range(3000, 3131):
    completeURL = url + str(i)
    page = requests.get(completeURL)
    if page.status_code == 200:
        content = page.content
        soup = BeautifulSoup(content, 'html.parser')
        res = soup.find(color="blue").get_text()
        names = soup.findAll('b')[1]
        names = list (names)
        name = names[2][13:-3]
        ran = names[26][24:-3]
        pre = names[10][32:-3]
        string = f"{pre} :  {ran}  :  {name}"
        arrange.append(string)
        if res ==" الإحصاء و علم الحاسب":
            f1.write(name)
            f1.write('\n')
        elif res ==" الرياضيات و علم الحاسب":
            f2.write(name)
            f2.write('\n')
        elif res ==" الفيزياء و علم الحاسب":
            f3.write(name)
            f3.write('\n')
        elif res ==" الرياضيات":
            f4.write(name)
            f4.write('\n')
        elif res == " الفيزياء":
            f5.write(name)
            f5.write('\n')
        elif res ==" الفضاء":
            f6.write(name)
            f6.write('\n')
        else:
            f7.write(str(i))
            f7.write('\n')

    else:
        continue
arrange.sort(reverse=True)
for i in arrange:
    f8.write(str(i))
    f8.write("\n")
print("Done, you can check your current directory, you will find new files.")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()