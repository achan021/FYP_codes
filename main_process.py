import pytorch_mobilenetv2_model as mv2

def main():
    model = mv2.get_net()
    train_loader, test_loader = mv2.load_dataset()
    mv2.train_model(model,train_loader)
    mv2.save_model(model, './base_case_folder/train_70.pth')

    # model = mv2.load_model(mv2.get_net(),'./base_case_folder/train_70.pth')
    mv2.evaluate(model,test_loader)


main()