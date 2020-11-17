# optimizer    				
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)    #확률적 경사하강법  #학습률 #모멘텀 #가중치 감소
optimizer_config = dict(grad_clip=None) #Gradient Clipping

# learning policy
lr_config = dict(
   policy='step',   #Learning rate scheduler
   warmup='linear',     #이외에 exp, constant 등
   warmup_iters=500,    #Number of Iteration for warmup
   warmup_ratio=0.001   #ratio
   step=[8, 11])        #Learning rate decay steps
total_epochs = 12   #Number of Iteration