# mmdetection/configs/_base_/models/fast_rcnn_r50_fpn.py

# model settings
model = dict(
    type='FastRCNN',                                                        #물체검출용/2-stage method CNN
    pretrained='torchvision://resnet50',                                    #이미학습이된 resnet
    backbone=dict(                                                          #image to feature map
        type='ResNet',                    
        depth=50,                                                           #50개의 layer(depth)
        num_stages=4,                                                       #전체 계산을 4단계로 나눔
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,                                                    #한단계를 freeze해 overfit 방지
        norm_cfg=dict(type='BN', requires_grad=True),                       #Batch Normalization
        norm_eval=True,                                                     #EvalNorm
        style='pytorch'),                                                   #stride 2 layers are in 3x3 conv
    neck=dict(                                                              #feature map의 refinement와 reconfiguration
        type='FPN',                                                         #Feature pyrimid network
        in_channels=[256, 512, 1024, 2048],                                 
        out_channels=256,
        num_outs=5),
    roi_head=dict(
        type='StandardRoIHead',
        bbox_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=7, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=dict(
            type='Shared2FCBBoxHead',
            in_channels=256,
            fc_out_channels=1024,
            roi_feat_size=7,
            num_classes=2,
            bbox_coder=dict(
                type='DeltaXYWHBBoxCoder',
                target_means=[0., 0., 0., 0.],
                target_stds=[0.1, 0.1, 0.2, 0.2]),
            reg_class_agnostic=False,
            loss_cls=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
            loss_bbox=dict(type='L1Loss', loss_weight=1.0))))
# model training and testing settings
train_cfg = dict(
    rcnn=dict(
        assigner=dict(
            type='MaxIoUAssigner',
            pos_iou_thr=0.5,
            neg_iou_thr=0.5,
            min_pos_iou=0.5,
            match_low_quality=False,
            ignore_iof_thr=-1),
        sampler=dict(
            type='RandomSampler',
            num=512,
            pos_fraction=0.25,
            neg_pos_ub=-1,
            add_gt_as_proposals=True),
        pos_weight=-1,
        debug=False))
test_cfg = dict(
    rcnn=dict(
        score_thr=0.05,
        nms=dict(type='nms', iou_threshold=0.5),
        max_per_img=100))
