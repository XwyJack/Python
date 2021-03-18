from urllib import request, error

if __name__ == '__main__':

    #url = "https://mail.qq.com/cgi-bin/frame_html?sid=KmgcbXK0Qaj6FSRE&r=01eff76236a38cc37ee55d4c07ddd341/"
    url = "http://www.renren.com/976410643/profile"
    # 如果填入了cookie 就可以直接登录了  手动爬取  数据不多的情况
    # headers = {
    #     "Cookie": "pgv_pvid=5384557530; uin=o0837361474; skey=@q5wBOS1lX; RK=gTzE4lPLX/; ptcz=fad31d2f7fc90031cddd8bd7191269fae8ba6437708ee15e3498f04e36916998; p_uin=o0837361474; pt4_token=Gy*Z79BtI4EGkTpt2IGS-t-E**SvUj5EVvI2mmPSMXc_; p_skey=ChgnoVNjJTz43mbjvsdSvR-y2nsl4i*9RgSCIYnQkiM_; tinfo=1616037491.0000*; wimrefreshrun=837361474&; qm_logintype=qq; qm_antisky=837361474&d529fc46643fba4d05ecb8d2129585a329e659f443dc22fbc90e5d0ddd22f8f1; qm_flag=0; qqmail_alias=837361474@qq.com; sid=837361474&2614f423558f782796d316fdb1e2c4ff,qQ2hnbm9WTmpKVHo0M21ianZzZFN2Ui15Mm5zbDRpKjlSZ1NDSVluUWtpTV8.; qm_username=837361474; qm_lg=qm_lg; new_mail_num=837361474&0; qm_domain=https://mail.qq.com; qm_ptsk=837361474&@q5wBOS1lX; CCSHOW=0000; foxacc=837361474&1; ssl_edition=sail.qq.com; edition=mail.qq.com; qm_loginfrom=837361474&wpt; username=837361474&837361474"
    # }

    headers = {
        "Cookie": "nonymid=kmehvblvveg945; depovince=GW; _r01_=1; JSESSIONID=abcPJ6ThcPfAJgs3tceHx; ick_login=1411d658-fdcd-46f9-906e-366bb6f48cf3; taihe_bi_sdk_uid=9f7f9ff8b58d29be09dd32a7ee554590; taihe_bi_sdk_session=b10a1bc3ac710e8c1861fb1976055c9b; ick=effec59e-d40c-4b77-9a14-c29b924734e2; wp_fold=0; jebecookies=edebd426-22ac-44f3-9e3e-9fc4fe061139|||||; _de=AF8392E60F638A06304B0C0E455D8A0E; p=a4466b996793fd9f640edb861d0900ff3; first_login_flag=1; ln_uact=18514587109; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=fa72b4b403f634934d1082d7c50088a03; societyguester=fa72b4b403f634934d1082d7c50088a03; id=976410643; xnsid=bbe3455a; loginfrom=syshome"
        }

    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode('utf-8')
    # html = rsp.read().decode('gbk')

    with open("renren.html", "w", encoding='utf-8') as f:
        f.write(html)

#  上面的例子 在打开网页后会出现短暂停留然后重新再进行登录，应该为从本地跳转导致  从renren.html来看已经拿到了万一的信息  应该没有问题