# Project from Meng, Liang and Cheng (Laboratory of Health Dynamics, Faculty of Psychology, Beijing Normal University)
# Original statement: Code written entirely by Meng Yifan
# ！！Note: The article has not been published yet, the data is not public, please do not disclose the experimental information
# other questions please contact the author by email: 202011061075@mail.bnu.edu.cn
# Date Last Modified: May 7, 2022

library(tidyverse)
library(stringr)
library(readxl)
library(effsize)
library(cowplot)
library(ggpubr)
setwd("D:\\文件\\无聊进食\\data")
data_wide<-read.csv("tidy_main/peacetidy_totalwide.csv")
data_www<-read.csv("tidy_main/peacetidy_superwide.csv")
data_wide$Group <- as.factor(data_wide$Group)
data_wide$time <- as.factor(data_wide$state)

data_www <- data_www%>%
  mutate(lgchipintake_1=log(`chip.intake_1`+2),
         lgchipintake_2=log(`chip.intake_2`+2),
         lgchipintake_3=log(`chip.intake_3`+2),
         lgchipintake_total=log(chip.intake_total+2))
data_wide <- data_wide%>%
  mutate(lgintake=log(chip.intake+2))

#############
#分布
data_wide <- mutate(data_wide,lgintake=log(chip.intake+1))
shapiro.test(data_wide$lgintake[data_wide$Group=='b'])
shapiro.test(data_wide$lgintake[data_wide$Group=='b'&data_wide$state=="1"])
shapiro.test(data_www$lgchipintake_3[data_www$Group=='s'])

df<-filter(data_wide,state==1|state==2|state==3)
ggplot(df, aes(lgintake,color=Group)) +
  geom_histogram(bins=60)+
  geom_density()+
  facet_wrap(Group~ state,nrow=2)
ggplot(data = data_wide, mapping = aes(x = state, y = chip.intake,color=Group,group = interaction(Group, state))) +
  geom_boxplot()
ggplot(data = data_wide, mapping = aes(x = state, y = sad,color=Group,group = interaction(Group, state))) +
  geom_boxplot()

ggplot(data=df,aes(state,lgintake,group = interaction(Group, state)))+
  geom_boxplot(width=0.5,aes(color=Group),position = position_dodge(width = 0.8))+
  geom_point(aes(color = Group), position = position_jitterdodge(dodge.width = 0.8, jitter.width = 0.1))   
fit <- aov(lgintake~Group*state+Error(Sub/state),data=data)
summary(fit)

##异常值
databore <- filter(data_www,Group=='b')
datasad <- filter(data_www,Group=='s')
datapeace <- filter(data_www,Group=="p")
intakeout1b <- boxplot.stats(databore$lgchipintake_1)$out
intakeout1s <- boxplot.stats(datasad$lgchipintake_1)$out
intakeout2s <- boxplot.stats(datasad$lgchipintake_2)$out
intakeout3s <- boxplot.stats(datasad$lgchipintake_3)$out
print(subset(databore, lgchipintake_1 %in% intakeout1b)$Sub,
      subset(databore, lgchipintake_1 %in% intakeout1b)$chip.intake_1)

intakeout2p <- boxplot.stats(datapeace$lgchipintake_2)$out
intakeout_p <- boxplot.stats(datapeace$lgchipintake_total)$out

print(subset(datapeace, lgchipintake_total %in% intakeout_p)$Sub)

sadout <- boxplot.stats(databore$sad_1)$out
print(subset(databore, sad_1 %in% sadout)$Sub)
a <- filter(databore,sad_1==sadout)
sadout <- boxplot.stats(databore$sad_3)$out
a <- filter(databore,sad_3==sadout)

sadout <- boxplot.stats(datapeace$sad_1)$out
print(subset(datapeace, sad_1 %in% sadout)$Sub)
a <- filter(datapeace,sad_1==sadout)
sadout <- boxplot.stats(datapeace$sad_0)$out
print(subset(datapeace, sad_0 %in% sadout)$Sub)
b <- filter(datapeace,sad_0==sadout)
sadout <- boxplot.stats(datapeace$sad_2)$out
c <- filter(datapeace,sad_2==sadout)
sadout <- boxplot.stats(datapeace$sad_3)$out
print(subset(datapeace, sad_3 %in% sadout)$Sub)
c <- filter(datapeace,sad_3==sadout)

