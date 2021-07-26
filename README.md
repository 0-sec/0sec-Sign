# 0sec-Sign

零组文库积分签到，将就用,不喜勿喷

# 使用方式

## 1. Github action部署

### 1. Fork该仓库

### 2. 创建Secrets

-   创建`ZSECWIKIUSER`,填入文库账号(**必填**)

-   创建`ZSECWIKIPASS`,填入文库密码(**必填**)

-   创建`VCUSER`,填入验证码平台账号(**必填**)注册地址：ttshitu.com

-   创建`VCPASS`,填入验证码平台密码(**必填**)

-   创建`PUSHTYPE`,填入选择的推送渠道(可选)(dingtalk|telegram|ftpush|bark|enterprise\_wechat)(可选)

-   创建`DINGTALKACCESSTOKEN`(钉钉推送参数，可选)

-   创建`FTSERVERKEY`(方糖推送参数，可选)

-   创建`TELEGRAMTOKEN`,`TELEGRAMCHADID`,(Telegram推送参数，可选)

-   创建`BARKTOKEN`,`BARKSERVER`(Bark推送参数，可选)

-   创建`PLUSPUSH`(Plus推送参数，可选)

-   创建`EWECHATPUSHTOKEN`,`EWECHATAGENTID`,`EWECHATAPPSECRETS`(企业微信推送参数，可选)

### 3. 启用Action

点击 Actions，选择 **I understand my workflows, go ahead and enable them**

**由于 GitHub Actions 的限制，直接 fork 来的仓库不会自动执行！！！**

必须手动修改项目提交上去，最简单的方法就是修改下图的 README.md 文件（右侧有网页端编辑按钮）。
![](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519153752.png)

随便修改什么都行，修改完 commit 就可以了。

之后**每天 8 点**会自动执行一次脚本
![Pasted image 20210519153834](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519153834.png)
![Pasted image 20210519153916](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519153916.png)

## 2.云函数部署

什么是**云函数**？就是可以让你没有服务器、本地电脑不用下载Python也可以使用这个项目，而且还是**白嫖**！

既解决了很多人部署的麻烦，也给了那些被劝退的朋友回来的勇气，**十分钟**便可以全部弄完。

### 1. 进入云函数

这里拿腾讯云函数距离，没有的可以开通一下，地址：https://console.cloud.tencent.com/scf/list-create?rid=1&ns=default

### 2. 新建函数

新建方式选自定义创建，名称地域随意，运行环境python3.6,设置超时时间。

![Pasted image 20210519155422](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519155422.png)

选择在线编辑，执行方法默认

![Pasted image 20210519155521](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519155521.png)

### 3.复制0sec-Sign-Cloud.py代码

修改代码，填写文库账号，验证码平台账号

![Pasted image 20210519155711](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519155711.png)

如需要推送，请填写相关配置

### 4.触发器配置

下面展示了一些 Cron 表达式和相关含义的示例：

-   `0 0 10,14,16 * * * *` 表示在每天上午10点，下午2点，4点触发
-   `0 0 8 \*/1 \* \* \*`每天8点执行

官方文档：https://cloud.tencent.com/document/product/583/9708#cron-.E8.A1.A8.E8.BE.BE.E5.BC.8F

至此项目部署完毕，可进行测试查看是否配置成功

![Pasted image 20210519160638](https://github.com/l1angfeng/0sec-Sign/blob/main/Readme/images/Pasted%20image%2020210519160638.png)

# 推送方式

脚本提供了多种消息推送渠道供选择使用，便于用户查看执行结结果。以下多个推送方式可以同时多选使用。

## 1. 钉钉推送

使用dingtalk机器人推送脚本执行结果

1. 电脑登录钉钉建群
2. 添加机器人，设置关键字，复制webhook
3. 填入对应的部署方式

## 2. Server 酱 Turbo 推送

使用 Server 酱 Turbo 版可以绑定微信，将脚本每次的运行结果推送到你的微信上。

使用方法：

1.  访问[Server 酱 Turbo 版官网](https://sct.ftqq.com/)，点击**登入**，使用微信扫码登录

2.  登入成功后，按照网站上的说明选择消息通道，如**方糖服务号**（于 2021 年 4 月停止服务）

3.  点击**SendKey**，找到自己的 SendKey，并复制
4.  填入对应的部署方式

## 3. Telegram Bot 推送

使用 Telegram 机器人按时推送脚本执行结果。

使用方法：

1.  创建 Telegram 机器人并获取机器人 Token 以及个人账户的 Chat ID
2.  填入对应的部署方式

## 4. Bark 推送

使用 Bark App 实现推送（建议 iOS/iPadOS 用户使用）。

使用方法：

1.  安装 Bark 移动端程序
2.  复制应用内的示例 URL 并截取其中的 22 位随机字符串
3.  填入对应的部署方式

## 5. pushplus 微信公众号推送

使用[pushplus](http://www.pushplus.plus/)平台进行推送。

使用方法：

1.  访问[pushplus](http://www.pushplus.plus/)官网，登录
2.  找到**一对一推送**，并复制你的**token**
3.  填入对应的部署方式

## 6. 企业微信推送

使用方法:

1.  配置企业微信，获取企业 ID、应用 ID、应用 Secret
2.  填入对应的部署方式



