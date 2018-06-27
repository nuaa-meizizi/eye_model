# 环境
## python3.6 + sklearn

# eye_train.py
## 训练文件
# eye_predict.py
## 预测文件
### 预测格式
#### 六个指标
RIGHT_CLOS_CONF float 右眼开闭精确度  
LEFT_CLOS_CONF flaot 左眼开闭精确度  
BLINKING flaot 眨眼次数  
BLINK_FREQ flaot 眨眼频率  
PUPIL_R_DIAM flaot 右眼瞳孔径大小  
PUPIL_L_DIAM flaot 左右瞳孔径大小  
#### python predict.py 0.56 0.55 0.0 0.0 0.0035 0.00345 0.56 0.55 0.0 0.0 0.0035 0.00345 0.56 0.55 0.0 0.0 0.0035 0.00345
六个一组
以上示例有18个数 为18/6=3组
#### 返回数组 [1. 1. 1.]  为标签 1 为不疲劳 -1 为疲劳

# health_train.py 健康训练文件
# eye_predict.py 预测文件
## 5个指标
temperature 温度  
heartrate 心率  
weight 体重  
D 扩张压
S 收缩压
#### python health_predict.py 37.01471262813102 86 59 113 66 0 35.932006648342394 70 48 140 118
五个一组  
以上示例有10个数 两组  
#### 返回数组 [0 1]  0 不健康 1 健康