##删了
out <- filter(databore,lgchipintake_1 %in% intakeout1b)
write.csv(out,"D:/文件/无聊进食/实验一分析结果/boutbyintake1.csv")
intakeout2b <- boxplot.stats(databore$lgchipintake_2)$out
print(subset(databore, lgchipintake_2 %in% intakeout2b)$Sub)
###
data_www <- filter(data_www,Sub!="44b"&Sub!="20b"&Sub!="30b")
data_wide <- filter(data_wide,Sub!="44b"&Sub!="20b"&Sub!="30b")
###
intakeout1 <- boxplot.stats(data_www$lgchipintake_1)$out
intakeout2b <- boxplot.stats(databore$lgchipintake_2)$out
intakeout3b <- boxplot.stats(databore$lgchipintake_3)$out
#情绪的异常值
ggplot(data = data_wide, mapping = aes(x = state, y = bored,color=Group)) +
  geom_boxplot()
bore <- boxplot.stats(databore$bored_1)$out
print(subset(data_wide, lgchipintake_1 %in% intakeout1b)$Sub)
shapiro.test(data_wide$bored[data_wide$Group=='b'&data_wide$state=="1"])
ggplot(data = data_wide, mapping = aes(x = time, y = peace,color=Group,group = interaction(Group, state))) +
  geom_boxplot()
####
##方差齐性检验
bartlett.test(lgintake~as.factor(Group)*as.factor(state),data=data_wide)
library(car)
leveneTest(lgintake~time*Group,data=data_wide)
leveneTest(lgintake~Group,data=data_wide)
leveneTest(lgintake~time,data=data_wide)
leveneTest(chip.intake~state*Group,data=data_wide)
leveneTest(chip.intake~state,data=data_wide)
leveneTest(bored~time*Group,data=data_wide)
######
#分析
##视频情绪启动效应：
#两因素重复测量方差分析
primedata<-data_wide%>%
  filter(time==-1|time==0)%>%
  filter(Group!="s")
primeanovab <- aov(bored ~ time*Group+Error(Sub), data=primedata)
summary(primeanovab)
primedata<-data_wide%>%
  filter(time==-1|time==0)%>%
  filter(Group!="b")
primeanovas <- aov(sad ~ state*Group+Error(Sub/(state)), data=primedata)
summary(primeanovas)

