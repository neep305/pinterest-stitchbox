# pinterest-stitchbox
Testing the concept of Stitchbox

## STEP1. App 생성하기
```shell
1. Go to 'Apps'.
2. Agree to our terms and policies and click 'Create app'.
3. Choose a name and description for your app. Be careful, you won’t be able to change the name of your app later. Click Create
```

## STEP2. Authentication
> 1. Authorization code 얻기
```shell
https://api.pinterest.com/oauth/?
    response_type=code&
    redirect_uri=https://mywebsite.com/connect/pinterest/&
    client_id=12345&
    scope=read_public,write_public&
    state=768uyFys
``` 

> 2. Access Token 얻기
```shell
https://api.pinterest.com/v1/oauth/token?
    grant_type=authorization_code&
    client_id=12345&
    client_secret=6789abcd&
    code=xyz1010
```
