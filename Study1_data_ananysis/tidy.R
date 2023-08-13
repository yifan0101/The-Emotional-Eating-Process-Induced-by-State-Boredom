# Project from Meng, Liang and Cheng (Laboratory of Health Dynamics, Faculty of Psychology, Beijing Normal University)
# Original statement: Code written entirely by Meng Yifan
# ！！Note: The article has not been published yet, the data is not public, please do not disclose the experimental information
# other questions please contact the author by email: 202011061075@mail.bnu.edu.cn
# Date Last Modified: May 7, 2022

##进食量的连续变化：
##思路1：剩余量-初始量（g）最后都剩0
##    1‘：或者初始量归零，保持相同的基线
###预处理关键量：进食量、情绪值、意图、（人格变量）、时间
library(tidyverse)
library(stringr)
library(readxl)
setwd("D:\\文件\\无聊进食\\data")
dir() %>% str_subset("\\.csv$") -> fn
data=list()
Data=list()
data1=list()
stste<-c(NA,NA,NA,0,0,0,0,0,0,0,0,0,0,0,0,0,NA,NA,NA,NA,1,1,1,1,1,1,1,1,1,1,1,1,1,NA,NA,2,2,2,2,2,2,2,2,2,2,2,2,2,NA,NA,3,3,3,3,3,3,3,3,3,3,3,3,3,NA)
for(i in 1:length(fn)){
  data[[i]]=read.csv(fn[i])
  Data[[i]]<-data[[i]]%>%
    select(c("participant","age","gender","date","expName","imagefile","type","ques_resp.keys","intention_resp.keys"))
  Data[[i]]<-Data[[i]]%>%
    mutate(state=stste)%>%
    filter(!is.na(state))
  participant=Data[[i]]$participant[1]
  age=Data[[i]]$age[1]
  gender=Data[[i]]$gender[1]
  j<-1
  while (j<=4){
    k<- 12*j-11
    while (k<=12*j){
      Data[[i]][k,c("intention_resp.keys")]=Data[[i]][12*j+1,c("intention_resp.keys")]
      k<-k+1
    }
    Data[[i]]<-Data[[i]][-c(12*j+1),]
    j<-j+1
  }
  
  data1[[i]]<-Data[[i]] %>% 
    
    group_by(type,state) %>% 
    summarise( emotion= mean(ques_resp.keys),
               intention=mean(intention_resp.keys))
  data1[[i]]<-data1[[i]]%>%
    filter(!type==0)%>%
    mutate(Sub=participant,age=age,gender=gender)
}
rm(data)
tidydata<-data1[[1]]
g<-2
while(g<=length(fn))
{
  tidydata<-full_join(tidydata,data1[[g]])
  g<-g+1}
tidydata<-tidydata%>%
  ungroup()
tidydata<-tidydata%>%
  mutate(Sub=tolower(Sub))%>%
  mutate(Group=str_sub(tidydata$Sub,-1))

write.csv(tidydata,"tidy_main/totaltidy_main.csv")
#进食量数据
intakedata<-read_xlsx("D:\\文件\\无聊进食\\data\\intakedata\\tidyintakedata.xlsx")
data<-right_join(intakedata,tidydata)
data<-data%>%
  mutate(Group=tolower(Group))%>%
  arrange(Sub,state)
#前测情绪
emotion0<-read_xlsx("D:\\文件\\无聊进食\\data\\emotion0\\emotion0new.xlsx")
emotion0<-emotion0%>%
  select(c("Sub","bored","sad","peace","hunger_degree"))%>%
  mutate(state=-1)%>%
  mutate(Group=str_sub(emotion0$Sub,-1))
#personality
prone<-read_xlsx("D:\\文件\\无聊进食\\data\\emotion0\\prone.xlsx")
prone<-prone%>%
  select(c("Sub","prone"))%>%
  mutate(Group=str_sub(Sub,-1))
DEBQ<-read_xlsx("D:\\文件\\无聊进食\\data\\emotion0\\finedDEBQ.xlsx")
DEBQ<-DEBQ%>%
  select(c("Sub","DEBQ"))%>%
  mutate(Group=str_sub(Sub,-1))
