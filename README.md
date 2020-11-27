# 1. 개요

이번 반려동물 행동인식 프로젝트의 최종 목표는 감정인식이다. 그렇다면 우리는 우리가 현재 가진 데이터로 어떤 모델,알고리즘을 선택해야 좋은 결과물을 낼 수있을까. 
 
모델을 만들때 어떤 알고리즘이 어떤 상황에 적용되느냐의 기준이 없다. 예를 들어, 성능이 좋지만 연산 시간이 터무니 없이 길다던가, 이런 경우에는 실시간 행동 인식을 해야하는 우리의 상황과는 맞지 않다. 그래서 여러가지 알고리즘을 적용해보고 상황에 따라 좀더 목적에 맞는 것을 선택해야한다.

실 사용에서의 성능을 확보하는 좋은 방법은 미리 기학습(pre-trained)된 [backbone](#backbone)에 우리가 가지고 있는 데이터셋으로 [finetuning](#finetuning)을 하는 것이다. 하지만 유의해야하는 점은 데이터셋 종류에 따라서도 결과가 약간씩 차이가 있을 수 있다는 것이다.(bounding box를 다른형태로 친다던가) 물론 전부 학습시킨다면 결국에는 결과가 비슷하게 수렵하겠지만 굳이 혼동을 줄 필요는 없다. 

우리는 받은 데이터로 스크레치부터 모델을 훈련을 시킬것이다. 그리고 [mmaction2](https://github.com/open-mmlab/mmaction2)를 활용하였다. [mmaction2](https://github.com/open-mmlab/mmaction2)는 행동 인식의 다양한 모델들을 구현해 놓은 오픈소스 툴박스이다. 


# 2. 모델 선택

우리가 가진 데이터를 모든 모델에 적용시켜보면 가장 이상적이겠지만, 그렇게 하기엔 비효율적일뿐더러 시간도 많이 걸리게 된다.

우리는 [paperswithcode](https://paperswithcode.com/area/computer-vision)에서 제공해주는 벤치마크에서 높은 점수를 받은 모델들을 먼저 선별 하였다. 모두 state-of-the-art를 달성한 모델들이다.

[SlowFast Network](https://github.com/5248p/mmdetection-review/tree/main/slowfast%20network)

[Temporal Segment Network](https://github.com/5248p/mmdetection-review/tree/main/Temporal%20Segment%20Network)

[Temporal Shift Module](https://github.com/5248p/mmdetection-review/tree/main/Temporal%20Shift%20Module)


[ResneXt]()

[fast-rcnn]()

[Two-Stream inflated 3D convnet(I3D)](https://github.com/5248p/mmdetection-review/tree/main/Two-Stream%20Inflated%203D%20ConvNet)




# 3. 모델 평가 및 성능 비교

## 3.1 중간점검

    python 3.7.9 / num of GPU 4 / Geforce RTX 2080 Ti / Cuda 10.2 / pytorch

총 데이터셋 중 80%가 훈련 데이터로 쓰였고 나머지 20%는 성능 테스트로 쓰였다.

* ## slowfast network
    (epoch: 80, initial lr:0.005, dataset:952개)

    |epoch|learning rate|top1_acc|top5_acc|
    |------|---|---|---|
    |80|0.00525|0.125|0.65|
    |80|0.00525|0.15|0.675|
    |80|0.00525|0.325|0.6|
    |80|0.00525|0.2|0.625|
    |80|0.00525|0.3|0.775|
    |80|0.00525|0.225|0.725|
    |80|0.00525|0.275|0.85|
    |80|0.00525|0.35|0.75|
    |80|0.00525|0.275|0.725|
    |80|0.00525|0.27778|0.63889|

<img src="./image/slowfast.png" width="450px" height="300px" title="slowfast" alt="slowfast"></img><br/>

데이터양이 적어서 그런지 결과가 좋은 모습은 아니다. 마지막 top1 accuracy가 0.27778밖에 나오지 않았다.

* ## I3D
    (epoch: 50, initial lr: 1.000e-02, dataset:952개)

    |epoch|learning rate|top1_acc|top5_acc|
    |------|---|---|---|
    |50|1.000e-04|0.8500|1.0|
    |50|1.000e-04|0.8000|0.9500|
    |50|1.000e-04|0.7000|0.8750|
    |50|1.000e-04|0.9000|1.0|
    |50|1.000e-04|0.8500|0.9750|
    |50|1.000e-04|0.7750|1.0|
    |50|1.000e-04|0.6500|0.9500|
    |50|1.000e-04|0.7250|0.9750|
    |50|1.000e-04|0.9000|1.0|
    |50|1.000e-04|0.8056|0.9444|

<img src="./image/i3d_r50_50e.png" width="450px" height="300px" title="i3d_r50_50e" alt="i3d_r50_50e"></img><br/>

* ## TSN
    (epoch: 100, initial lr: 0.002, dataset:952개)

    |epoch|learning rate|top1_acc|top5_acc|
    |------|---|---|---|
    |100|2e-05|0.89583|1.0|
    |100|2e-05|0.89583|0.95833|
    |100|2e-05|0.95833|1.0|
    |100|2e-05|0.8125|1.0|
    |100|2e-05|0.875|0.97917|
    |100|2e-05|0.875|1.0|
    |100|2e-05|0.89583|1.0|
    |100|2e-05|0.79167|0.97917|
    |100|2e-05|0.91667|1.0|
    |100|2e-05|0.80556|1.0|

<img src="./image/1120TSN1X1X8X1600.png" width="450px" height="300px" title="1120TSN1X1X8X1600" alt="1120TSN1X1X8X1600"></img><br/>

* ## TSM r_101
    (epoch: 100, initial lr: 0.005, dataset:952개)

    |epoch|learning rate|top1_acc|top5_acc|
    |------|---|---|---|
    |100|5e-05|0.96429|1.0|
    |100|5e-05|0.96429|0.96429|
    |100|5e-05|1.0|1.0|
    |100|5e-05|0.96429|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|0.92857|1.0|
    |100|5e-05|0.96429|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|1.0|1.0|

<img src="./image/tsm_r101_954_100e.png" width="450px" height="300px" title="tsm_r101_954_100e" alt="tsm_r101_954_100e"></img><br/>

* ## TSM r_50
    (epoch: 100, initial lr: 2.000e-03, dataset: 1952개)

    |epoch|learning rate|top1_acc|top5_acc|
    |------|---|---|---|
    |100|5e-05|1.0|1.0|
    |100|5e-05|0.9750|1.0|
    |100|5e-05|0.9250|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|1.0|1.0|
    |100|5e-05|0.9250|1.0|
    |100|5e-05|0.9500|1.0|
    |100|5e-05|0.9750|1.0|
    |100|5e-05|0.7500|1.0|

<img src="./image/tsm_r50_1918_100e.png" width="450px" height="300px" title="tsm_r50_1918_100e" alt="tsm_r50_1918_100e"></img><br/>

TSM이 애초부터 적은 데이터셋에서도 성능이 잘나오게 설계가 되어서 그런지, 가장 성능이 좋은 모습을 모여준다. 마지막 TSM_r50가 1900장의 데이터셋을 사용하긴 하였지만, TSM r_101에서도 볼수있듯이 다른 모델들보다 성능이 잘나오는것을 확인할수있다. 한편으로는, 데이터셋을 전부 받았을때 과연 순위의 변화가 있을것인지에 대한 기대도 된다.

## 3.2 파이널



# 4. 결론



<hr/>

#### backbone

 큰 데이터셋(ImageNet 등)에 기학습된 딥러닝 모델. feature extract 역할을 한다.

#### finetuning

기존에 학습되어져 있는 모델에 추가 데이터를 투입하여 파라미터를 업데이트(미세조정)

####  
testtest