This folder contains the model trained on 70% of the dataset with the following parameters:
batch_size : 64
epochs : 8
optim.Adam(model.parameters(), lr=0.0005)
nn.BCEWithLogitsLoss()
threshold : 0.5 #for the classification

#Other parameters

transform_img = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406],
                             std=[0.229,0.224,0.225])
    ])

model.classifier = nn.Sequential(nn.Dropout(p=0.2,inplace=False),
                                          nn.Linear(in_features = num_ftrs,out_features = 256),
                                          nn.Dropout(p=0.5),
                                          nn.Linear(256,1))