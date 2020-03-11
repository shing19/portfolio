## 设计背景

云中街的木屋群是日治时代的警察宿舍，当地人总是对此地畏惧三分。在云中街变身生活聚落后，即使地处闹市，比邻市场，这里也鲜有人迹。

![](static/projects/yun_lantern/process/1.jpg)

希望借由我们的设计，拉近社区居民与生活聚落的距离，来云中街认识自己小镇的历史和文化，同时也让来斗六求学的年轻人和观光的游客，在云中街感受到这座小镇独有的气息与魅力。

## 设计理念

### 关键词：守护

原来住在云中街的警察，是斗六的守护者，守护着当地的治安。现在的云中街是思想的守护者，开展哲学讲座、读书讨论，吸引中小学乃至大学生、工作人士来此地碰撞思想。而斗六人是云中街的守护者，男女老少来这里参加活动，留下回忆，是无数个回忆和经历重建了云中街，重建了每个斗六人心中的云中街。云中街作为结点，连接了每个斗六人的共识。

希望通过居民参与手作的形式，为云中街制作灯笼，用灯光点亮黑夜里的云中街，寄托社区居民对云中街的爱意，守护每个人心中的斗六。

### 装置互动艺术

由大家制作的灯笼，装点在云中街的各个角落，以”呼吸“的状态缓慢闪烁。灯笼通过声音捕捉，推断周围的人群数量，当聚集在云中街的人愈多，灯笼就愈亮，”呼吸“就相对愈急促。当人群散去时，灯笼也逐渐暗淡，”呼吸“趋于平缓，仿佛云中街陷入沉睡一般。

![](static/projects/yun_lantern/process/2.png)

对于当地居民来说，云中街是有生命的，灯笼仿佛就是云中街生命体征的象征，愈是活跃便愈是强烈。而为云中街亲手挂上灯笼的居民，身处其中，和灯笼保持一样的呼吸频率。所有在云中街的人，都可以感受到生命的共振。

### 手作共创

借由手做灯笼活动，让参加者能自己动手做，体会认真动手做的快乐，情侣和亲子也能在过程中学习合作与互动。

台湾在元宵节有提灯笼的习俗，日本也有在门口挂灯笼的习俗，我们融合两地传统文化进行了创新。灯笼本身设计成拼接模组，让人能体验到拼接的乐趣。灯笼表面的图形由制作者自己创作，所以能打造出自己独一无二的灯笼。

![](static/projects/yun_lantern/process/3.png)

制作者可以选择将灯笼带回家，或留在云中街。因此我们也设计了高级版的灯笼，可以借由手机遥控，还有声音控制，使灯笼更多样化。以及，中控版的灯笼，5个灯笼能进行同步互动的，非常适合室内空间中展示，让使用者感受到一场视觉飨宴。

![](static/projects/yun_lantern/process/process.png)

## 工业设计

利用 ID Factory 现有的材料：激光切割机和3mm厚的密积板，进行结构设计。为了全年龄向受众，结构拼接尽可能简化，以插接、卡榫形式为主，不用胶水。

![](static/projects/yun_lantern/process/4.png)

经过几代尝试与验证后，加以考虑电路安装，用AutoCAD画出加工图，并将云中街的LOGO融入到产品外观中。

![](static/projects/yun_lantern/process/5.svg)

再找到透光性良好的描图纸和防水的塑料膜，打印产品编号和售后服务联系方式的贴纸。

![](static/projects/yun_lantern/process/6.jpg)

## 技术实现

### 电控

洞洞板做底，Arduino nano为主控，连接3W小灯、锂电池、USB dip接口、光遮断器、ZIGBEE和充电模组。

![](static/projects/yun_lantern/process/7.png)

ZIGBEE作为物联网群控模块，当一个麦克风侦测到环境声音变化时，ZIGBEE发出信号，令一定范围内灯笼“呼吸”同频。

![](static/projects/yun_lantern/process/8.svg)

### 程式

将AutoDraw封装到app中，在绘制完成后对图案进行轴对称或中心对称处理，输出成PDF文档，发送至打印机。

![](static/projects/yun_lantern/process/9.png)

为ZIGBEE写控制程序，通过连接灯笼发射的Wi-Fi登录到控制页面，借Web App控制小灯。

![](static/projects/yun_lantern/process/10.png)

## 活动记录

![](static/projects/yun_lantern/process/11.JPG)

![](static/projects/yun_lantern/process/12.jpg)

![](static/projects/yun_lantern/process/13.png)

![](static/projects/yun_lantern/process/14.JPG)