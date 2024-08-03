from docx import Document

def saver(text,saved,v):
    for i in text:
        with open("Product_2.txt","a")as f:
            f.write(f"{v} = {i}\n")
        v += 1
    else:
        with open("Product_2.txt","r")as f:
            content = f.read()
            add = Document()
            add.add_paragraph(content)
            add.save(saved)

def file_txt(text,v):
    for i in text:
        with open("Product_files_.txt","a")as f:
            f.write(f"{v} = {i}\n")
        v += 1
my_products = []
a = 1
v = 0
money = int(input("Enter your Money: "))
print(f"Your Money Rs : {money}")
print("Your Products = 00\n")
print("******Wellcom To MR Aro Shoping Mals******\n")
shoping = {"mobiles":300,"cars":700,"guns":1000,"free fire":500,"toys":6100,"youtube":800,
           "facebook":500,"instgram":400,"whatsapp":7000,"projects":8999}
print_1 = ["facebook Rs:500","mobiles Rs:300","cars Rs:700","guns Rs:1000","free fire Rs:500",
            "toys Rs:6100","youtube Rs:800","intgram Rs:400","whatsapp Rs: 7000","projects Rs:8999"]
for i in print_1:
    print(i)
while True:
        bye = input('Enter your boy products Name: ')
        if bye in shoping and money >= shoping[bye]:
            money -= shoping[bye]
            v += shoping[bye]
            my_products.append(bye)
            print("Thank You ***Successfully***")
            print(f"Your Money Rs:{money}")
        elif bye == "00":
            for i in my_products:
                print(f":{i}")
            print(money)
            print(f'Your Total Pay Rs:{v}')
            home = input("\nYour Product Save to file\nEnter 1 file Docx\nEnter 2 file txt\nEnter choice: ")
            if home == "1":
                saver(my_products,"product_1.docx",a)
            elif home == "2":
                file_txt(my_products,a)
            break
        else:
            print("Your products is Not avalibale!")
            print(money)
            