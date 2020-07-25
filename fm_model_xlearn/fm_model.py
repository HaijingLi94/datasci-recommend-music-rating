import xlearn as xl

def fm_xlearn(df_train):
    fm_model = xl.create_fm()
    fm_model.setTrain(df_train)  # use the whole train dataset

    param = {'task':'reg',
         'lr':0.2,
         'lambda':0.002,
         'fold':10,
         'k':8,
         'metric':'rmse',
         'epoch':10}

    fm_model.cv(param)

if __name__ == "__main__":
    fm_xlean('libfm/train.txt')