##无关变量差异检验
f <- aov(hunger_degree~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(prone~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(DEBQ~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(BMI~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(ERQ~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(EIS总分~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(ERQ_认知重评~Group+Error(Sub),data=data_www)
summary(f)
f <- aov(ERQ_表达抑制~Group+Error(Sub),data=data_www)
summary(f)
extra <- data_www%>%
  group_by(Group)%>%
  summarise(hunger_degree=mean(hunger_degree),
            prone=mean(prone),
            DEBQ=mean(DEBQ,na.rm=TRUE),
            BMI=mean(BMI,na.rm=TRUE),
            EIS总分=mean(EIS总分,na.rm=TRUE),
            ERQ=mean(ERQ,na.rm=TRUE),
            ERQ_认知重评=mean(ERQ_认知重评,na.rm=TRUE),
            ERQ_表达抑制=mean(ERQ_表达抑制,na.rm=TRUE))
write.csv(extra,"D:/文件/无聊进食/实验一分析结果/额外变量结果.csv")

#描述统计
dis <- data_wide%>%
  group_by(Group,time)%>%
  summarise(mean_lgintake=mean(lgintake),
            sd_lgintake=sd(lgintake),
            se_lgintake=sd(lgintake)/sqrt(length(lgintake)),
            mean_chipintake=mean(chip.intake),
            sd_chipintake=sd(chip.intake),
            se_chipintake=sd(chip.intake)/sqrt(length(chip.intake)),
            mean_intention=mean(intention),
            sd_intention=sd(intention),
            se_intention=sd(intention)/sqrt(length(intention)),
            mean_bored=mean(bored),
            sd_bored=sd(bored),
            se_bored=sd(bored)/sqrt(length(bored)),
            mean_sad=mean(sad),
            sd_sad=sd(sad),
            se_sad=sd(sad)/sqrt(length(sad)),
            mean_peace=mean(peace),
            sd_peace=sd(peace),
            se_peace=sd(peace)/sqrt(length(peace)))

dis[,3:20] <- round(dis[,3:20],2)
write.csv(dis,"D:/文件/无聊进食/实验一分析结果/描述统计结果长new(两位小数).csv")
pdf("discribe_plots.pdf")
chipintake <- ggplot(data = dis, mapping = aes(x = time, y = mean_chipintake,group=Group)) +
  geom_line(size=1,aes(color=Group))+
  geom_point(size=3,aes(color=Group))+
  geom_text(aes(label = mean_chipintake), vjust = -1)+
  geom_errorbar(aes(ymin = mean_chipintake - se_chipintake, ymax = mean_chipintake + se_chipintake,color=Group), width = 0.2,size=0.8)
print(chipintake)
lgintake <- ggplot(data = dis, mapping = aes(x = time, y = mean_lgintake,group=Group)) +
  geom_line(size=1,aes(color=Group))+
  geom_point(size=3,aes(color=Group))+
  geom_text(aes(label = mean_lgintake), vjust = -1)+
  geom_errorbar(aes(ymin = mean_lgintake - se_lgintake, ymax = mean_lgintake + se_lgintake,color=Group), width = 0.2,size=0.8)
print(lgintake)
intention <- ggplot(data = dis, mapping = aes(x = time, y = mean_intention,group=Group)) +
  geom_line(size=1,aes(linetype=Group,color=Group))+
  geom_point(size=3,aes(shape=Group,color=Group))+
  theme_classic()+
  ylab("进食意图") +xlab("进食阶段")+labs(color="组别",shape="组别",linetype="组别")+
  #geom_text(aes(label = mean_intention), vjust = -1)+
  geom_errorbar(aes(ymin = mean_intention - se_intention, ymax = mean_intention + se_intention,color=Group), width = 0.2,size=0.8)
print(intention)
sad <- ggplot(data = dis, mapping = aes(x = time, y = mean_sad,group=Group)) +
  geom_line(size=1,aes(linetype=Group,color=Group))+
  geom_point(size=3,aes(shape=Group,color=Group))+
  theme_classic()+
  ylab("悲伤程度") +xlab("进食阶段")+labs(color="组别",shape="组别",linetype="组别")+
  #geom_text(aes(label = mean_sad), vjust = -1)+
  geom_errorbar(aes(ymin = mean_sad - se_sad, ymax = mean_sad + se_sad,color=Group), width = 0.2,size=0.8)
print(sad)
bored <- ggplot(data = dis, mapping = aes(x = time, y = mean_bored,group=Group)) +
  geom_line(size=1,aes(linetype=Group,color=Group))+
  geom_point(size=3,aes(shape=Group,color=Group))+
  theme_classic()+
  ylab("无聊程度") +xlab("进食阶段")+labs(color="组别",shape="组别",linetype="组别")+
  #geom_text(aes(label = mean_bored), vjust = -1)+
  geom_errorbar(aes(ymin = mean_bored - se_bored, ymax = mean_bored + se_bored,color=Group), width = 0.2,size=0.8)
print(bored)
# 关闭 PDF 设备
dev.off()
rm(chipintake,lgintake,intention,sad,bored)

chipintake <- ggplot(data = dis, mapping = aes(x = time, y = mean_chipintake,group=Group)) +
  geom_line(size=1,aes(linetype=Group,color=Group))+
  geom_point(size=3,aes(shape=Group,color=Group))+
  theme_classic()+
  ylab("薯片进食量(g)") +xlab("进食阶段")+labs(color="组别",shape="组别",linetype="组别")+
  geom_text(aes(label = mean_chipintake), vjust = -1)+
  geom_errorbar(aes(ymin = mean_chipintake - se_chipintake, ymax = mean_chipintake + se_chipintake,color=Group), width = 0.2,size=0.8)
print(chipintake)
lgintake <- ggplot(data = dis, mapping = aes(x = time, y = mean_lgintake,group=Group)) +
  geom_line(size=1,aes(linetype=Group,color=Group))+
  geom_point(size=3,aes(shape=Group,color=Group))+
  theme_classic()+
  ylab("对数转换后的薯片进食量") +xlab("进食阶段")+labs(color="组别",shape="组别",linetype="组别")+
  geom_text(aes(label = mean_lgintake), vjust = -1)+
  geom_errorbar(aes(ymin = mean_lgintake - se_lgintake, ymax = mean_lgintake + se_lgintake,color=Group), width = 0.2,size=0.8)


##################标定纵轴，对齐
y_min <- 1
y_max <- 3.5
ybreaks <- seq(ceiling(y_min), floor(y_max), by = 0.5)
sad <- ggplot(data = dis, mapping = aes(x = time, y = mean_sad,group=Group)) +
  geom_line(size=1,aes(color=Group))+
  geom_point(size=3,aes(color=Group))+
  geom_text(aes(label = mean_sad), vjust = -1)+
  geom_errorbar(aes(ymin = mean_sad - se_sad, ymax = mean_sad + se_sad,color=Group), width = 0.2,size=0.8)+
  scale_y_continuous(breaks = ybreaks,limits=c(y_min, y_max))
bored <- ggplot(data = dis, mapping = aes(x = time, y = mean_bored,group=Group)) +
  geom_line(size=1,aes(color=Group))+
  geom_point(size=3,aes(color=Group))+
  geom_text(aes(label = mean_bored), vjust = -1)+
  geom_errorbar(aes(ymin = mean_bored - se_bored, ymax = mean_bored + se_bored,color=Group), width = 0.2,size=0.8)+
  scale_y_continuous(breaks = ybreaks,limits=c(y_min, y_max))
plot_grid(sad ,bored, ncol=2,align="v")

ggpaired(df,x="time",y="lgintake",id="Sub",color="Group",xlab = "Time",ylab = "lgintake",palette="jco",line.color="gray",line.size=0.4,facet.by="Group")+theme_classic()+stat_compare_means(label='p.format',paired=TRUE)

#####
#方差分析

fit <- aov(lgintake~Group*time+Error(Sub/time),data=data_wide)
summary(fit)
omega_squared(fit)
fit <- aov(intention~Group*time+Error(Sub/time),data=data_wide)
summary(fit)
# 安装并加载 interactions 包
install.packages("interactions")
library(interactions)
# 可视化交互作用
with(data_wide, {
  interaction.plot(Group, time, lgintake, type = "b",fixed = TRUE)
})
interaction.plot(x.factor = Group, trace.factor = time, response = lgintake, 
                 data = data_wide, type = "b")
################################
library(bruceR)
data <- select(data_wide,Sub,Group,time,intention)
data <- na.omit(data)
MANOVA(data, subID="Sub",dv="intention",
       between="Group", within="time",sph.correction="GG")%>%
  EMMEANS("Group")%>%
  EMMEANS("time")%>%
  EMMEANS("Group", by="time")

######################注意：三个组的样本量不一致，所以不能用
TukeyHSD(fit, "Group")  # 比较 factor1 的水平之间的差异
TukeyHSD(fit, "time")  # 比较 factor2 的水平之间的差异

######################决策树就是试试玩儿~没啥用的
install.packages("ggRandomForests")
library(ggRandomForests)
library(lattice)
# 使用 lattice 库可视化模型系数
dotplot(coef(model))
plot(model)
# 提取预测值和观察值
data <- data.frame(predicted = predict(model), observed = model$fitted.values)
# 添加组信息
data$Group <- data_wide$Group
# 绘制散点图
ggplot(data, aes(x = predicted, y = observed, color = Group)) +
  geom_point() +
  geom_abline(slope = 1, intercept = 0, linetype = "dashed") +
  xlab("Predicted values") +
  ylab("Observed values") +
  ggtitle("Mixed-effects model visualization")


#对数转换
library(lme4)
library(nlme)
library(lmerTest)

model <- lmer(intention ~ bored*time + (1 | Sub)+(1 | Group), data = data_wide)
model <- lmer(lgintake ~ intention*Group + (1 | Sub), data = data_wide)
HLM_summary(model)
model <- lmer(lgintake ~ bored*time + (1 | Sub)+(1 | Group), data = data_wide)
model <- lmer(lgintake ~ intention*time + (1 | Sub)+(1 | Group), data = data_wide)
model <- lmer(lgintake ~ intention*time + (1 | Sub), data = data_wide)
model <- lmer(bored ~ lgintake*time +(1 | Sub)+(1 | Group), data =data_wide)
model <- lmer(intention ~ lgintake*time + (1 | Sub)+(1 | Group), data = data_wide)

data_wide$timec <- as.numeric(data_wide$state)
mymodel <- lmer(intention~Group*timec+(1|Sub),data_wide[data_wide$timec!=(-1),])
mymodel2<-lmer(lgintake~intention+Group*timec+(1|Sub),data_wide[data_wide$timec!=(-1),])
HLM_summary(model)

summary(model)
library(emmeans)
library(Ismeans)
library(multcomp)
summary(glht(model,linfct=c("intention:Groups-intention:Groupp=0")))
emmeans(model, pairwise~intention) 
emmeans(model, pairwise~bored|time) 
emmeans(model, pairwise~lgintake|time)

#或者将Group放到随机效应

fit <- lmer(lgintake~state*bored+(1|Sub)+(1|Group),data=data_wide)
summary(fit)

shapiro.test(data_wide$lgintake[data_wide$Group=='b'])
shapiro.test(data_wide$lgintake[data_wide$Group=='s'])
shapiro.test(data_wide$chip.intake[data_wide$Group=='b'])
shapiro.test(data_wide$chip.intake[data_wide$Group=='s'])

#################
#自回归交叉滞后模型
##对所有被试，所以要保证全部正态？
shapiro.test(data_wide$lgintake)
library(lavaan)

# Define the model
CLPM <- '
# Cross-lagged effects路径系数
#直接效应
lgchipintake_1 ~ beta*intention_0
lgchipintake_2 ~ beta*intention_1
lgchipintake_3 ~ beta*intention_2

intention_0 ~ b1*bored_0
intention_1 ~ b2*bored_1
intention_2 ~ b3*bored_2
intention_3 ~ b4*bored_3

intention_1 ~ e1*intention_0
intention_2 ~ e2*intention_1
intention_3 ~ e3*intention_2

bored_1 ~ f1*bored_0
bored_2 ~ f2*bored_1
bored_3 ~ f3*bored_2

lgchipintake_1 ~ alpha*bored_0
lgchipintake_2 ~ alpha*bored_1
lgchipintake_3 ~ alpha*bored_2
#螺旋效应
bored_1 ~ c*lgchipintake_1
bored_2 ~ c*lgchipintake_2
bored_3 ~ c*lgchipintake_3
#螺旋效应
intention_1 ~ d1*lgchipintake_1
intention_2 ~ d2*lgchipintake_2
intention_3 ~ d3*lgchipintake_3
#滞后效应
lgchipintake_2 ~ lgchipintake_1
lgchipintake_3 ~ lgchipintake_2
'
fit <- sem(CLPM, data = data_www)
summary(fit)
semPlot(fit, type = "std", what = "est")
Paths(fit)
library(lavaanPlot)
lavaanPlot(fit, layout = "tree", node_label = TRUE)

library(semPlot)
semPaths(fit, whatLabels = "par",
         layout="circle",
         edge.label.cex = 0.8, 
         style = "lisrel", sizeMan = 8)
################################
#特质：
##prone 分组
data_www <- data_www%>%
  mutate(bored_mean=(bored_0+bored_1+bored_2+bored_3)/4)
a <- quantile(data_www$prone,0.27)
b <- quantile(data_www$prone,0.73)
c <- quantile(data_www$bored_mean,0.5)
d <- quantile(data_www$bored_mean,0.6)
data_www <- data_www%>%
  mutate(pgroup=ifelse(prone < a, 1, 2))%>%
  mutate(bgroup=ifelse(bored_mean < c, 1,2))

data_www <- data_www%>%
  mutate(pgroup=ifelse(prone < a, 1, ifelse(prone < b, 2, 3)))
mutate(bgroup=ifelse(bored_mean < c, 1,2))
mutate(bgroup=ifelse(bored_mean < c, 1, ifelse(bored_mean < d, 2, 3)))
dataprone <- filter(data_www,pgroup!=2)
dataprone <- filter(dataprone,Group!="s")
dataprone <- filter(dataprone,bgroup!=2)
dataprone <- mutate(dataprone,group=ifelse(Group=="b",1,2))
fit <- aov(lgchipintake_total ~ pgroup*group+Error(Sub), data=dataprone)
fit <- aov(lgchipintake_1 ~ pgroup*group+Error(Sub), data=dataprone)
fit <- aov(bored_0 ~ pgroup*Group+Error(Sub), data=dataprone)
dataprone$pgroup <- as.factor(dataprone$pgroup)
dataprone$group <- as.factor(dataprone$group)
data_www$pgroup <- as.factor(data_www$pgroup)
data_www$bgroup <- as.factor(data_www$bgroup)
ggplot(data = dataprone, mapping = aes(x = pgroup, y = lgchipintake_total,fill=group)) +
  geom_bar(stat = "identity", position = "dodge")
ggboxplot(dataprone, x = "pgroup", y = "lgchipintake_total",
          color = "group", palette = "aaas",facet.by="group",xlab = "trait",
          add = "jitter")+ stat_compare_means(method = "t.test")+theme_classic()

MANOVA(dataprone, subID="Sub",dv="lgchipintake_total",
       between=c("Group","pgroup"))%>%
  EMMEANS("Group",by="pgroup")
fit <- lmer(lgchipintake_total ~ bored_mean+(1|pgroup), data=dataprone)

#ERQ
a <- quantile(data$ERQ,0.27)
b <- quantile(data$ERQ,0.73)
data <- data%>%
  mutate(pgroup=ifelse(ERQ < a, 1, ifelse(ERQ < b, 2, 3)))
dataERQ <- filter(data,pgroup!=2)
borelong <- borelong%>%
  mutate(pgroup_1=ifelse(ERQ < a, 1, ifelse(ERQ < b, 2, 3)))
boreERQ <- filter(borelong,pgroup_1!=2)
fit <- aov(lgchipintake_total ~ pgroup*Group+Error(Sub), data=dataERQ)
fit <- aov(bored ~ pgroup_1*state+Error(Sub), data=dataERQ)
fit <- aov(lgintake ~ pgroup_1*state+Error(Sub), data=dataERQ)
summary(fit)
ggplot(data = dataERQ, mapping = aes(x = pgroup_1, y = lgchipintake_total,fill=Group)) +
  geom_bar(stat = "identity", position = "dodge")
#EIS总分
data <- data_www%>%
  filter(Sub!="37p")
a <- quantile(data$ERQ总分,0.27)
b <- quantile(data$ERQ总分,0.73)
data <- data%>%
  mutate(pgroup=ifelse(EIS总分 < a, 1, ifelse(EIS总分 < b, 2, 3)))
dataEIS <- filter(data,pgroup!=2)
fit <- aov(lgchipintake_total ~ pgroup*Group+Error(Sub), data=dataEIS)
fit <- aov(bored_0 ~ pgroup*Group+Error(Sub), data=dataEIS)
ggplot(data = dataEIS, mapping = aes(x = pgroup, y = lgchipintake_total,fill=Group)) +
  geom_bar(stat = "identity", position = "dodge")

#ERQ_认知重评
data <- data_www%>%
  filter(Sub!="37p")
a <- quantile(data$ERQ_认知重评,0.27)
b <- quantile(data$ERQ_认知重评,0.73)
data <- data%>%
  mutate(pgroup=ifelse(ERQ_认知重评 < a, 1, ifelse(ERQ_认知重评 < b, 2, 3)))
dataERQ_认知重评 <- filter(data,pgroup!=2)
fit <- aov(lgchipintake_total ~ pgroup*Group+Error(Sub), data=dataERQ_认知重评)
fit <- aov(bored_0 ~ pgroup*Group+Error(Sub), data=dataERQ_认知重评)
ggplot(data = dataERQ_认知重评, mapping = aes(x = pgroup, y = lgchipintake_total,fill=Group)) +
  geom_bar(stat = "identity", position = "dodge")

#ERQ_表达抑制
data <- data_www%>%
  filter(Sub!="37p")
a <- quantile(data$ERQ_表达抑制,0.27)
b <- quantile(data$ERQ_表达抑制,0.73)
data <- data%>%
  mutate(pgroup=ifelse(ERQ_表达抑制 < a, 1, ifelse(ERQ_表达抑制 < b, 2, 3)))
dataERQ_表达抑制 <- filter(data,pgroup!=2)
fit <- aov(lgchipintake_total ~ pgroup*Group+Error(Sub), data=dataERQ_表达抑制)
fit <- aov(bored_0 ~ pgroup*Group+Error(Sub), data=dataERQ_表达抑制)
ggplot(data = dataERQ_表达抑制, mapping = aes(x = pgroup, y = lgchipintake_total,fill=Group)) +
  geom_bar(stat = "identity", position = "dodge")