BMI<-read_xlsx("D:\\文件\\无聊进食\\data\\emotion0\\BMI.xlsx")
BMI<-BMI%>%
  select(c("Sub","BMI"))%>%
  mutate(Group=str_sub(Sub,-1))
EISERQ<-read_xlsx("D:\\文件\\无聊进食\\data\\emotion0\\EIS+ERQ.xlsx")
EISERQ<-EISERQ%>%
  select(c("Sub","EIS总分","ERQ_认知重评","ERQ_表达抑制","ERQ"))%>%
  mutate(Group=str_sub(Sub,-1))

data_wide <- data %>% 
  pivot_wider(names_from = type, values_from= c("emotion"))%>%
  rename( c("bored" ="1", "peace"="2", "sad"="3"))

data_wide<-full_join(emotion0,data_wide)
data_wide<-right_join(prone,data_wide)
data_wide<-right_join(DEBQ,data_wide)
data_wide<-right_join(BMI,data_wide)
data_wide<-right_join(EISERQ,data_wide)
data_wide<-arrange(data_wide,Sub,state)
#错位
datalenth<-length(data_wide$age)/5
q<-1
while (q <=datalenth)
{data_wide[5*q-4,c("age","gender")]<-data_wide[5*q-3,c("age","gender")]
data_wide[5*q-2,c("hunger_degree")]<-data_wide[5*q-4,c("hunger_degree")]
data_wide[5*q-3,c("hunger_degree")]<-data_wide[5*q-4,c("hunger_degree")]
data_wide[5*q-1,c("hunger_degree")]<-data_wide[5*q-4,c("hunger_degree")]
data_wide[5*q,c("hunger_degree")]<-data_wide[5*q-4,c("hunger_degree")]
q<-q+1}
#终极变宽
data_www <- data_wide %>% 
  pivot_wider(names_from = state, values_from= c("chip-intake","intention","bored","sad","peace"))%>%
  mutate(`chip-intake_total`=`chip-intake_1`+`chip-intake_2`+`chip-intake_3`)

data_www <- data_www%>%
  mutate(lgchipintake_1=log(`chip-intake_1`+2),
         lgchipintake_2=log(`chip-intake_2`+2),
         lgchipintake_3=log(`chip-intake_3`+2))
write.csv(data,"tidy_main/totaltidy_total.csv")
write.csv(data_wide,"tidy_main/totaltidy_totalwide.csv")
write.csv(data_www,"tidy_main/totaltidy_superwide.csv")


##异常值检验
###以下内容是画图练习（不重要）
#箱型图
ggplot(data = data_wide, mapping = aes(x = reorder(state, `chip-intake`,FUN = median), y = log(`chip-intake`+1),color=Group)) +
  geom_boxplot()
lgintakeout1 <- boxplot.stats(data_www$lgchipintake_1)$out
print(subset(data_www, lgchipintake_1 %in% lgintakeout1)$Sub)
ggplot(data=data,aes(state,`chip-intake`,fill=Group))+
  geom_bar(stat="identity", color="black", position=position_dodge(),width=0.7,size=0.25)

ggplot(data = data_wide, mapping = aes(x = reorder(state,bored ,FUN = median), y = bored,color=Group)) +
  geom_boxplot()
ggplot(data = data_wide, mapping = aes(x = reorder(state,sad ,FUN = median), y = sad,color=Group)) +
  geom_boxplot()
ggplot(data = data_wide, mapping = aes(x = reorder(state,peace ,FUN = median), y = peace,color=Group)) +
  geom_boxplot()
ggplot(data = data_wide, mapping = aes(x = reorder(state,intention ,FUN = median), y = intention,color=Group)) +
  geom_boxplot()
#分布图
ggplot(data_wide, aes(`chip-intake`,color=Group)) +
  geom_histogram(bins=60)+
  facet_wrap(Group~ state,nrow=2)
ggplot(data_wide, aes(`chip-intake`,color=Group)) +
  geom_density(alpha=0.55,bw=1,size=0.6)+
  facet_grid(Group~ state)

ggplot(data_wide, aes(bored,color=Group)) +
  geom_histogram(bins=60)+
  facet_wrap(Group~ state,nrow=2)
ggplot(data_wide, aes(bored,color=Group)) +
  geom_density(alpha=0.55,bw=1,size=0.6)+
  facet_grid(Group~ state)
