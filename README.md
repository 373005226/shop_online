# [shop_online_front](https://github.com/373005226/shop_online_front)

![](https://img.shields.io/badge/author-LY-blue)![](https://img.shields.io/badge/License-MIT-blue)![](https://img.shields.io/badge/build-Django2.2.9-green)![](https://img.shields.io/badge/build-djangorestframework%203.10.3-brightgreen)![](https://img.shields.io/badge/build-vue%20cli%203.11.0-brightgreen)

本项目采用了Django+Django rest-framework来写接口，vue来写前端，elementui来写的后台管理系统，虽然Django有自己的后台管理界面，但是Django拓展功能难度比较大，所以还是选择了elementui来写一个管理系统。

后台管理界面UI样式采用了github上的开源项目，用户的PC样式首页模仿了苏宁超市、网易严选，图片采用了京东商城和苏宁超市，如有侵权可联系373005226@qq.com删除。

如有疑问可以发邮件或者发送邮箱：373005226@qq.com

这里展示的是需要配置的版本(即需要配置支付、云片网的短信)

# 项目说明

### 其余项目地址：

后端地址：[https://github.com/373005226/shop_online_backend](https://github.com/373005226/shop_online_backend)

后端管理系统地址：[https://github.com/373005226/shopping_admin](https://github.com/373005226/shopping_admin)

项目开发说明，我会在我的博客中写开发项目的思路和详细说明，地址为：[https://www.ly-blog.top/](https://www.ly-blog.top/)，国内地址为：[https://liuyuan636.gitee.io](https://liuyuan636.gitee.io/)

### 项目说明：

这个项目也是我的毕业设计项目，开发一套完整的超市购物流程，包括用户购买、员工后台处理。本项目有pc端和移动端，但是移动端采用了graceui作为UI框架，graceui有版权不能分享至公共平台，所以移动端会采用重构UI的方式再开源；

PC端的支付、发送短信功能真实可用，但是为了防止被恶意使用，所以关键代码不展示，但是如下会教如何配置；

单体版没有支付、发送短信功能，但是流程完全可用，单体版等待我后续设计。

### 版本说明：

本项目如今还是有关键代码不能展示，本项目还是线上版本，还在开发单体版本(即没有短信发送功能和支付功能)

### 用户角色：

本项目的购买方式有线上送货到家和线下超市自提两种选购方式。

本项目有7个角色：

1. 用户：用户拥有pc端和移动端，主要功能是查看、选购商品、购买、修改地址、修改个人信息(昵称、头像)、登录、注册(手机号注册)、收藏商品、查看物流信息等，后续会加上浏览历史、询问客服功能
2. 拣货人员：拣货人员负责对用户购买的商品进行拣货；负责对验货人员打回来的疑问商品进行重新拣货；查看个人的拣货记录；
3. 验货人员：负责对拣货人员拣货完毕的商品进行二次验货；发现拣货错误的商品可以打回去给拣货人员进行二次拣货；如果是线下超市自提的订单，在二次验货完毕后给用户发送提取码，提取码正确则订单结束；如果是线上送货到家的购物方式，验货人员要确认超市的送货员是否正确，点击确认后订单才可以调整为送货状态
4. 订单分配员：负责对送货到家的购物方式的订单进行分配送货员；
5. 送货员：负责对线上送货到家的订单进行配送；
6. 后台管理员:负责商品的增删改查；负责分类的增删改查；负责处理疑问订单；负责处理评论信息；
7. 超级管理员：负责商品的增删改查；负责分类的增删改查；负责处理疑问订单；负责处理评论信息；负责优惠券的增删改查；负责对积分商品的增删改查；查看员工业绩以及信息；

### 项目流程：

本项目的运行流程如下：

线上送货到家：

用户购买商品-->拣货人员进行第一次拣货-->验货人员进行验货-->订单分配员对订单分配送货员-->验货人员确认送货员身份并且确认商品提被提取-->送货员对订单进行配送-->订单完成

线下超市自提：

用户购买商品-->拣货人员进行第一次拣货-->验货人员进行验货-->验货人员发送通知短信通知用户到超市提取-->用户到达超市，验货人员发送提取码，提取码正确才可以提取-->提取成功，订单结束

## 项目配置：

请在setting.py里面修改你的mysql数据库：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413162158.png)

修改你的redis数据库(如需要缓存)：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413162221.png)

申请你的支付宝秘钥(如需要)，[方法](https://www.cnblogs.com/crazymagic/articles/9866953.html)，[申请地址](https://auth.alipay.com/login/ant_sso_index.htm?goto=https%3A%2F%2Fopenhome.alipay.com%2Fplatform%2FappDaily.htm%3Ftab%3Dinfo)

得到的公钥秘钥放在trade/keys文件夹中：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413162741.png)

发送短信功能(如需要)，在：

utils文件夹里面添加一个名为`yunpian.py`的文件，如图：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413163748.png)

里面的配置如下，申请了云片网后，添加模板（即你短信发送的内容），具体配置如下所示：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413163546.png)



## 项目图片

本项目采用的是Django restframwork开发接口，如图所示：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413155051.png)

重写的后台如图所示：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413155625.png)

商城首页：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160032.gif)

商品详情：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160606.png)

搜索商品：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160305.gif)

积分商城：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160352.png)

订单物流查询：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160425.png)

购物车：

![](https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200413160458.png)