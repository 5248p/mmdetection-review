# Two-Stream Inflated 3D ConvNet(I3D)

Two-Stream은 RGB와 Optical flow를 같이 사용하기 떄문에 붙여졌고 Inflated 3D ConvNet은 2D를 3D로 변환하여 사용하기 떄문에 붙은 이름이다.

RGB를 3D conv 함으로써 시간정보는 포함이 되지만, 그래도 여전히 행동 인식에는 부족한면이 있기 때문에 Optical flow도 사용한다. [논문](https://arxiv.org/pdf/1705.07750.pdf)

## Inflating 2D conv into 3D

2D ConvNet의 ImageNet dataset으로 모델을 3D ConvNet로 바꾸는 방법을 Inflating이라 한다. 

간단하게, dimension하나를 추가하고 pad를 줘서 모양을 맞추면 된다.N × N 필터는 N × N × N이 된다.

![inflat](./image/inflat.png "inflat")

3D Conv에서 ImageNet pre-trained 된 가중치들을 활용하려면 가중치를 N번 복사해 주면 된다.

![infcep](./image/infcep.png "infcep")
![model](./image/model.png "model")

* receptive field는 출력 레이어의 뉴런 하나에 영향을 미치는 입력 뉴런들의 공간 크기이다. 필터가 한번에 보는 영역. 필터크기=receptive field

    참조:[receptive field(수용영역, 수용장)과 dilated convolution(팽창된 컨볼루션)](https://m.blog.naver.com/PostView.nhn?blogId=sogangori&logNo=220952339643&proxyReferer=https:%2F%2Fwww.google.com%2F)

* Optical flow 란?

    기존 영상처리에서 움직이는 객체를 추적할때 자주 사용하던 방법입니다. Optical flow를 사용하면 움직이는 객체의 x방향 y방향의 벡터를 뽑아 낼 수 있습니다. 


## 실험 결과

##### 파라미터수와 인풋
![res1](./image/res1.png "res1")

![res2](./image/res2.png "res2")

##### pre-trained 사용유무
![res3](./image/res3.png "res3")

##### 비교 모델중 I3D가 제일 좋다.
![res4](./image/res4.png "res4")