ggplot(data_wide, aes(intention,color=Group)) +
  geom_density(alpha=0.55,bw=1,size=0.6)+
  facet_grid(Group~ state)
#峰峦图
install.packages("ggridges")
library(ggridges)
ggplot(data_wide, aes(x =`chip-intake`, y =state,group = state,color=Group)) +
  geom_density_ridges()+
  stat_density_ridges(quantile_lines = TRUE, quantiles = 2)+
  facet_wrap(~Group)
ggplot(data_wide, aes(x =bored, y =state,group = state,color=Group,height = stat(density))) +
  geom_density_ridges(stat = "density")+
  stat_density_ridges(quantile_lines = TRUE, quantiles = 2)+
  facet_wrap(~Group)
ggplot(data_wide, aes(x =sad, y =state,group = state,color=Group)) +
  geom_density_ridges()+
  stat_density_ridges(quantile_lines = TRUE, quantiles = 2)+
  facet_wrap(~Group)
ggplot(data_wide, aes(x =intention, y =state,group = state,color=Group)) +
  geom_density_ridges2()+
  stat_density_ridges(quantile_lines = TRUE, quantiles = 2)+
  facet_wrap(~Group)
#折线图
a<-data_wide%>%
  group_by(Group,state)%>%
  summarise(intake=mean(`chip-intake`))
ggplot(data=data_www,aes(y=,x=state,color=Group ))+
  geom_line(size=2) + xlab("阶段") + ylab("薯片进食量[g]") + ggtitle("进食量折线图")
#相关
ggplot(data = data_wide) +
  geom_point(mapping = aes(x = `chip-intake`, y = bored,color=Group)) +
  geom_smooth(mapping = aes(x =`chip-intake`, y = bored,color=Group))+
  facet_wrap(~state)
ggplot(data = data_wide) +
  geom_point(mapping = aes(x = `chip-intake`, y = sad,color=Group)) +
  geom_smooth(mapping = aes(x =`chip-intake`, y = sad,color=Group))+
  facet_wrap(~state)
#正态检验
shapiro.test(data_wide$`chip-intake`[data_wide$Group=='b'])
shapiro.test(data_wide$`chip-intake`[data_wide$Group=='s'])
shapiro.test(data_wide$`chip-intake`[data_wide$Group=='b'&data$state=="3"])
shapiro.test(data_wide$intention[data_wide$Group=='s'])
shapiro.test(data_wide$intention[data_wide$Group=='b'])
shapiro.test(data_www$`chip-intake_total`[data_wide$Group=='b'])
shapiro.test(data_www$`chip-intake_total`[data_wide$Group=='s'])
#对数正态吗？

#方差齐性检验
install.packages("car")
library(car)
leveneTest(data_wide$`chip-intake`~as.factor(data_wide$state)*as.factor(data_wide$Group))
leveneTest(data_wide$intention~as.factor(data_wide$state)*as.factor(data_wide$Group))
leveneTest(intention ~ state*Group, data=data_wide)
sum<-data_wide %>% 
  group_by(Group,state)
summarise( emotion= mean(ques_resp.keys),
           intention=mean(intention_resp.keys))
ggplot(data_wide, aes(`chip-intake`,color=Group)) +
  geom_histogram(bins=60)+
  geom_density()+
  facet_wrap(Group~ state,nrow=2)
ggplot(data=data_wide,aes(state,sad,group=Group,color=Group))+
  geom_point(size=4)+
  geom_smooth(method = 'loess',span=0.4,se=TRUE,colour="#00A5FF",fill="#00A5FF",alpha=0.2)
geom_line(position = position_dodge(0.1),cex=1.3)

ggplot(data=data_wide,aes(state,peace,group=Group,color=Group))+
  geom_point(size=4)+
  geom_smooth(method = 'loess',span=0.4,se=TRUE,colour="#00A5FF",fill="#00A5FF",alpha=0.2)
geom_line(position = position_dodge(0.1),cex=1.3)

aggregate(data_wide,by=Group)
#方差分析
fit <- aov(`chip-intake`~state*Group+Error(Sub/state),data=data_wide)
summary(fit)

fit <- aov(intention~state*Group+Error(Sub/state),data=data_wide)
summary(fit) 