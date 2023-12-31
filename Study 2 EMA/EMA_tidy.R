#tidy
library(tidyverse)
library(stringr)
library(readxl)
setwd("D:\\文件\\无聊进食\\实验二EMA\\data")
#### main longitude data
dir() %>% str_subset("\\.xlsx$") -> fn
data=list()
for(i in 1:length(fn)){
  data[[i]]=read_xlsx(fn[i])
  col_name <- colnames(data[[i]])
  col_name <- sub("^\\d+、", "",col_name)
  colnames(data[[i]]) <- col_name
}
main_data=data[[1]]
for(j in 2:i){main_data=full_join(main_data,data[[j]])}
main_data <- main_data %>%
  rename("Sub"="被试编号")%>%
  mutate(Day=str_sub(main_data$`测试日期`,-1),
       Time=ifelse(`测试时间`=="10:00-11:00",1,ifelse(`测试时间`=="14:00-15:00",2,ifelse(`测试时间`=="18:00-19:00",3,4))),
       Positive=(`感兴趣的`+`精神活力高的`+`劲头足的`+`热情的`+`自豪的`+`警觉性高的`+`备受鼓舞的`+`意志坚定的`+`注意力集中的`+`有活力的`),
       Negative=(`心烦的`+`心神不宁的`+`内疚的`+`恐惧的`+`敌意的`+`易怒的`+`害羞的`+`紧张的`+`坐立不安的`+`害怕的`),
       MSBS=rowSums(select(., 24:47)))%>%
       select(-c("总分"))%>%
       filter(Sub!= "f094")
main_data <- main_data%>%
  mutate(S=ifelse(`具体进食了什么糖果类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         CD=ifelse(`具体进食了什么甜点类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         B=ifelse(`具体进食了什么饼干类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         CH=ifelse(`具体进食了什么膨化食品类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         M=ifelse(`具体进食了什么肉制类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         FR=ifelse(`具体进食了什么水果：请尽量用明确的语言报告种类和数量`==0,0,1),
         N=ifelse(`具体进食了什么干果、坚果：请尽量用明确的语言报告种类和数量`==0,0,1),
         Y=ifelse(`具体进食了什么酸奶：请尽量用明确的语言报告种类和数量`==0,0,1),
         D=ifelse(`具体进食了什么饮料：请尽量用明确的语言报告种类和数量`==0,0,1),
         I=ifelse(`具体进食了什么冷饮类零食：请尽量用明确的语言报告种类和数量`==0,0,1),
         O=ifelse(`具体进食了什么“其他”零食：请尽量用明确的语言报告种类和数量`==0,0,1))
main_data <- main_data%>%
  rename("food_craving_intensity"="此时你想要吃零食的食欲有多强？",
         "perceived_reason_of_snacking--hunger"="是否是因为饥饿进食了零食",
         "perceived_reason_of_snacking--liking"="是否因为很喜欢这种零食所以进食了零食",
         "perceived_amount_of_snacking(satiety)"="进食零食后，感到多大程度的饱腹感",
         "perceived_satisfaction_of_snacking"="多大程度上食欲得到了满足",
         "emotional_change_afterwards"="感受到情绪在本次进食零食后的变化",
         "Intention_level_of_improving_ones_emotion_by_behaving_since"="自上次填写到现在的这段时间，你有多想要做些什么来改善你的情绪？",
         "Intention_level_of_improving_ones_emotion_by_eating_since"="自上次填写到现在的这段时间，你有多想要通过进食来应对或改善你的情绪？",
         "snack_as_substitute"="是否用零食代替了正餐？")



food_data <- filter(main_data, snack_as_substitute !="是")
write.csv(food_data,"D:\\文件\\无聊进食\\实验二EMA\\tidy_longitude_snack_data.csv")
write.csv(main_data,"D:\\文件\\无聊进食\\实验二EMA\\tidy_longitude_data.csv")
#### basic information
BMI <- read_xlsx("D:\\文件\\无聊进食\\实验二EMA\\被试报名信息final.xlsx")
BMI <- BMI %>%
  rename("Sub"="序号","age"="2、年龄：","gender"="3、您的性别：")%>%
  select("Sub","age","gender","BMI")

DEBQ <- read_xlsx("D:\\文件\\无聊进食\\实验二EMA\\DEBQ.xlsx")
DEBQ <- DEBQ %>%
  rename("Sub"="1、基本信息")%>%
  select("Sub","DEBQ","DEBQ_EE","DEBQ_R","DEBQ_Ext")

EIS_ERQ <- read_xlsx("D:\\文件\\无聊进食\\实验二EMA\\EIS+ERQ.xlsx")
EIS_ERQ <- EIS_ERQ%>%
  rename("Sub"="实验编号：")%>%
  select("Sub","EIS","ERQ_认知重评","ERQ_表达抑制","ERQ")

BPS <- read_xlsx("D:\\文件\\无聊进食\\实验二EMA\\无聊倾向性量表BPS.xlsx")
BPS <- BPS%>%
  rename("Sub"="被试编号")%>%
  select("Sub","prone")

PSS <- read_xlsx("D:\\文件\\无聊进食\\实验二EMA\\感知压力量表PSS-14.xlsx")
PSS <- PSS%>%
  rename("Sub"="实验编号：","PSS"="总分")%>%
  select("Sub","PSS")
##### merge
Data <- full_join(main_data,BMI)
Data <- left_join(Data,DEBQ)
Data <- full_join(Data,BPS)
Data <- full_join(Data,EIS_ERQ)
Data <- full_join(Data,PSS)
##### individual level
Data_bySub <- full_join(BMI,DEBQ)
Data_bySub <- full_join(Data_bySub,BPS)
Data_bySub <- full_join(Data_bySub,EIS_ERQ)
Data_bySub <- full_join(Data_bySub,PSS)


food_Data <- filter(Data,snack_as_substitute!="是")
write.csv(Data,"D:\\文件\\无聊进食\\实验二EMA\\tidy_EMA_data.csv")
write.csv(food_Data,"D:\\文件\\无聊进食\\实验二EMA\\tidy_EMA_snack_data.csv")
write.csv(Data_bySub,"D:\\文件\\无聊进食\\实验二EMA\\data_by_Sub.csv")
