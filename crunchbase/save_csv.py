# brew link --force openssl

import csv                                                                                                                            

filename = "ecommerce/companies-04-02-2020.csv" 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    # fields = csvreader.next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
    print(type(row))
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
    print("Total no. of rows: %d"%(len(rows))) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 


print(rows[1][14])
print('\n\n')
print(rows[2][14])

# rowsTemp = rows
# for r in range(len(rows)):
#     rows[r].append(foundersLink[r])
# 'cookie': '__cfduid=dc8e9afe0d514432a5409c5257eaf980f1580891053; _pxhd=71118eac2817d141d6521b5614023ae582f06925e8b9c567f97c245af9a1a832:e4305f81-47f0-11ea-a852-b37908212520; cid=rBsFWl46e7CFvAAwGdb3Ag==; _pxvid=e4305f81-47f0-11ea-a852-b37908212520; _pxff_ne=1; _pxff_wa=1; _px3=096f21e64b77f3b5fbf395f6884db81ec17c18f0c746e053bbd3db265f0f7f78:mxKi8pwQ2G+nW2XE1VV2XgU2usgjcf/CctcDaP+BScMPmWXh0wLxRzGc+4gYluA0UmkMGWJaeektpzb66aABdw==:1000:iaQAGGXdgofgZtET3R4vAWxCW7ejM0s5R4A3rz05jgcl9Y3+p6haYXY/oDSdiyfWBe/5rLNJJWcn7RzNsXNey+nHNfNp1Bh3KXrUNCPAX0joOWWXkZQ8DACWKx/1NkLe2Kgg/A4KLt1QXdvACSUpApgFdUeGeywg4ExI9T3uoD4=; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _ga=GA1.2.1007903799.1580891064; _gid=GA1.2.2065855134.1580891064; _gat_UA-60854465-1=1; _fbp=fb.1.1580891064747.1394099720; _hp2_ses_props.973801186=%7B%22r%22%3A%22https%3A%2F%2Fwww.crunchbase.com%2Fperson%2Fjiby-thomas%22%2C%22ts%22%3A1580891064487%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjiby-thomas%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%228983544961729747%22%2C%22pageviewId%22%3A%222827936134138092%22%2C%22sessionId%22%3A%224646637756809616%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
