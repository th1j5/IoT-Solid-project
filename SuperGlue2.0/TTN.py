import requests as req



payload_login = {"username":"TheWifiMaster","password":"VOP2020"}


def SimulateUplink(data, login=payload_login):
    #gebruikte headers voor uplink te kunnen simmuleren

    header_login = {
        'Content-type': 'application/json;charset=UTF-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }

    #op voorand gekende urls
    url_login = 'https://account.thethingsnetwork.org/api/v2/users/login'
    url_uplink = 'https://console.thethingsnetwork.org/api/applications/iot_and_solid/devices/the_stupid_blue_board/uplink'

    with req.session() as s:
        # login
        login = s.post(url_login, json=payload_login, headers=header_login)
        if login.status_code == 200:
            print("login succes!")
        else:
            print("login failure!")
            return 0

        step2 = s.get('https://console.thethingsnetwork.org/', headers=header_login, allow_redirects=False)

        step3 = s.get(step2.headers['location'], headers=header_login, allow_redirects=False)

        step4 = s.get(step3.headers['location'], headers=header_login, allow_redirects=False)

        step5 = s.get('https://console.thethingsnetwork.org/refresh', headers=header_login)

        token = step5.json()['access_token']
        token_str = "Bearer " + token

        header_uplink = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
            'authorization': token_str

        }

        post = s.post(url_uplink, json=data, headers=header_uplink)
        if post.status_code == 204:
            print("data send! %s" % post.status_code)
            s.close()
            return 1
        else:
            print("data send failed! %s" % post.status_code)
            s.close()
            return 0
