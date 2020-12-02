# Yolo v4

## Introduction


[youtube](https://www.youtube.com/watch?v=_JzOFWx1vZg)

[yolo v4](https://arxiv.org/pdf/2004.10934.pdf)는 다른 최신 네트워크들이 가지는 특징인 높은 정확도를 가지지만 낮은 FPS와 큰 mini-batch-size를 가져 많은 GPU 수가 필요한점을 개선하는데 초점을 맞췄다. 

![yolo1](./image/yolo1.png "yolo1")

Figure 1: Comparison of the proposed YOLOv4 and other
state-of-the-art object detectors. YOLOv4 runs twice faster
than EfficientDet with comparable performance. Improves
YOLOv3’s AP and FPS by 10% and 12%, respectively.


1) 일반적인 환경에서도 학습 가능 = 1개의 GPU만 필요하다.
2) BOF, BOS
3) CBn, PAN, SAM

![hnb](./image/hnb.png "hnb")

최신 detector는 주로 백본(Backbone)과 헤드(Head)라는 두 부분으로 구성된다. 백본은 입력 이미지를 feature map으로 변형시켜주는 부분이다. ImageNet 데이터셋으로 pre-trained 시킨 VGG16, ResNet-50 등이 대표적인 Backbone이다. 헤드는 Backbone에서 추출한 feature map의 location 작업을 수행하는 부분이다. 헤드에서 predict classes와 bounding boxes 작업이 수행된다. 

헤드는 크게 Dense Prediction, Sparse Prediction으로 나뉘는데, 이는 Object Detection의 종류인 1-stage인지 2-stage인지와 직결된다. Sparse Prediction 헤드를 사용하는 Two-Stage Detector는 대표적으로 Faster R-CNN, R-FCN 등이 있다. Predict Classes와 Bounding Box Regression 부분이 분리되어 있는 것이 특징이다. Dense Prediction 헤드를 사용하는 One-Stage Detector는 대표적으로  YOLO, SSD 등이 있다. Two-Stage Detector와 다르게, One-Stage Detector는 Predict Classes와 Bounding Box Regression이 통합되어 있는 것이 특징이다.

넥(Neck)은 Backbone과 Head를 연결하는 부분으로, feature map을 refinement(정제), reconfiguration(재구성)한다. 대표적으로 FPN(Feature Pyramid Network), PAN(Path Aggregation Network), BiFPN, NAS-FPN 등이 있다. 


• Input: Image, Patches, Image Pyramid

• Backbones: VGG16, ResNet-50, SpineNet, EfficientNet-B0/B7, CSPResNeXt50, CSPDarknet53

• Neck:
- Additional blocks: SPP, ASPP, RFB, SAM

- Path-aggregation blocks: FPN, PAN,
NAS-FPN, Fully-connected FPN, BiFPN, ASFF, SFAM

• Heads::
- Dense Prediction (one-stage):
        
    ◦ RPN, SSD, YOLO, RetinaNe (anchor based)

    ◦ CornerNet, CenterNet, MatrixNet, FCOS(anchor free)

- Sparse Prediction (two-stage):
  
    ◦ Faster R-CNN, R-FCN, Mask RCNN(anchor based)
   
    ◦ RepPoints(anchor free)

2.2. Bag of Freebies (BOF)

 BOF는 inference cost의 변화 없이 (공짜로) 성능 향상(better accuracy)을 꾀할 수 있는 딥러닝 기법들이다. 대표적으로 데이터 증강(CutMix, Mosaic 등)과 BBox(Bounding Box) Regression의 loss 함수(IOU loss, CIOU loss 등)이 있다. 이 기법들의 상세한 내용은 3.4 YOLO v4에서 소개하겠다.

 

2.3. Bag of Specials (BOS)

 BOS는 BOF의 반대로, inference cost가 조금 상승하지만, 성능 향상이 되는 딥러닝 기법들이다. 대표적으로 enhance receptive filed(SPP, ASPP, RFB), feature integration(skip-connection, hyper-column, Bi-FPN) 그리고 최적의 activation function(P-ReLU, ReLU6, Mish)이 있다. 이 기법들의 상세한 내용도 3.4절에서 소개하겠다.


adversarial attack

[cutmix](https://arxiv.org/pdf/1905.04899.pdf) = image augmentation의 방법

![cutmix](./image/cutmix.png "cutmix")


이미지의 일부를 다른 이미지에서 따온 patch로 대체한다. (mixup이나 cutout 보다 더나음)

data augmentation의 유일한 목적은 입력 이미지의 가변성을 증가시켜 설계된 물체 감지 모델이 다른 환경에서 얻은 이미지에 대해 더 높은 견고성을 갖도록 하는 것입니다.








1) Backbone : CSP-Darkent53

2) Neck : SPP(Spatial Pyramid Pooling), PAN(Path Aggregation Network)

3) Head : YOLO-v3 

1) WRC (weighted-residual-connections)
2) CSP (cross-stage-partial-connections)
3) CmBN (cross mini batch normalization)
4) SAT (self-adversarial-training)
5) Mish Activation
6) Mosaic Data Agumentation
7) Drop Block REgularization
8) CIOU Loss






[YOLO v4 리뷰 : Optimal Speed and Accuracy of Object Detection (공부중)](https://ropiens.tistory.com/33)