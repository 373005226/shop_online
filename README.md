本项目在vue cli3基础上完成，后端采用的是python3.6+django+django restframwork

本网站目的是建立一个分布式高可用的前后端分离的网站，本网站会长期维护

本网站首页部分模仿于[苏宁超市](https://chaoshi.suning.com/?utm_source=baidu&utm_medium=cpc_chaoshix&utm_campaign=%E5%93%81%E7%89%8C%E8%AF%8D-%E8%B6%85%E5%B8%82&utm_content=88biaoti&utm_term=u27241169.c0.g0.k122828583134.a29715448827.pb&bd_vid=9626075559004225824)

**后期任务：**

- [ ] 添加品牌列表（BrandSale.vue）
- [ ] 添加修改密码功能
- [ ] 添加评论功能
- [ ] 添加秒杀专场
- [ ] 添加年货专场
- [ ] 添加指定节假日(双十一、双十二等)专场秒杀
- [x] 改写首页的分辨率自适应



**优化任务：**

- [x] 重新封装axios请求
- [ ] 全部页面添加动画
- [x] 默认地址表的重新设计
- [ ] 修改登录注册失败的信息反馈
- [ ] 商品详情页的不同规格商品的显示不同选择框
- [x] 每次登录注册后headers的信息都要刷新一下才能修改，要用改成vuex
- [x] 收藏商品的发送请求的异步任务，需要axios去设置先后顺序
- [ ] 购物车全选功能要用watch监听
- [x] 结算页面需要添加运费
- [ ] 结算页面需要添加checked验证
- [ ] 积分和购物商品点击加入购物车时，库存商品会两倍的形式减少，而不是减少指定数量
- [x] 解决积分商城当库存小于0时依然会占位



**后台任务：**

1. 超市自提人员：

   - [ ] 对配送人员送来的货物进行二次检验

   - [ ] 对自提方式的用户进行检验完发送验证提取码和确认订单结束状态

2. 订单管理员：

   - [ ] 查看订单的状态

   - [ ] 分配订单任务（对送货人员分配）
   
   - [ ] 接收用户的疑问请求（使用channel发送消息机制）
   
3. 后台管理员：

   - [ ] 对商品进行分类
- [ ] 查看销量图表
   - [ ] 价格信息的增删改查
   - [ ] 对公告的管理
   
4. 超级管理员：

   - [ ] 查看商品信息的操作人
   - [ ] 发布折扣商品
   - [ ] 发布优惠券
   - [ ] 查看用户的评论、反馈、新增的会员

   

